<template>
  
  <v-breadcrumbs :items="breadcrumps">
    <template v-slot:prepend>
      <v-icon size="small" icon="$vuetify"></v-icon>
    </template>
  </v-breadcrumbs>
  
  <v-container>
    <h1>Home</h1>
  </v-container>
  

  
</template>

<script>
export default {
  name: "Home-View",
  data() {
    return {
      breadcrumps: [
      {
        text: 'Home',
        disabled: false,
        link: true,
        exact: true,
        to: {
            name: 'Home', 
            params: {}
        }
      },
      {
        text: 'Overview',
        disabled: true,
        link: true,
        exact: true,
        to: {
            name: 'Home', 
            params: {}
        }
      }
      ]
    }
  }
}
</script>