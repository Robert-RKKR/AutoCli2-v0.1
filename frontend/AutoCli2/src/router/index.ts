import { createRouter, createWebHistory } from 'vue-router'

// View import:
import DashboardView from '../views/DashboardView.vue'
import SettingsView from '../views/SettingsView.vue'
import HomeView from '../views/HomeView.vue'
import HostsView from '../views/HostsView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
        path: '/dashboard',
        name: 'dashboard',
        component: DashboardView
    },
    {
        path: '/settings',
        name: 'settings',
        component: SettingsView
    },
    {
        path: '/hosts',
        name: 'hosts',
        component: HostsView
    }
  ]
})

export default router
