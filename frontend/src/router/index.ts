/**
 * router/index.ts
 *
 * Automatic routes for `./src/pages/*.vue`
 */

// Composables
import { createRouter, createWebHistory } from 'vue-router/auto'
import { setupLayouts } from 'virtual:generated-layouts'
import { routes } from 'vue-router/auto-routes'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: setupLayouts(routes),
})



router.addRoute({
  path: '/',
  name: 'mainpage',
  component: () => import('@/layouts/default.vue'),
  children: [
    {
      path: 'map',
      name: 'mainpage-map',
      component: () => import('@/pages/map/index.vue') 
    }
  ],
  meta: {
    requiresAuth: true,
    layout: 'default'
  }
})

router.addRoute({
  path: '/:pathMatch(.*)*', // Catch-all route for 404
  name: 'not-found',
  component: () => import('@/pages/NotFoundPage.vue'),
  meta: {
    layout: 'error'
  }
})
// Workaround for https://github.com/vitejs/vite/issues/11804
router.onError((err, to) => {
  if (err?.message?.includes?.('Failed to fetch dynamically imported module')) {
    if (!localStorage.getItem('vuetify:dynamic-reload')) {
      console.log('Reloading page to fix dynamic import error')
      localStorage.setItem('vuetify:dynamic-reload', 'true')
      location.assign(to.fullPath)
    } else {
      console.error('Dynamic import error, reloading page did not fix it', err)
    }
  } else {
    console.error(err)
  }
})

router.isReady().then(() => {
  localStorage.removeItem('vuetify:dynamic-reload')
})

export default router
