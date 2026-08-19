// 引入路由配置文件
import {createRouter, createWebHistory} from 'vue-router';

// 定义路由配置对象 -- 数组
const routes = [
    {
        // 一个页面的访问路径就是一个 js 对象，至少包含 2 个属性：path、component
        path: '',   // 访问路径，和服务器的请求路访问规则一致
        meta:{
            login:false  // 该页面是否允许（或需要）登录态访问
        },
        component: () => import('../components/Login.vue')    // 访问组件
    },
    {
        // 一个页面的访问路径就是一个 js 对象，至少包含 2 个属性：path、component
        path: '/chat',   // 访问路径，和服务器的请求路访问规则一致
        meta:{
            login:true // 该页面是否允许（或需要）登录态访问
        },
        component: () => import('../components/Chat.vue')    // 访问组件
    }
]

// 设置路由模式为 history 模式 -- 默认 hash 模式，访问路径中间有一个 # 号
const router = createRouter({
    history: createWebHistory(),
    routes
})

// 导出路由实例
export default router
