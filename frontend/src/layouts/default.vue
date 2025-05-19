<template>
  <!-- v-app is the root wrapper for Vuetify -->
  <v-app :theme="theme">
    <!-- 
      NAVBAR / HEADER:
      Could be a <v-app-bar> or a custom component
    -->
    <AppHeader @toggle-theme="toggleTheme"></AppHeader>

    <!--
      MAIN CONTENT:
      router-view is where each page's component will be loaded
    -->
    <v-main>
      <router-view />
    </v-main>

    <!-- FOOTER (optional) -->
    <!-- <v-footer app color="grey darken-3" dark>
      <v-col class="text-center">© 2025 My Company</v-col>
    </v-footer> -->
    <AppFooter />
  </v-app>
</template>

<script setup>
import { ref, onMounted, watch } from "vue";
import { useTheme } from "vuetify";
import AppFooter from "@/components/AppFooter.vue";
import AppHeader from "@/components/AppHeader.vue";

// Theme management
const vuetifyTheme = useTheme();
const theme = ref(null); // Will hold 'light' or 'dark'

// Check if the user's system prefers dark mode
const prefersDarkMode = () => {
  return window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
};

// Get theme from localStorage or use system preference
const getStoredTheme = () => {
  const storedTheme = localStorage.getItem('theme');
  if (storedTheme) {
    return storedTheme;
  }
  return prefersDarkMode() ? 'dark' : 'light';
};

// Set the theme in localStorage
const setStoredTheme = (newTheme) => {
  localStorage.setItem('theme', newTheme);
};

// Toggle between light and dark themes
const toggleTheme = () => {
  theme.value = theme.value === 'light' ? 'dark' : 'light';
  setStoredTheme(theme.value);
};

// Initialize theme on component mount
onMounted(() => {
  theme.value = getStoredTheme();
  
  // Listen for system theme changes when using system default
  const mediaQuery = window.matchMedia('(prefers-color-scheme: dark)');
  mediaQuery.addEventListener('change', (e) => {
    if (!localStorage.getItem('theme')) {
      theme.value = e.matches ? 'dark' : 'light';
    }
  });
});

// Watch for theme changes to update the theme colors dynamically
watch(theme, (newTheme) => {
  vuetifyTheme.global.name.value = newTheme;
});
</script>

<style scoped>
/* You can add layout-specific styles here */
</style>
