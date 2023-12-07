<template>

  <div class="emoji-wrapper">

    <div>
      <div class="button-container">
        <el-button @click="showDialog">新增</el-button>

        <el-dialog v-model="dialogVisible" :width="dialogWidth" @close="resetForm">

          <el-form :model="form" label-width="80px">
            <el-form-item label="用户名">
              <el-input v-model="form.username" size="small" style="height: 30px;"></el-input>
            </el-form-item>
            <el-form-item label="密码">
              <el-input v-model="form.password" type="password" size="small" style="height: 30px;"></el-input>
            </el-form-item>
            <el-form-item label="确认密码">
              <el-input v-model="form.confirmPassword" type="password" size="small" style="height: 30px;"></el-input>
            </el-form-item>
          </el-form>

          <template v-slot:footer>
            <span class="dialog-footer">
              <el-button @click="dialogVisible = false">取消</el-button>
              <el-button type="primary" @click="submitForm">提交</el-button>
            </span>
          </template>

        </el-dialog>

      </div>
    </div>


    <el-table :data="users" style="width: 100%">
      <el-table-column label="ID" width="180">
        <template v-slot="scope">
          <i class="el-icon-time"></i>
          <span style="margin-left: 10px">{{ scope.row.id }}</span>
        </template>
      </el-table-column>
      <el-table-column label="用户" width="180">
        <template v-slot="scope">
          <el-popover trigger="hover" placement="top">
            <div>
              <p>用户: {{ scope.row.username }}</p>
              <p>密码: {{ scope.row.password }}</p>
            </div>
            <template v-slot:reference>
              <el-tag size="medium">{{ scope.row.username }}</el-tag>
            </template>
          </el-popover>
        </template>
      </el-table-column>
      <el-table-column label="密码" width="180">
        <template v-slot="scope">
          <i class="el-icon-time"></i>
          <span style="margin-left: 10px">{{ scope.row.password }}</span>
        </template>
      </el-table-column>
      <el-table-column label="操作">
        <template v-slot="scope">

          <el-popover
              placement="right-end"
              width="360"
              trigger="click"
              v-model:visible="scope.row.editPopoverVisible"
          >
            <el-form :model="editingUser" :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
              <el-form-item label="用户" prop="username">
                <el-input v-model="editingUser.username"></el-input>
              </el-form-item>
              <el-form-item label="密码" prop="password">
                <el-input type="text" v-model="editingUser.password" autocomplete="off"></el-input>
              </el-form-item>
              <!--            <el-form-item label="确认密码" prop="checkPass">-->
              <!--              <el-input type="password" v-model="editingUser.checkPass" autocomplete="off"></el-input>-->
              <!--            </el-form-item>-->
              <el-form-item>
                <el-button size="default" type="primary" @click="submitEdit(scope.row)">提交</el-button>
                <el-button size="default" @click="cancelEdit(scope.row)">取消</el-button>
              </el-form-item>
            </el-form>
            <template v-slot:reference>
              <el-button @click="editUser(scope.row)">编辑</el-button>
            </template>
          </el-popover>

          <el-popover
              placement="top-start"
              width="160"
              trigger="click"
              v-model:visible="scope.row.deletePopoverVisible"
          >
            <p>确定删除吗？</p>
            <div style="text-align: right; margin: 0">
              <el-button size="default" @click="scope.row.deletePopoverVisible = false">取消</el-button>
              <el-button type="primary" size="default" @click="deleteUser(scope.row.id)">确定</el-button>
            </div>
            <template v-slot:reference>
              <el-button @click="scope.row.deletePopoverVisible = false" type="danger" size="default">删除</el-button>
            </template>
          </el-popover>

        </template>
      </el-table-column>
    </el-table>

  </div>

</template>
<script>
import axios from "axios";

export default {
  data() {
    return {
      dialogVisible: false,
      dialogWidth: '400px', // 设置弹窗宽度
      form: {
        username: '',
        password: '',
        confirmPassword: '' // 添加确认密码字段
      },
      editingUser: {
        username: '',
        password: '',
        checkPass: '',
      },
      rules: {
        confirmPassword: [
          {required: true, message: "请再次输入密码", trigger: "blur"},
          {
            validator: (rule, value, callback) => {
              if (value !== this.form.password) {
                callback(new Error("两次输入密码不一致"));
              } else {
                callback();
              }
            },
            trigger: "blur",
          },
        ],
      },
      users: [],
    };
  },
  mounted() {
    this.loadUsers();
  },
  methods: {
    loadUsers() {
      axios
          .get("http://seqnqc.natappfree.cc/api/user/")
          .then((response) => {
            this.users = response.data;
          })
          .catch((error) => {
            console.error(error);
          });
    },
    showDialog() {
      this.dialogVisible = true;
    },
    //新增
    submitForm() {
      if (this.form.password !== this.form.confirmPassword) {
        alert('密码和确认密码不匹配');
        return;
      }
      // 构造要发送到服务器的数据
      const newUser = {
        username: this.form.username,
        password: this.form.password,
      };

      // 向服务器发送 POST 请求来添加新用户
      axios
          .post("http://seqnqc.natappfree.cc/api/user/", newUser)
          .then((response) => {
            // 添加成功后，刷新用户列表
            this.loadUsers();

            // 重置表单
            this.dialogVisible = false;
            this.resetForm();
          })
          .catch((error) => {
            console.error(error);
            // 在实际应用中，你可能会根据服务器返回的错误信息进行适当的处理
          });
      this.dialogVisible = false;
      this.resetForm();
    },
    resetForm() {
      this.form.username = '';
      this.form.password = '';
      this.form.confirmPassword = ''; // 重置确认密码字段
    },
    deleteUser(id) {
      axios
          .delete(`http://seqnqc.natappfree.cc/api/user/${id}`)
          .then((response) => {
            this.users = this.users.filter((user) => user.id !== id);
          })
          .catch((error) => {
            console.error(error);
          });
    },
    editUser(user) {
      this.editingUser = {...user};
      user.editPopoverVisible = false;
    },
    submitEdit(user) {
      user.editPopoverVisible = false;
      axios
          .put(`http://seqnqc.natappfree.cc/api/user/${user.id}/`, this.editingUser)
          .then((response) => {
            const index = this.users.findIndex(u => u.id === user.id);
            if (index !== -1) {
              this.users[index] = {...this.editingUser};
            }
            user.editPopoverVisible = false;
            this.editingUser = {};
          })
          .catch((error) => {
            console.error(error);
          });
    },
    cancelEdit(user) {
      user.editPopoverVisible = false;
      this.editingUser = {};
    },
  },
};
</script>
<style>
.emoji-wrapper {
  padding: 50px;
}

.add-user-button {
  padding: 50px;

  position: absolute;
  top: 0;
  left: 0;
  margin: 10px;
}

.dialog-footer {
  display: flex;
  justify-content: center;
  padding: 10px 0;
  border-top: 1px solid #ebeef5;
}

.button-container {
  display: flex;
  justify-content: flex-start;
  margin-bottom: 10px;
}

</style>