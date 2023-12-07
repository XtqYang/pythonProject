<template>
  <p>这是 user的 {{ $route.params.id }}</p>
  <router-link v-bind:to="'/user/'+$route.params.id+'/profile'">头像</router-link>
  <router-link v-bind:to="'/user/'+$route.params.id+'/pots'">背景</router-link>
  <router-view></router-view>
</template>

<script>
export default {
  name: "App",
  components: {},
  mounted() {
    console.log(this.$route.params.id)
  }
};
</script>
