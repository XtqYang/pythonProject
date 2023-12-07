<template>
  <el-row :gutter="20">
    <el-col :span="6">
      <div class="grid-content ep-bg-purple"/>
    </el-col>
    <el-col :span="12">
      <h1>后台登录</h1>
      <el-form :model="user" label-width="120px">
        <el-form-item label="用户名">
          <el-input v-model="user.username"/>
        </el-form-item>
        <el-form-item label="密码">
          <el-input v-model="user.password" type="password"/>
        </el-form-item>
        <el-form-item label="图片验证码" prop="captcha">
          <el-input v-model="user.captcha" placeholder="请输入验证码"></el-input>
          <img class="captcha-image" :src="captchaImageUrl" alt="验证码" @click="refreshCaptcha">
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="submitForm">登录</el-button>
        </el-form-item>

      </el-form>
      <p v-if="error" class="error-message">{{ error }}</p>
    </el-col>
    <el-col :span="6">
      <div class="grid-content ep-bg-purple"/>
    </el-col>
  </el-row>
</template>
<script>
import axios from "axios";

export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "Login",
  data() {
    return {
      user: {
        username: "",
        password: "",
        captcha: "", // 修改此处的属性名为 captcha
      },
      captchaImageUrl: "/api/image/code/", // 初始化验证码图片地址
      error: "",
    };
  },
  methods: {
    goToRegistration() {
      this.$router.push('/user/SignIn'); // 导航到目标页面
    },
    refreshCaptcha() {
      // 在点击图片验证码时重新获取验证码图片的URL
      this.captchaImageUrl = "/api/image/code/?" + new Date().getTime(); // 添加时间戳以避免缓存
    },
submitForm() {
  axios
      .post('/api/background/login/', {
        username: this.user.username,
        password: this.user.password,
        captcha: this.user.captcha, // 修改此处的属性名为 user.captcha
      })
      .then((response) => {
        const data = response.data;
        if (data.success) {
          // Save the username and role to localStorage
          localStorage.setItem('username', this.user.username);
          localStorage.setItem('role', data.characters); // Save role to localStorage

          alert(data.msg);
          this.$router.push('/user/list');
        } else {
          alert(data.msg);
          this.error = data.message;
        }
      })
      .catch((error) => {
        console.error(error);
        this.error = "网络请求失败，请稍后重试。";
      });
},

  },
};
</script>

<style>
.login-form {
  position: relative;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

.error-message {
  color: red;
}
</style>
