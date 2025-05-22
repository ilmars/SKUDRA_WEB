/**
 * main.ts
 *
 * Bootstraps Vuetify and other plugins then mounts the App`
 */

// Plugins
import { registerPlugins } from '@/plugins'

// Components
import App from './App.vue'

// Composables
import { createApp } from 'vue'

// Router and Store
import router from './router'
import store from './store'

const app = createApp(App)

// Register store
app.use(store)
app.use(router)

registerPlugins(app)

app.mount('#app')
