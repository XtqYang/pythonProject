<template>
  <div class="table-wrapper">
    <el-table
        ref="multipleTable"
        :data="tableData"
        tooltip-effect="dark"
        style="width: 80%"
        max-height="450"
        @selection-change="handleSelectionChange">

      <el-table-column
          type="selection"
          width="55">
      </el-table-column>

      <el-table-column
          prop="date"
          label="日期"
          width="200">
      </el-table-column>

      <el-table-column
          prop="book_name"
          label="书名"
          width="100">
      </el-table-column>
      <el-table-column
          prop="mobile"
          label="编号"
          width="100">
      </el-table-column>
      <el-table-column
          prop="author"
          label="作者"
          width="100">
      </el-table-column>
      <el-table-column
          prop="Price"
          label="价格"
          width="100">
      </el-table-column>

      <el-table-column
          label="操作"
          width="600">
        <template v-slot:default="scope">
          <el-button
              @click.prevent="deleteRow(scope.$index, tableData)"
              type="text"
              size="small"
              width="100"
          >
            移除
          </el-button>
        </template>
      </el-table-column>
    </el-table>

  </div>
  <!--  margin-top: -580px;margin-left: -740px;-->
  <div style="" class="buttons-group">
    <el-button @click="toggleSelection(tableData)">全选</el-button>
    <el-button @click="toggleSelection()">取消选择</el-button>
  </div>


  <el-popover
      placement="top"
      width="160"
      trigger="click"
      v-model:visible="dialogVisible"
  >
    <p>确定提交吗？</p>
    <div style="text-align: right; margin: 0">
      <el-button size="default" @click="dialogVisible = false">取消</el-button>
      <el-button type="primary" size="default" @click="submitData">确定</el-button>
    </div>
    <template v-slot:reference>
      <div class="submit-button-group">
        <el-button @click="showDialog" type="primary" size="default">提交</el-button>
      </div>
    </template>
  </el-popover>


</template>


<script>
import axios from 'axios'; // 首先确保已经安装了axios，并导入它
import {getCookie, setCookie} from '@/components/utils/utils.js'

export default {
  data() {
    return {
      currentUserName: '',  // 这里可以初始化为空字符串，或者您可以获取当前用户的名称
      dialogVisible: false,
      dialogWidth: '400px', // 设置弹窗宽度
      tableData: [],
      multipleSelection: []
    }
  },
  created() {
    this.tableData = JSON.parse(getCookie('cartItems') || '[]');
  },
  methods: {
    showDialog() {
      this.dialogVisible = false;
    },
    deleteRow(index, rows) {
      rows.splice(index, 1);
      setCookie('cartItems', JSON.stringify(rows), 7);
    },
    toggleSelection(rows) {
      if (rows && rows.length) {
        rows.forEach(row => {
          this.$refs.multipleTable.toggleRowSelection(row, true);
        });
      } else {
        this.$refs.multipleTable.clearSelection();
      }
    },
    handleSelectionChange(val) {
      this.multipleSelection = val;
    },
    // 新增方法：提交数据到API
    async submitData() {
      try {
        // 从 Vuex 存储中获取用户名称
        const name = localStorage.getItem('username');

        // 遍历所选行并格式化数据
        const formattedData = this.multipleSelection.map(item => ({
          date: item.date,
          username: name,
          author: item.author,
          BookName: item.book_name,
          mobile: item.mobile,
          give: 1
        }));
        // 对每个已选行进行POST请求到API
        for (let data of formattedData) {
          await axios.post('/api/lending/', data);
        }

        // 成功后，从tableData中移除所选的数据
        this.tableData = this.tableData.filter(row => !this.multipleSelection.includes(row));
        // 更新cookie中的数据
        setCookie('cartItems', JSON.stringify(this.tableData), 7);


        // 重置选择，关闭确认对话框，并显示成功消息
        this.$refs.multipleTable.clearSelection();
        this.dialogVisible = false;
        this.$message.success('数据成功提交!');

      } catch (error) {
        // 出错时，显示错误消息
        // this.$message.error('数据提交失败: ' + (error.message || '未知错误'));
        this.$message.error('请登录后再提交');
      }
    }
  }
}
</script>

<style scoped>
.table-wrapper {
  margin-left: 10vw;
  margin-top: 0px;
}


/* 调整行的高度 */
.el-table .el-table__row {
  height: 30px; /* 你可以根据需要调整这个值 */
  line-height: 30px; /* 确保这与上面的高度相同 */
}


.dialog-footer {
  display: flex;
  justify-content: center;
  padding: 10px 0;
  border-top: 1px solid #ebeef5;
}
.buttons-group {
  text-align: center;
  margin-top: 1vw;
  margin-left: 5vw;
}
.submit-button-group {
  text-align: center;
  margin-top: -160px; /* Adjust this value as needed to move the button up */
  margin-left: 300px;
}
</style>
