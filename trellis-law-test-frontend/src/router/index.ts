import {
  createMemoryHistory,
  createRouter,
  createWebHistory,
} from 'vue-router';
import EnglishNumbersPage from '../pages/EnglishNumbersPage/EnglishNumbersPage.vue';

const isServer = typeof window === 'undefined';

const routes = [
  {
    path: '/',
    redirect: '/test',
  },
  {
    path: '/test',
    name: 'Test',
    component: EnglishNumbersPage,
  },
];

const router = createRouter({
  history: isServer ? createMemoryHistory() : createWebHistory(),
  routes,
});

export default router;
