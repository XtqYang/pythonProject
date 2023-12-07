<template>
  <el-table
      :data="tableData"
      border
      style="width:70%">
    <el-table-column
        prop="date"
        label="借阅日期"
        width="180">
    </el-table-column>
    <el-table-column
        prop="username"
        label="用户名"
        width="180">
    </el-table-column>
    <el-table-column
        prop="BookName"
        label="书籍名称">
    </el-table-column>
    <el-table-column
        prop="author"
        label="作者"
        width="180">
    </el-table-column>
    <el-table-column
        prop="mobile"
        label="编号">
    </el-table-column>
    <el-table-column label="是否归还">
      <template v-slot="{ row }">
        <el-button v-if="row.give === 1" type="warning">未归还</el-button>
        <el-button v-else type="success">已归还</el-button>
      </template>
    </el-table-column>

  </el-table>
</template>

<script>
import axios from 'axios'; // 首先，确保您已经安装了axios并导入它。

export default {
  data() {
    return {
      currentUserName: '',// 新增属性来保存当前用户名
      tableData: [] // 初始化表格数据为空数组
    }
  },
  created() {
    this.currentUserName = localStorage.getItem('username'); // 从localStorage获取当前用户名
    this.fetchLendingData();
  },
  methods: {
    async fetchLendingData() {
      try {
        const response = await axios.get('/api/lending/');
        // 过滤数据，只保留与当前用户名相匹配的数据
        this.tableData = response.data.filter(item => item.username === this.currentUserName);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    }
  }
}
</script>
