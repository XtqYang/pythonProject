<template>
  <el-container>
    <el-header>
      <h1>首页</h1>

    </el-header>
    <el-main>
      <!-- 路由跳转 -->
      <router-view/>
    </el-main>
    <el-footer>Footer</el-footer>
  </el-container>
</template>

<style scoped>
.el-container {
  height: 100%;
}

.el-header,
.el-footer {
  background-color: #b3c0d1;
  color: var(--el-text-color-primary);
  text-align: center;
  line-height: 60px;
}

.el-footer {
  line-height: 60px;
}

.el-main {
  background-color: #e9eef3;
  color: var(--el-text-color-primary);
  text-align: center;
  line-height: 160px;
}
</style>
