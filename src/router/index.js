// Composables
import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    component: () => import('@/layouts/default/Default.vue'),
    children: [
      {
        path: '',
        name: 'Home',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import(/* webpackChunkName: "home" */ '@/views/Home.vue'),
      },
      {
        path: '/about',
        name: 'About',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import(/* webpackChunkName: "about" */ '@/views/About.vue'),
      },
      {
        path: '/poll/:id',
        name: 'Poll',

        component: () => import(/* webpackChunkName: "poll" */ '@/views/Poll.vue'),
      },
      {
        path: '/poll_result/:id',
        name: 'PollEnd',

        component: () => import(/* webpackChunkName: "poll_result" */ '@/views/PollEnd.vue'),
      },
      {
        path: '/login',
        name: 'Login',

        component: () => import(/* webpackChunkName: "login" */ '@/views/Login.vue'),
      },
      {
        path: '/poll/result/:id',
        name: 'PollResult',

        component: () => import(/* webpackChunkName: "poll_result" */ '@/views/PollResult.vue'),
      }
    ],
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
