<template>
    <v-breadcrumbs :items="breadcrumps">
        <template v-slot:prepend>
            <v-icon size="small" icon="$vuetify"></v-icon>
        </template>
    </v-breadcrumbs>

    <v-container class="text-center my-15">
        <h1>Abstimmung beendend</h1>

        <v-icon class="my-5" size="100">mdi-party-popper</v-icon>

        <p>Vielen Dank für deine Teilnahme an diesem Poll.</p>

        <v-btn @click="$router.push({ name: 'Home' })" class="mt-10" variant="tonal" size="x-large">
            <v-icon class="mr-2">mdi-home</v-icon>
            Home
        </v-btn>
    </v-container>
</template>

<script>
export default {
    name: "Poll-End",
    data() {
        let id = this.$route.params.id;
        return {
            breadcrumps: [
                {
                    text: "Home",
                    disabled: false,
                    link: true,
                    exact: true,
                    to: {
                        name: "Home",
                        params: {},
                    }
                },
                {
                    text: "Polls",
                    disabled: false,
                    link: true,
                    exact: true,
                    to: {
                        name: "Poll",
                        params: { id: id },
                    }
                },
                {
                    text: id,
                    disabled: true,
                    link: true,
                    exact: true,
                    to: {
                        name: "Poll",
                        params: { id: id },
                    }
                }
            ]
        }
    }
}
</script>