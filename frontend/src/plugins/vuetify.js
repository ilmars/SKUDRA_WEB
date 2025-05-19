// Vuetify
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'
import { aliases, mdi } from 'vuetify/iconsets/mdi'
import '@mdi/font/css/materialdesignicons.css'

// Theme configuration
const lightTheme = {
  dark: false,
  colors: {
    primary: '#1976D2',
    secondary: '#424242',
    accent: '#82B1FF',
    error: '#FF5252',
    info: '#2196F3',
    success: '#4CAF50',
    warning: '#FB8C00',
    background: '#FFFFFF',
    surface: '#F5F5F5',
    'on-surface': '#212121',
    'on-background': '#212121',
  },
}

const darkTheme = {
  dark: true,
  colors: {
    primary: '#2196F3',
    secondary: '#607D8B',
    accent: '#82B1FF',
    error: '#FF5252',
    info: '#2196F3',
    success: '#4CAF50',
    warning: '#FB8C00',
    background: '#121212',
    surface: '#212121',
    'on-surface': '#FFFFFF',
    'on-background': '#FFFFFF',
  },
}

export default createVuetify({
  components,
  directives,
  icons: {
    defaultSet: 'mdi',
    aliases,
    sets: {
      mdi,
    },
  },
  theme: {
    defaultTheme: 'light',
    themes: {
      light: lightTheme,
      dark: darkTheme,
    },
  },
})