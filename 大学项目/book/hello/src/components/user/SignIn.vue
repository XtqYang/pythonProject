<template>
  <div class="register-container">
    <h2 class="register-title">用户注册</h2>
    <el-form :model="form" :rules="rules" ref="registerForm" class="register-form">
      <el-form-item label="&nbsp&nbsp&nbsp用户名" prop="username" style="width: 350px;">

        <el-input v-model="form.username"></el-input>

        <span v-if="usernameTaken" class="error-message">用户名已被使用</span>
      </el-form-item>
      <br>
      <el-form-item label="&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp密码" prop="password" style="width: 350px;">

        <el-input type="password" v-model="form.password"></el-input>

      </el-form-item>
      <br>

      <el-form-item label="确认密码" prop="confirmPassword" style="width: 350px;">

        <el-input type="password" v-model="form.confirmPassword"></el-input>
      </el-form-item>
      <br>
      <el-form-item label="手机号&nbsp&nbsp&nbsp&nbsp&nbsp" prop="phoneNumber" style="width: 350px;">
        <el-input v-model="form.phoneNumber" placeholder="请输入手机号"></el-input>
      </el-form-item>
      <br>
      <br>

      <el-form-item label="验证码&nbsp&nbsp&nbsp&nbsp&nbsp" prop="verificationCode" style="width: 350px;">
        <el-button
            type="primary"
            class="send-code-button"
            @click="sendVerificationCode"
            :disabled="countdown > 0">
          {{ countdown > 0 ? `${countdown}秒后重发` : '发送验证码' }}
        </el-button>
        <el-input type="text" v-model="form.verificationCode" class="verification-input"></el-input>
        <span v-if="verificationCodeError" class="error-message">{{ verificationCodeError }}</span>
      </el-form-item>


      <el-form-item style="text-align: center;">
        <el-button type="primary" class="login-button" @click="submitForm">注册</el-button>
      </el-form-item>

    </el-form>
    <div v-if="error" class="error-message">{{ error }}</div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Register",
  data() {
    return {
      phoneNumber: [
        {required: true, message: '请输入手机号', trigger: 'blur'},
        {pattern: /^[1][3-9][0-9]{9}$/, message: '请输入有效的手机号', trigger: 'blur'}
      ],
      verificationCodeClicked: false,  // 新增的属性，用于跟踪用户是否点击了发送验证码按钮
      verificationCodeError: "",  // 新增的属性，用于显示验证码错误
      verificationCodeSent: false,
      countdown: 0,
      timer: null,
      isButtonDisabled: false,
      form: {
        phoneNumber: "",  // 新增的字段
        username: "",
        password: "",
        confirmPassword: "",
        verificationCode: "",
      },
      error: "",
      usernameTaken: false, // 新增的属性，用于标记用户名是否已被使用
      rules: {
        username: [
          {required: true, message: '请输入用户名', trigger: 'blur'},
          {min: 4, max: 20, message: '长度在 4 到 20 个字符', trigger: 'blur'}
        ],
        password: [
          {required: true, message: '请输入密码', trigger: 'blur'},
          {validator: this.validatePasswordComplexity, trigger: 'blur'}
        ],
        confirmPassword: [
          {required: true, message: '请确认密码', trigger: 'blur'},
          {validator: this.validateConfirmPassword, trigger: 'blur'}
        ]
      },

    };
  },
  methods: {
sendVerificationCode() {
  this.verificationCodeClicked = true;
  if (!this.form.phoneNumber) {
    this.verificationCodeError = "请输入手机号";
    return;
  }

  if (!/^[1][3-9][0-9]{9}$/.test(this.form.phoneNumber)) {
    this.verificationCodeError = "请输入有效的手机号";
    return;
  }

  // 发送验证码请求
  axios.post(`/api/message/code/${this.form.phoneNumber}/`)
      .then((response) => {
        this.verificationCodeSent = true;
        this.verificationCodeError = "";  // 清除验证码错误消息
        this.$refs.registerForm.clearValidate('phoneNumber');  // 清除手机号验证状态
        this.$refs.registerForm.clearValidate('verificationCode');  // 清除验证码验证状态

        // 开始倒计时
        if (this.countdown === 0) {
          this.countdown = 60;
          this.timer = setInterval(() => {
            if (this.countdown > 0) {
              this.countdown--;
            } else {
              clearInterval(this.timer);
              this.timer = null;
            }
          }, 1000);
        }
      })
      .catch((error) => {
        console.error(error);
        this.verificationCodeError = "验证码发送失败，请稍后再试";
      });
}
,
    validatePasswordComplexity(rule, value, callback) {
      const complexityRegex = /^(?=.*[a-z])(?=.*\d)[A-Za-z\d@$!%*?&]{8,}$/;
      if (!complexityRegex.test(value)) {
        callback(new Error('密码必须包含至少一个小写字母、一个数字，且长度至少为8个字符'));
      } else {
        callback();
      }
    },

    validateConfirmPassword(rule, value, callback) {
      if (value !== this.form.password) {
        callback(new Error("两次输入的密码不一致"));
      } else {
        callback();
      }
    },
    submitForm() {
      // 检查用户是否点击了发送验证码按钮
      if (!this.verificationCodeClicked) {
        this.verificationCodeError = "请获取验证码";
        return;
      }
      // 检查验证码输入框是否为空
      if (!this.form.verificationCode) {
        this.verificationCodeError = "请输入验证码";
        return;
      }
      this.$refs.registerForm.validate(valid => {
        if (valid && !this.usernameTaken) {
          axios.post('/api/user/', {
            username: this.form.username,
            password: this.form.password,
            confirmPassword: this.form.confirmPassword,
            verificationCode: this.form.verificationCode  // 添加此行
          })
              .then((response) => {
                const data = response.data;
                if (data.id) {
                  alert("注册成功");
                  this.$message.success("请登录");
                  this.$router.push('/user/login');
                }
              })
              .catch((error) => {
                // 如果后端返回了明确的错误信息
                if (error.response && error.response.data) {
                  const data = error.response.data;

                  // 判断是否返回了验证码错误
                  if (data.verificationCode) {
                    this.verificationCodeError = data.verificationCode[0];
                  } else {
                    this.$message.error(data.msg || "发生错误，请重试");
                  }

                } else {
                  // 如果没有明确的错误消息，显示默认错误
                  this.error = "发生错误，请重试";
                }
              });
        } else {
          return false;
        }
      });
    },
  },
};
</script>


<style scoped>

.register-container {
  max-width: 400px;
  margin: 0 auto;
  padding: 50px;
  border: 1px solid #ccc;
  border-radius: 5px;
  box-shadow: 5px 5px 20px #aaa;
}

.register-title {
  text-align: center;
}

.register-form {
  margin-top: 20px;
}

.error-message {
  color: red;
  margin-top: 10px;
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
  margin: 0 auto; /* 水平居中 */
}

.send-code-button {
  margin-left: 290px;
  position: relative;
  top: -4px;
  width: 80px; /* 设置按钮的宽度为100像素 */

}

.verification-input {
  position: relative;
  top: -35px;
}


</style>
