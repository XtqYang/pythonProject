<template>
  <div class="wrapper">

    <el-descriptions class="margin-top description-container" title="带边框列表" :column="3" :size="size" border>
      <template v-slot:extra>
        <el-button type="primary" size="small">操作</el-button>
      </template>
      <el-descriptions-item>
        <template v-slot:label>
          <i class="el-icon-user"></i>
          用户名
        </template>
        {{ username }}
      </el-descriptions-item>
      <el-descriptions-item>
        <template v-slot:label>
          <i class="el-icon-mobile-phone"></i>
          手机号
        </template>
        18100000000
      </el-descriptions-item>
      <el-descriptions-item>
        <template v-slot:label>
          <i class="el-icon-location-outline"></i>
          居住地
        </template>
        成都市
      </el-descriptions-item>
      <el-descriptions-item>
        <template v-slot:label>
          <i class="el-icon-tickets"></i>
          备注
        </template>
        <el-tag size="small">成都东软学院</el-tag>
      </el-descriptions-item>
      <el-descriptions-item>
        <template v-slot:label>
          <i class="el-icon-office-building"></i>
          联系地址
        </template>
        四川成都
      </el-descriptions-item>
    </el-descriptions>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: localStorage.getItem('username') || '未登录'
    };
  },
  watch: {
    '$route': function() {
      this.username = localStorage.getItem('username') || '未登录';
    }
  }
}
</script>
<style>
.wrapper {
  width: 80%;  /* 缩小页面宽度 */
  margin: 50px auto 0;  /* 整体向下移动，并居中对齐 */
}

.margin-top {
  margin-top: 20px;
}

.description-container {
  width: 100%; /* 设置描述列表的宽度 */
}
</style>