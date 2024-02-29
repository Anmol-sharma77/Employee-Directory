import { createRouter, createWebHistory } from 'vue-router';
import login from '../components/login.vue';
import signup from '../components/signup.vue';

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', component: login },
    { path: '/login', component: login },
    {path:'/signup',component: signup}
  ]
});

export default router;
