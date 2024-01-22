<template>
  <div id="app">
    <div class="login-container">
      <h2 class="login-title">用户登录</h2>
      <el-form :model="form" ref="loginForm" @submit.prevent="submitForm" class="login-form">
        <el-form-item label="&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp用户名" prop="username">
          <el-input v-model="form.username" placeholder="请输入用户名"></el-input>
        </el-form-item>
        <el-form-item label="&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp密码" prop="password">
          <el-input v-model="form.password" type="password" placeholder="请输入密码"></el-input>
        </el-form-item>
        <el-form-item label="图片验证码" prop="captcha">
          <el-input v-model="form.captcha" placeholder="请输入验证码"></el-input>
          <img class="captcha-image" :src="captchaImageUrl" alt="验证码" @click="refreshCaptcha">
        </el-form-item>
        <el-form-item>
          <el-button type="primary" class="login-button" @click="submitForm">登录</el-button>
          <el-button type="primary" class="login-button" @click="goToRegistration">注册</el-button>
        </el-form-item>
      </el-form>
      <div v-if="error" class="error-message">{{ error }}</div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Login",
  data() {
    return {
      form: {
        username: "",
        password: "",
        captcha: "",
      },
      captchaImageUrl: "http://seqnqc.natappfree.cc/api/image/code/",
      error: "",
    };
  },

  methods: {
    goToRegistration() {
      this.$router.push('/user/SignIn');
    },

    refreshCaptcha() {
      this.captchaImageUrl = "http://seqnqc.natappfree.cc/api/image/code/?" + new Date().getTime();
    },
    handleSuccess(response) {
      localStorage.setItem('token', response.data.token);
      localStorage.setItem('username', this.form.username);
      localStorage.setItem('role', response.data.characters); // 保存角色到 localStorage

      if (response.data.success) {
        this.$message.success(response.data.msg);
        this.$router.push('/book/IndexBook/');
      } else {
        this.handleError(response.data);
      }
    },

    handleError(data) {
      this.$message.error(data.msg);
      this.error = data.message;

      if (data.msg.includes('验证码')) {
        this.refreshCaptcha();
      }
    },

    submitForm() {
      this.$refs.loginForm.validate((valid) => {
        if (valid) {
          axios.post('http://seqnqc.natappfree.cc/api/foreground/login/', this.form)
              .then(this.handleSuccess)
              .catch((error) => {
                console.error(error);
                this.error = "网络请求失败，请稍后重试。";
              });
        }
      });
    },
  },
};
</script>

<style scoped>
.login-container {
  max-width: 400px;
  margin: 0 auto;
  padding: 50px;
  border: 1px solid #ccc;
  border-radius: 5px;
  box-shadow: 5px 5px 20px #aaa;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.login-title {
  text-align: center;
}

.login-form {
  margin-top: 20px;
}

.login-button {
  width: 20%;
  padding: 8px;
  font-size: 14px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  margin: 0 auto;
}

.error-message {
  color: red;
  margin-top: 10px;
}

.captcha-image {
  cursor: pointer;
}
</style>
