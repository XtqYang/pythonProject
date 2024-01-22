import {createApp} from 'vue'
import App from './App.vue'
import router from './router/index'
import {createStore} from 'vuex'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import '@/css/common.css'
// 创建一个新的 store 实例
const store = createStore({
    state() {
        return {}
    },
    mutations: {},
})
// 创建一个 Vue 实例
const app = createApp(App)

// 使用插件
app.use(router)
app.use(store)
app.use(ElementPlus)

// 挂载 Vue 实例到 DOM 元素
app.mount('#app')

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