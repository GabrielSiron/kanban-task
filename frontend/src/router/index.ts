import {createRouter, createWebHistory} from 'vue-router'

import signup from '../pages/signup.vue'

export const router = createRouter({
  history: createWebHistory(),
  routes:[
      { path: '/signup', component: signup}
  ]
});