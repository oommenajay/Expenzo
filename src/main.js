import './assets/main.css'
import '@fortawesome/fontawesome-free/css/all.css';
import { createApp } from 'vue'
import App from './App.vue'
import '@fortawesome/fontawesome-free/css/all.css'
import '@fortawesome/fontawesome-free/js/all.js'
import { createWebHistory, createRouter } from 'vue-router'
import Dashboard from './components/Dashboard.vue'
import Transaction from './components/Transaction.vue';
import Login from './components/Login.vue'
import Budget from './components/Budget.vue'
const routes = [
    { path: '/', component: Login },
    {path: '/dashboard', component: Dashboard},
    {path:'/transaction', component:Transaction},
    {path:'/budget',component:Budget}
  ]

  const router = createRouter({
    history: createWebHistory(),
    routes,
  })

createApp(App)
    .use(router)
    .mount('#app')
