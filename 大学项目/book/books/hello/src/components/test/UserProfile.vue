<template>
  <p>这是头像</p>
  <span>store的count属性：{{ count }}--{{ name }}</span>
  <button @click="plus">按钮</button>
  <hr>
  <span>查看今天完成多少日程：{{ doneCount }}</span>
</template>

<script>
import {mapState, mapGetters, mapActions} from 'vuex'
// import {increment} from '@/store/mutation-types'

export default {
  name: 'App',
  data() {
    return {
      age: 22,
      num: 10,
    };
  },
  components: {},
  methods: {
    ...mapActions(['increment']),
    plus() {
      //对共享变量的一个操作逻辑
      // this.$store.commit({type: increment, n: 10});
      this.$store.dispatch('increment');

    },
  },
  //计算属性,参数传递
  computed: {
    ...mapGetters(['doneCount']),
    ...mapState(['count', 'name']),
    myNum() {
      return this.num + 10
    },
  }
};
</script>
