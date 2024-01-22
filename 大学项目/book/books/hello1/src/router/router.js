import Vue from 'vue'
import VueRouter from 'vue-router'
import Main from '@/components/main/IndexMain'

Vue.use(VueRouter)

const routes = [
  {
    path: '/main',
    component: Main
  }
]

const router = new VueRouter({
  routes
})

export default router
