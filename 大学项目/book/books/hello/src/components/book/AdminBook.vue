<template>
  <!-- 搜索输入框和按钮 -->
<el-button class="adjust-button-position" @click="showDialog">新增书籍</el-button>
  <el-dialog v-model="dialogVisible" :width="dialogWidth" @close="resetForm">
    <el-form :model="form" label-width="80px">
      <el-form-item label="书籍名称">
        <el-input v-model="form.book_name" size="small" style="height: 30px;"></el-input>
      </el-form-item>
      <el-form-item label="出版社">
        <el-input v-model="form.Publishing_house" size="small" style="height: 30px;"></el-input>
      </el-form-item>
      <el-form-item label="作者">
        <el-input v-model="form.author" size="small" style="height: 30px;"></el-input>
      </el-form-item>
      <el-form-item label="价格">
        <el-input v-model="form.Price" size="small" style="height: 30px;"></el-input>
      </el-form-item>
      <el-form-item label="编号">
        <el-input v-model="form.mobile" size="small" style="height: 30px;"></el-input>
      </el-form-item>
      <el-form-item label="状态">
        <el-input v-model="form.status" size="small" style="height: 30px;"></el-input>
      </el-form-item>
    </el-form>
    <template v-slot:footer>
            <span class="dialog-footer">
              <el-button @click="dialogVisible = false">取消</el-button>
              <el-button type="primary" @click="submitForm">提交</el-button>
            </span>
    </template>
  </el-dialog>
  <el-input
      v-model="searchKeyword"
      placeholder="输入关键字搜索..."
      style="width: 200px;"
  >


  </el-input>

  <el-button type="primary" @click="searchBooks">搜索</el-button>

  <div>
    <el-table :data="displayedData" style="width: 100%">
      <el-table-column label="书名" prop="book_name"></el-table-column>
      <el-table-column label="出版社" prop="Publishing_house"></el-table-column>
      <el-table-column label="作者" prop="author"></el-table-column>
      <el-table-column label="价格" prop="Price"></el-table-column>
      <el-table-column label="编号" prop="mobile"></el-table-column>
      <el-table-column label="状态">
        <template v-slot="{ row }">
          <span>{{ row.status === 1 ? '启用' : '禁用' }}</span>
        </template>
      </el-table-column>

      <el-table-column label="操作">
        <template v-slot="{ row }">
          <!-- 编辑书籍信息的弹出框 -->
          <el-popover
              placement="right-end"
              width="360"
              trigger="click"
              v-model:visible="row.editPopoverVisible"
          >
            <!-- 编辑书籍信息的表单 -->
            <el-form :model="editingBook" ref="ruleForm" label-width="100px" class="demo-ruleForm">
              <el-form-item label="书名" prop="book_name">
                <el-input v-model="editingBook.book_name"></el-input>
              </el-form-item>
              <el-form-item label="出版社" prop="Publishing_house">
                <el-input type="text" v-model="editingBook.Publishing_house" autocomplete="off"></el-input>
              </el-form-item>
              <el-form-item label="作者" prop="author">
                <el-input type="text" v-model="editingBook.author" autocomplete="off"></el-input>
              </el-form-item>
              <el-form-item label="价格" prop="Price">
                <el-input type="text" v-model="editingBook.Price" autocomplete="off"></el-input>
              </el-form-item>
              <el-form-item label="编号" prop="mobile">
                <el-input type="text" v-model="editingBook.mobile" autocomplete="off"></el-input>
              </el-form-item>
              <el-form-item label="状态" prop="status">
                <el-input type="text" v-model="editingBook.status" autocomplete="off"></el-input>
              </el-form-item>
              <el-form-item>
                <el-button size="default" type="primary" @click="submitEdit(row)">提交</el-button>
                <el-button size="default" @click="cancelEdit(row)">取消</el-button>
              </el-form-item>
            </el-form>
            <!-- 触发编辑的按钮 -->
            <template v-slot:reference>
              <el-button @click="editBook(row)">编辑</el-button>
            </template>
          </el-popover>

          <!-- 删除按钮 -->
          <el-button @click="showDeleteConfirm(row.id)" type="danger">删除</el-button>
        </template>
      </el-table-column>
    </el-table>

    <!-- 分页器 -->
    <div class="pagination-container">
      <el-pagination
          @current-change="handlePageChange"
          :current-page="currentPage"
          :page-size="pageSize"
          :total="data.length"
      >
      </el-pagination>
    </div>
  </div>
</template>


<script>
import axios from "axios";

