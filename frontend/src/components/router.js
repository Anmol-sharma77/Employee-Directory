import { createRouter, createWebHistory } from 'vue-router';
import login from '../components/login.vue';
import signup from '../components/signup.vue';
import notfound from '../components/404.vue';
import home from '../components/home.vue';
import add from '../components/add.vue';


const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', component:login},
    { path: '/login', component: login },
    {path:'/signup',component: signup},
    {path:'/addemployee',component:add},
    {path:'/home',component:home},
    { path: '/:catchAll(.*)', component: notfound },
  ]
});

export default router;
