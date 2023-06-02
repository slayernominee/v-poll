<template>
    
    <v-breadcrumbs :items="breadcrumps">
        <template v-slot:prepend>
            <v-icon size="small" icon="$vuetify"></v-icon>
        </template>
    </v-breadcrumbs>
    
    <v-container>
        <h1 class="text-center">About</h1>
        
        <p class="text-center mt-5">Naja hier gibts net wirklich was zu sehen lmao</p>
    </v-container>
    
</template>

<script>
export default {
    name: "About-View",
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
                text: 'About',
                disabled: true,
                link: true,
                exact: true,
                to: {
                    name: 'About', 
                    params: {}
                }
            }
            ]
        }
    }
}
</script>