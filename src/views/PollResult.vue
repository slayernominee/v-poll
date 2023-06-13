<template>
    <v-breadcrumbs :items="breadcrumps">
        <template v-slot:prepend>
            <v-icon size="small" icon="$vuetify"></v-icon>
        </template>
    </v-breadcrumbs>
    <v-container>
        <h1 class="text-center">Abstimmungs Ergebnisse</h1>
        
        <div class="bg-grey-darken-4 pt-4 pl-7 pr-7 mt-7 pb-3 rounded-lg">
            <div v-for="(question, i) in questions" class="mt-4">
                <h2>{{ question.title }}</h2>
                
                <v-table theme="dark">
                    <thead>
                        <tr>
                            <th class="text-left">
                                Option
                            </th>
                            <th class="text-left">
                                Stimmen
                            </th>
                            <th class="text-left">
                                Prozent
                            </th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr
                        v-for="answer in answers[i]"
                        >
                        <td>{{ answer }}</td>
                        <td>1</td>
                        <td>...</td>
                    </tr>
                </tbody>
            </v-table>
            
            <hr class="mt-7 mb-7">
        </div>
    </div>
</v-container>
</template>

<script lang="ts">
import axios from 'axios';

export default {
    name: 'PollResult',
    data() {
        let id = this.$route.params.id;
        return {
            answers: [],
            questions: [],
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
                text: "Poll Result",
                disabled: false,
                link: true,
                exact: true,
                to: {
                    name: "PollResult",
                    params: {},
                }
            },
            {
                text: id,
                disabled: true,
                link: true,
                exact: true,
                to: {
                    name: "PollResult",
                    params: { id: id },
                }
            }
            ]
        }
    },
    created() {
        let id = this.$route.params.id;
        axios.post(this.$api + 'getResult/' + id).then((res) => {
            this.questions = res.data.questions;
            this.answers = res.data.answers;
        });
    }
}

</script>

<style scoped>

</style>