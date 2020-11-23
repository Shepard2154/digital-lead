import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'login',
    meta: { layout: 'empty' },
    component: () => import('../views/Login.vue')
  },
  {
    path: '/signup',
    name: 'sigh',
    meta: { layout: 'empty' },
    component: () => import('../views/Signup.vue')
  },

  {
    path: '/main',
    name: 'home',
    meta: { layout: 'main' },
    component: () => import('../views/Home.vue')
  },
  {
    path: '/statistics',
    name: 'statistics',
    meta: { layout: 'main' },
    component: () => import('../views/Statistics.vue'),
  },
  {
    path: '/reports',
    name: 'reports',
    meta: { layout: 'main' },
    component: () => import('../views/Reports.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
