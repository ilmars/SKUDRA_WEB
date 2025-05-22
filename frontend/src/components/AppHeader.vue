<template>

<v-app-bar app dark :elevation="9">
    <!-- <v-app-bar-nav-icon @click.stop="drawerOpen = !drawerOpen" /> -->
    <v-toolbar-title>
      <router-link :to="{ name: 'mainpage' }" style="text-decoration: none; color: inherit;">
      {{ title }}
      </router-link>
    </v-toolbar-title>
    <!-- Spacer pushes the following items to the right -->
    <v-spacer />

    <v-btn text :to="{ name: 'mainpage-map' }"> Map </v-btn>
    <v-btn text :to="{ name: 'not-found' }"> Not Found </v-btn>
    <!-- <v-btn text :to="{ name: 'contact' }"> Contact </v-btn> -->
    <!-- <v-spacer /> -->
      <!-- Theme Toggle Button -->
    <v-btn icon @click="$emit('toggle-theme')">
      <v-icon>{{ isDarkTheme ? 'mdi-white-balance-sunny' : 'mdi-moon-waning-crescent' }}</v-icon>
    </v-btn>

    <!-- User Menu -->
    <v-menu>
      <!-- Activator slot: the avatar button that opens the menu -->
      <template #activator="{ props }">
        <v-btn v-bind="props">
          <v-avatar>
            <v-icon icon="mdi-account" size="24" />
          </v-avatar>
          {{ userName }}
        </v-btn>
        
      </template>

      <!-- Menu content: shows user name, profile link, logout, etc. -->
      <v-list>


        <!-- <v-divider /> -->

        <!-- Example profile link -->
        <v-list-item :to="{ name: 'mainpage-map' }">
          <v-list-item-title>Profile</v-list-item-title>
        </v-list-item>

        <!-- Logout option -->
        <v-list-item @click="logout">
          <v-list-item-title>Logout</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-menu>

   
  </v-app-bar>
</template>

<script setup>
import { ref, computed } from 'vue';
import { useTheme } from 'vuetify';

// Props or data
const drawerOpen = ref(false);
const title = "SKUDRA WEB";

// Example links for the navigation drawer
const links = [
  { to: "/", title: "Home" },
  { to: "/about", title: "About" },
  // etc...
];

const userName = "John Doe";

// Example logout function
function logout() {
  // e.g., Clear tokens, redirect, etc.
  alert("Logging out...");
}

// Access the current theme
const vuetifyTheme = useTheme();

// Compute whether current theme is dark
const isDarkTheme = computed(() => {
  return vuetifyTheme.global.current.value.dark;
});

// We'll emit an event when the theme toggle is clicked
defineEmits(['toggle-theme']);
</script>