export default {
  computed: {
    filteredData() {
      if (this.searchKeyword === "") {
        return this.data;
      } else {
        const keyword = this.searchKeyword.toLowerCase();
        return this.data.filter(book => {
          return (
              book.book_name.toLowerCase().includes(keyword) ||
              book.Publishing_house.toLowerCase().includes(keyword) ||
              book.author.toLowerCase().includes(keyword) ||
              book.Price.toString().includes(keyword) ||
              book.mobile.toString().includes(keyword) ||
              (book.status === 1 ? "启用" : "禁用").includes(keyword)
          );
        });
      }
    },
    displayedData() {
      const startIndex = (this.currentPage - 1) * this.pageSize;
      const endIndex = startIndex + this.pageSize;
      return this.filteredData.slice(startIndex, endIndex);
    },
  },

  data() {
    return {
      data: [],
      users: [],
      dialogVisible: false,
      dialogWidth: '400px', // 设置弹窗宽度
      form: {
        book_name: '',
        Price: '',
        author: '',
        Publishing_house: '',
        mobile: '',
        status: '',
      },
      searchKeyword: "", // 搜索关键字
      editingBook: {
        Publishing_house: "",
        author: "",
        Price: "",
        mobile: "",
        status: "",
      },
      currentPage: 1, // 当前页码
      pageSize: 20, // 每页显示的书籍数量
    };
  },
  mounted() {
    this.getData();
  },
  methods: {


    //新增
    submitForm() {
      // 构造要发送到服务器的数据
      const newUser = {
        book_name: this.form.book_name,
        Price: this.form.Price,
        author: this.form.author,
        Publishing_house: this.form.Publishing_house,
        mobile: this.form.mobile,
        status: this.form.status,
      };
      // 向服务器发送 POST 请求来添加新管理员
      axios
          .post("http://seqnqc.natappfree.cc/api/publishes/", newUser)
          .then((response) => {
            // 添加成功后，刷新管理员列表
            this.loadUsers();
            // 重置表单
            this.dialogVisible = false;
            this.resetForm();
          })
          .catch((error) => {
            console.error(error);
            // 在实际应用中，你可能会根据服务器返回的错误信息进行适当的处理
          });
      this.dialogVisible = false;
      this.resetForm();
    },

    resetForm() {
      this.form.book_name = '';
      this.form.Price = '';
      this.form.author = '';
      this.form.Publishing_house = '';
      this.form.mobile = '';
      this.form.status = '';
    },
    showDialog() {
      this.dialogVisible = true;
    },
    searchBooks() {
      this.currentPage = 1; // 重置当前页码为第一页
    },
    handlePageChange(newPage) {
      this.currentPage = newPage;
    },
    getData() {
      axios
          .get("http://seqnqc.natappfree.cc/api/publishes/") // 使用 axios 发送 GET 请求
          .then((response) => {
            this.data = response.data; // 使用返回的数据更新 this.data
          })
          .catch((error) => {
            console.error(error);
          });
    },
    showDeleteConfirm(bookId) {
      const book = this.data.find((book) => book.id === bookId);
      if (!book) {
        return;
      }

      this.$confirm(`确定删除书籍 ${book.book_name} 吗？`, "确认删除", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning",
      })
          .then(() => {
            this.deleteBook(bookId);
          })
          .catch(() => {
            // 用户点击取消按钮时的回调
          });
    },

    deleteBook(bookId) {
      const bookIndex = this.data.findIndex((book) => book.id === bookId);
      if (bookIndex > -1) {
        this.data.splice(bookIndex, 1); // 删除找到的书籍
      }
    },
    submitEdit(book) {
      book.editPopoverVisible = false;
      axios
          .put(`http://seqnqc.natappfree.cc/api/publishes/${book.id}/`, this.editingBook)
          .then((response) => {
            const index = this.data.findIndex((b) => b.id === book.id);
            if (index !== -1) {
              this.data[index] = {...this.editingBook};
              Object.assign(this.data[index], this.editingBook);
            }
            this.editingBook = {
              Publishing_house: "",
              author: "",
              Price: "",
              mobile: "",
              status: "",
            };
          })
          .catch((error) => {
            console.error(error);
          });
    },
    cancelEdit(book) {
      book.editPopoverVisible = false;
      this.editingBook = {
        Publishing_house: "",
        author: "",
        Price: "",
        mobile: "",
        status: "",
      };
    },
    editBook(book) {
      this.editingBook = {...book};
      book.editPopoverVisible = false;
      book.editPopoverVisible = true;
    },
  },
};
</script>


<style>
.card-container {
  width: 300px;
  margin: 30px;
}

.time {
  font-size: 13px;
  color: #999;
}

.bottom {
  margin-top: 13px;
  line-height: 12px;
}

.button {
  padding: 0;
  float: right;
}

.image {
  width: 100%;
  display: block;
}

.clearfix:before,
.clearfix:after {
  display: table;
  content: "";
}

.clearfix:after {
  clear: both
}

.pagination-container {
  display: flex;
  justify-content: center;
  margin-top: 20px; /* Adjust the margin as needed */
}

.search-container {
  display: flex;
  justify-content: center; /* 水平居中对齐 */
  align-items: center; /* 垂直居中对齐 */
  margin-bottom: 10px;
}

body {
  margin: 0;
  padding: 0;
}
.adjust-button-position {
    position: relative;
    left: -190px; /* 调整这个值以达到您希望的效果 */
}
</style>