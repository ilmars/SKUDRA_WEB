<template>
  <v-footer height="20" app>
    <a
      v-for="item in items"
      :key="item.title"
      :href="item.href"
      :title="item.title"
      class="d-inline-block mx-2 social-link"
      rel="noopener noreferrer"
      target="_blank"
    >
      <v-icon
        :icon="item.icon"
        :size="item.icon === '$vuetify' ? 24 : 16"
      />
    </a>

    <div
      class="text-caption text-disabled"
      style="position: absolute; right: 16px;"
    >
      <a
        class="text-decoration-none on-surface"
        href="https://www.esakari.lv/"
        rel="noopener noreferrer"
        target="_blank"
      >
      &copy; {{ (new Date()).getFullYear() }} Electronic communication office of Latvia
      </a>
    </div>
  </v-footer>
</template>

<script setup lang="ts">
  const items = [
    
    {
      title: 'SKUDRA',
      icon: `mdi-information`,
      href: 'https://skudra.esakari.lv/',
    },
    {
      title: 'support email',
      icon: `mdi-email`,
      href: 'mailto:support+skudra-skudra-server-v5-frontend-40-issue-@skudra.vases.lv',
    },
  ]
</script>



<style scoped lang="sass">
  .social-link :deep(.v-icon)
    color: rgba(var(--v-theme-on-background), var(--v-disabled-opacity))
    text-decoration: none
    transition: .2s ease-in-out

    &:hover
      color: rgba(25, 118, 210, 1)
</style>
