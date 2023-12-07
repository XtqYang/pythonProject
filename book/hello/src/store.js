// store.js
import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    cart: []  // 用于保存购物车中的书籍
  },
  mutations: {
    addToCart(state, book) {
      state.cart.push(book);
    },
    removeFromCart(state, bookId) {
      const index = state.cart.findIndex(b => b.id === bookId);
      if (index !== -1) {
        state.cart.splice(index, 1);
      }
    }
  },
  actions: {
    // 异步操作可以放在这里
  },
  getters: {
    // 如果需要，可以添加计算属性
  }
});
