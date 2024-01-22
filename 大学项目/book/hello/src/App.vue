<template>
  <div id="app">
    <div class="header">
      <div class="dropdown-container">
        <el-dropdown v-if="username !== '未登录'">
          <span class="el-dropdown-link">
            <i class="user-icon"></i> {{ username }}<i class="el-icon-arrow-down el-icon--right"></i>
          </span>
          <template v-slot:dropdown>
            <el-dropdown-menu>
              <el-dropdown-item>
                <router-link to="/user/PersonalInformation" class="unstyled-link">个人信息</router-link>
              </el-dropdown-item>
              <el-dropdown-item>当前角色: {{ role }}</el-dropdown-item>
              <el-dropdown-item @click="logout">退出</el-dropdown-item>
            </el-dropdown-menu>
          </template>
        </el-dropdown>
        <button v-else class="plain-button" title="登录" @click="goToLogin">登录</button>
      </div>
    </div>
    <router-view/>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: localStorage.getItem('username') || '未登录',
      role: localStorage.getItem('role') || '未知角色'
    };
  },
  watch: {
    '$route': function () {
      this.username = localStorage.getItem('username') || '未登录';
      this.role = localStorage.getItem('role') || '未知角色';
    }
  },
  methods: {
    goToLogin() {
      this.$router.push({name: 'userlogin'});
    },
    logout() {
      // 清除localStorage中的用户信息
      localStorage.removeItem('username');
      localStorage.removeItem('role');

      // 重新获取username和role，此时应为'未登录'和'未知角色'
      this.username = localStorage.getItem('username') || '未登录';
      this.role = localStorage.getItem('role') || '未知角色';

      // 重定向到登录页面或首页（根据你的路由设置）
      this.$router.push({name: 'userlogin'});
    }
  }

}

const debounce = (fn, delay) => {
  let timer = null;
  return function () {
    let context = this;
    let args = arguments;
    clearTimeout(timer);
    timer = setTimeout(function () {
      fn.apply(context, args);
    }, delay);
  }
}

const _ResizeObserver = window.ResizeObserver;
window.ResizeObserver = class ResizeObserver extends _ResizeObserver {
  constructor(callback) {
    callback = debounce(callback, 16);
    super(callback);
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

.header {
  width: 100%;
  text-align: right;
  background-color: #f1f1f1;
  padding: 10px;
}

.dropdown-container {
  margin-right: 100px; /* 添加右边距来向左移动下拉菜单 */
}

.el-dropdown-link {
  /*outline: none;*/
  cursor: pointer;
  color: #808080;
  font-size: 16px; /* 这里是增加的字体大小，可以根据需要调整 */
}

.el-icon-arrow-down {
  font-size: 12px;
}

.user-icon::before {
  content: ""; /* 添加一个内容属性，这里将显示图片 */
  display: inline-block;
  width: 30px; /* 图片的宽度 */
  height: 30px; /* 图片的高度 */
  background-image: url('tushu.jpg'); /* 替换成你的圆形图片的 URL */
  background-size: cover; /* 调整图片尺寸以适应元素大小 */
  border-radius: 50%; /* 创建圆形效果 */
  margin-right: 5px; /* 调整图标与文本之间的间距 */
  vertical-align: middle; /* 垂直对齐方式 */
}

/* 定义无样式链接的样式 */
.unstyled-link {
  text-decoration: none; /* 去除下划线 */
  color: inherit; /* 继承父元素的文本颜色 */
  background: none; /* 去除背景 */
  border: none; /* 去除边框 */
  cursor: pointer; /* 鼠标指针为指针形状 */
}

.plain-button {
  /*position: absolute;*/
  top: 0;
  right: 0;
  border: none;
  background: none;
  color: inherit;
  font: inherit;
  cursor: pointer;
}

</style>
