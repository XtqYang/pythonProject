<template>
  <el-container>
    <el-menu
        class="el-menu-demo"
        mode="horizontal"
        background-color="#f5f7fa"
        text-color="#4d70ff"
        active-text-color="#4d70ff"
    >
      <el-menu-item index="1-3" @click="open('IndexBook')">阅读图书</el-menu-item>
      <el-menu-item index="1-4" @click="open('ShoppingHome')">购物车</el-menu-item>
      <el-menu-item index="1-5" @click="open('UserLending')">我的借阅情况</el-menu-item>
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
  height: auto;
}

.el-footer {
  background-color: #ffffff;
  color: var(--el-text-color-primary);
  text-align: center;
  line-height: 60px;
}

.el-main {
  background-color: #ffffff;
  color: var(--el-text-color-primary);
  text-align: center;
  line-height: 160px;
}

.el-menu-demo {
  display: flex;
  justify-content: center;
}

.el-menu-item {
  color: #726e6e;
}
.el-main {
  background-color: #ffffff;
  color: var(--el-text-color-primary);
  text-align: center;
  line-height: 160px;
  overflow-y: scroll; /* 确保内容超出时会出现滚动条 */
}

/* 为Webkit内核的浏览器 (如Chrome和Safari) 设计滚动条 */
.el-main::-webkit-scrollbar {
    width: 8px;
}

.el-main::-webkit-scrollbar-track {
    background: #f1f1f1;
}

.el-main::-webkit-scrollbar-thumb {
    background: #4d70ff; /* 滚动条颜色 */
}

.el-main::-webkit-scrollbar-thumb:hover {
    background: #555;
}

/* 针对IE和Edge */
.el-main {
    -ms-overflow-style: auto;
}

/* 针对Firefox */
.el-main {
    scrollbar-width: thin;
    scrollbar-color: #4d70ff #f1f1f1;
}

</style>
