import {createRouter, createWebHistory} from 'vue-router';
// 预定义允许访问的路由列表
const allowedRoutes = ['/user/login', '/user/SignIn', '/user/yvedu', '/book/IndexBook',
    '/test/UserPots', '/test/name', '/user/PersonalInformation', '/test/pass2',
    "/Shopping/ShoppingHome"];  // 请根据您的实际需要更改


// 创建路由
const router = createRouter({
    history: createWebHistory(),
    routes: [
        //测试
        {
            path: '/test/name',
            name: 'TsetName',
            component: () => import('@/components/test/TestName'),
        }, {
            path: '/test/pass2',
            name: 'TsetPass2',
            component: () => import('@/components/test/TestPass2'),
        },
        //--------------------------前台---------------------------
        //用户登录页面
        {
            path: '/user/login',
            name: 'userlogin',
            component: () => import('@/components/user/Login'),
        },
        //注册页面
        {
            path: '/user/SignIn',
            name: 'SignIn',
            component: () => import('@/components/user/SignIn'),
        },
        //个人信息
        {
            path: '/user/PersonalInformation',
            name: 'Personal_Information',
            component: () => import('@/components/user/PersonalInformation'),
        },
        //前台首页
        {
            path: '/user/yvedu',
            name: 'yvedu',
            component: () => import('@/components/main/Index_Main'),
            children: [
                //图书展示
                {
                    path: '/book/IndexBook/',
                    name: 'IndexBook',
                    meta: {
                        showName: '我的首页',
                        requiresAuth: true, // 添加需要身份验证的标志
                    },
                    component: () => import('@/components/book/IndexBook'),
                },
                //购物车
                {
                    path: '/Shopping/ShoppingHome',
                    name: 'ShoppingHome',
                    component: () => import('@/components/Shopping/ShoppingHome'),
                },
                //用户个人借阅情况
                {
                    path: '/user/Lending',
                    name: 'UserLending',
                    component: () => import('@/components/user/UserLending'),
                },
            ],
        },
//-----------------------后台-------------------------------
//    后台登录页面
        {
            path: '/admin/Login',
            name: 'AdminLogin.vue',
            component: () => import('@/components/admin/AdminLogin'),
        },
        //后台首页
        {
            path: '/user/admin/yvedu',
            name: 'AdminYvedu',
            component: () => import('@/components/main/admin_Main'),
            children: [
                //用户列表
                {
                    path: '/user/list',
                    name: 'UserList',
                    alias: '/myAbout',
                    component: () => import('@/components/user/UserList.vue'),
                },
                //管理员列表
                {
                    path: '/admin/list',
                    name: 'AdminList',
                    meta: {
                        showName: '管理员列表',
                        requiresAuth: true, // 添加需要身份验证的标志
                    },
                    component: () => import('@/components/admin/AdminList.vue')
                },
                //图书列表
                {
                    path: '/admin/book',
                    name: 'AdminBook',
                    meta: {
                        showName: '图书列表',
                        requiresAuth: true, // 添加需要身份验证的标志
                    },
                    component: () => import('@/components/book/AdminBook.vue')
                },
                //借阅情况
                {
                    path: '/loan/status',
                    name: 'LoanStatus',
                    meta: {
                        showName: '图书列表',
                        requiresAuth: true, // 添加需要身份验证的标志
                    },
                    component: () => import('@/components/book/LoanStatus.vue')
                },
            ],
        },

    ],
});

// // 全局前置守卫
// router.beforeEach((to, from, next) => {
//     const isAuthenticated = false;  // 请替换为您的身份验证逻辑
//     if (isAuthenticated || allowedRoutes.includes(to.path)) {
//         next();
//     } else {
//         next('/book/IndexBook');
//     }
// });

export default router;