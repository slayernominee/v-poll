<template>
  
  <v-breadcrumbs :items="breadcrumps">
    <template v-slot:prepend>
      <v-icon size="small" icon="$vuetify"></v-icon>
    </template>
  </v-breadcrumbs>
  
  <v-container class="text-center">
    <h1 class="mb-5">Home</h1>
    
    <div class="mt-15">
      <h2 class="my-4 text-h5">Empholene Abstimmungen</h2>
      <div class="d-flex flex-wrap justify-center">
        <v-card v-for="poll in popular_polls" :title="poll.title" :text="poll.description" @click="$router.push({ name: 'Poll', params: { id: poll.id } })" class="w-25 mx-5 my-3" variant="tonal"></v-card>
      </div>
    </div>
  </v-container>
  
  
  
</template>

<script>
import axios from 'axios';

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
      ],
      popular_polls: []
    }
  },
  created() {
    axios.post(this.$api + '/getPopularPolls').then(response => {
      this.popular_polls = response.data.popular_polls;
    });
  }
}
</script>