// 创建一个新的 store 实例
import {createStore} from "vuex";
import moduleA from "@/store/models/moduleA";
import moduleB from "@/store/models/moduleB";
import actions from "@/store/actions";
import mutations from "@/store/mutations";
// import {increment} from './mutation-types'
const store = createStore({
    modules: {
        a: moduleA,
        b: moduleB
    },
    actions,
    mutations,
})

export default store
// const store = createStore({
//     //  state相当于data，只不过他是全局的，所有的组件都能访问
//     state() {
//         return {
//             count: 1,
//             name: 'tom',
//             num: 2,
//             todos: [
//                 {id: 1, text: '吃饭', done: true},
//                 {id: 2, text: '睡觉', done: false}
//             ]
//         }
//     },
//     //和计算属性很像
//     getters: {
//         doneCount(state) {
//             return state.todos.filter(todo => todo.done == true).length
//         },
//     },
//     //保存了对共享数据的修改逻辑
//     mutations: {
//         [increment](state, payload) {
//             state.count += payload.n
//             // setTimeout(() => {
//             //     state.const += payload.n
//             // }, 2000)
//         }
//     },
//     actions: {
//         increment({commit}) {
//             commit('increment', {n: 50})
//             setTimeout(() => {
//                 commit('increment', {n: 50})
//             }, 2000)
//         }
//     },
// })

// main.js
// import {createApp} from 'vue'
// import App from '@/App.vue'
// import router from '@/router/index'
// import store from '@/store'
// import ElementPlus from 'element-plus'
// import 'element-plus/dist/index.css'
//
// //app根组件(全局)
// let app = createApp(App).use(router).use(store).use(ElementPlus)
// // createApp(app).mount('#app')
// app.mount('#app')
