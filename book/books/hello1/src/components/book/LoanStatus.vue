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
        <el-button v-if="row.give === 1" type="warning" @click="toggleGiveStatus(row)">未归还</el-button>
        <el-button v-else type="success" @click="toggleGiveStatus(row)">已归还</el-button>
      </template>
    </el-table-column>
  </el-table>
</template>

<script>
import axios from 'axios'; // 首先，确保您已经安装了axios并导入它。

export default {
  data() {
    return {
      tableData: [] // 初始化表格数据为空数组
    }
  },
  created() {
    this.fetchLendingData(); // 在组件创建时发起API请求
  },
  methods: {
    async toggleGiveStatus(row) {
      try {
        // 切换give字段的状态
        row.give = row.give === 1 ? 0 : 1;

        // 准备需要发送到后端的数据
        const payload = {...row};

        // 使用axios发起PUT请求来更新后端数据
        await axios.put(`/api/lending/${row.id}/`, payload);

        // 前端数据已经在上面更新了，所以不需要额外操作
      } catch (error) {
        console.error('Error updating the give status:', error);
        this.$message.error('更新归还状态失败');
      }
    },
    async fetchLendingData() {
      try {
        const response = await axios.get('/api/lending/'); // 使用axios发起GET请求
        this.tableData = response.data; // 假设响应数据直接是一个数组，您可以将其赋值给tableData
      } catch (error) {
        console.error('Error fetching data:', error); // 错误处理
      }
    }
  }
}
</script>
