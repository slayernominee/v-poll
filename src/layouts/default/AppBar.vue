<template>
  <v-tabs
  v-model="tab"
  bg-color="grey-darken-4"
  >
  <v-tab @click="$router.push('/')" class="w-25"><v-icon class="mr-2">mdi-home</v-icon> Home</v-tab>
  
  <div class="w-50"></div>

  <div class="text-right w-25">
    <v-tab @click="toggleTheme"><v-icon>mdi-weather-night</v-icon></v-tab>
    <v-tab @click="$router.push('/about')"><v-icon>mdi-information</v-icon></v-tab>
  </div>
  </v-tabs
  >
  
</template>


<script>
import { useTheme } from 'vuetify'

export default {
  setup () {
    const theme = useTheme()
    
    return {
      theme,
      toggleTheme: () => theme.global.name.value = theme.global.current.value.dark ? 'light' : 'dark'
    }
  },
}
</script>
