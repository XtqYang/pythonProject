<template>
  <el-container>
    <el-menu
        class="el-menu-demo"
        mode="horizontal"
        background-color="#f5f7fa"
        text-color="#fff"
        active-text-color="#ffd04b"
    >
      <el-menu-item index="1-1" @click="open('UserList')">用户管理</el-menu-item>
      <el-menu-item index="1-2" @click="open('AdminList')">管理员管理</el-menu-item>
      <el-menu-item index="1-3" @click="open('AdminBook')">图书管理</el-menu-item>
      <el-menu-item index="1-4" @click="open('LoanStatus')">学生借阅情况</el-menu-item>
    </el-menu>
    <el-main>
      <!-- 路由跳转 -->
      <router-view/>
    </el-main>
    <el-footer></el-footer>
  </el-container>
</template>

<script setup>
import {useRouter} from 'vue-router';

// 路由跳转，获取路由信息
const router = useRouter();
let open = (name) => {
  // 路由跳转，在组合式的 API 中不能使用 this
  router.push({name});
};
</script>

<style scoped>
.el-container {
  margin-top: 0; /* 清除顶部外边距 */
  display: flex;
  flex-direction: column; /* 将子元素纵向排列 */
}

.el-main {
  flex: 1; /* 占据剩余的空间 */
  background-color: #ffffff;
  color: var(--el-text-color-primary);
  text-align: center;
  line-height: 160px;
}

.el-footer {
  background-color: #ffffff;
  color: var(--el-text-color-primary);
  text-align: center;
  line-height: 60px;
}

.el-menu-demo {
  display: flex;
  justify-content: center;
}

.el-menu-item {
  color: #726e6e;
}

</style>
