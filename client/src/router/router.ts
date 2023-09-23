import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import Home from '../views/Home.vue'
import Calculator from '../views/Calculator.vue'
import Viewer from '../views/Viewer.vue'

const routes: Array<RouteRecordRaw> = [
  { path: '/', component: Home },
  { path: '/calculator', component: Calculator },
  { path: '/viewer', component: Viewer },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;