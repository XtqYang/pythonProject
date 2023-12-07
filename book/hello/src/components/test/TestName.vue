<template>

  <div style="height: 100vh; display: flex; align-items: center; justify-content: center; margin-top: -200px">
    <el-table
        ref="multipleTable"
        :data="tableData"
        tooltip-effect="dark"
        style="width: 60%"
        height="300"
        @selection-change="handleSelectionChange">
      <el-table-column
          type="selection"
          width="150"
          fixed="left">
      </el-table-column>
      <el-table-column
          prop="book_name"
          label="书名"
          width="180"
          align="center">
      </el-table-column>
      <el-table-column
          prop="mobile"
          label="编号"
          width="150"
          align="center">
      </el-table-column>
      <el-table-column
          prop="author"
          label="作者"
          width="150"
          align="center">
      </el-table-column>
      <el-table-column
          prop="Price"
          label="价格"
          width="150"
          align="center">
      </el-table-column>
      <el-table-column
          label="操作"
          width="150"
          align="center"
          fixed="right">
        <template v-slot:default="scope">
          <el-button
              @click.prevent="deleteRow(scope.$index, tableData)"
              type="text"
              size="small">
            移除
          </el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
  <div style="margin-top: -580px;margin-left: -740px; text-align: center;">
    <el-button @click="toggleSelection(tableData)">全选</el-button>
    <el-button @click="toggleSelection()">取消选择</el-button>
  </div>
  <div style="margin-top: 400px;margin-left: 10px; text-align: center;">
    <el-button @click="submitData">提交</el-button>
  </div>

</template>

<script>
import axios from 'axios'; // 首先确保已经安装了axios，并导入它
import {getCookie, setCookie} from '@/components/utils/utils.js'

export default {
  data() {
    return {
      tableData: [],
      multipleSelection: []
    }
  },
  created() {
    this.tableData = JSON.parse(getCookie('cartItems') || '[]');
  },
  methods: {
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
    async submitData() {
      try {
        // 将数据转换为后台所需格式
        const formattedData = this.multipleSelection.map(item => ({
          date: "", // 从item中获取适当的值，如果有的话
          name: item.author,
          BookName: item.book_name,
          mobile: item.mobile,
          give: null
        }));

        // 发送数据
        await axios.post('/api/lending/', formattedData);

        // 如果成功，从tableData中移除已提交的数据
        this.tableData = this.tableData.filter(item => !this.multipleSelection.includes(item));
        this.multipleSelection = []; // 清空已选择的数据
      } catch (error) {
        console.error("提交数据时出错:", error);
        // 这里可以添加错误处理逻辑，例如显示一个通知或警告
      }
    }
  }
}
</script>