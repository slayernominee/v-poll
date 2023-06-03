<template>
    
    <v-breadcrumbs :items="breadcrumps">
        <template v-slot:prepend>
            <v-icon size="small" icon="$vuetify"></v-icon>
        </template>
    </v-breadcrumbs>
    
    <v-container class="text-center">

        
        <v-alert
        id="already_voted_alert"
        v-model="already_voted_alert"
        border="start"
        elevation="2"
        closable
        type="warning"
        class="my-5 text-left"
        close-label="Schließen"
        title="Bereits Abgestimmt"
        >
        Du hast bereits für diese Umfrage abgestimmt, insofern werden weitere Abgaben nicht mehr gezählt.<br>
        Wenn du denkst, dass das ein Fehler ist, dann kontaktiere bitte einen Administrator.<br>
        </v-alert
        >
        
        
        
        
        <h1>{{ title }}</h1>
        
        <v-container class="border rounded-xl my-5" style="min-height: 60vh" v-if="questions.length > 0">
            <div>
                <h3 class="text-h5 text-center">{{ questions[page - 1].title }}</h3>
                
                <p class="text-center w-50 mx-auto my-5">{{ questions[page - 1].text }}</p>
                
                <div v-if="questions[page - 1].answers && questions[page - 1].answers.length > 0">
                    <v-slider 
                    v-if="questions[page - 1].answers[0].component == 'v-slider'"
                    color="orange"
                    class="w-75 mx-auto"
                    :min="questions[page - 1].answers[0].range[0]"
                    :max="questions[page - 1].answers[0].range[1]"
                    :step="questions[page - 1].answers[0].steps"
                    v-model="questions[page - 1].answers[0].selected"
                    thumb-label></v-slider>
                    
                    <v-select
                    v-if="questions[page - 1].answers[0].component == 'v-select'"
                    class="w-50 mx-auto my-5 text-left"
                    :label="questions[page - 1].answers[0].label"
                    :hint="questions[page - 1].answers[0].hint"
                    persistent-hint
                    :multiple="questions[page - 1].answers[0].multiple"
                    :chips="questions[page - 1].answers[0].chips"
                    v-model="questions[page - 1].answers[0].selected"
                    :items="questions[page - 1].answers[0].options"
                    ></v-select>
                    
                    <v-text-field
                    v-if="questions[page - 1].answers[0].component == 'v-text'"
                    :label="questions[page - 1].answers[0].label"
                    v-model="questions[page - 1].answers[0].selected"
                    class="w-50 mx-auto"
                    ></v-text-field>
                </div>
                
            </div>
            
            <v-btn v-show="page < questionCount" @click="next_question">Weiter</v-btn>
            <v-btn v-show="page == questionCount" @click="send_poll" :disabled="!voteable">Absenden</v-btn>
            
        </v-container>
        
        {{ question_count }}
        
        <v-pagination v-model="page" :length="questionCount"></v-pagination>
        
    </v-container>
    
</template>

<script>
import axios from 'axios';

export default {
    name: "Poll-View",
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
                    params: {},
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
            ],
            title: "<Poll Titel>",
                page: 1,
                questions: [],
                already_voted_alert: false,
                voteable: true,
            }
        },
        methods: {
            next_question() {
                if (this.page < this.questionCount) {
                    this.page++;
                }
            },
            send_poll() {
                let id = this.$route.params.id;
                let bow = [];
                for (let i = 0; i < this.questionCount; i++) {
                    bow.push(this.questions[i].answers[0].selected);
                }
                
                //console.log(bow);
                axios.post(this.$api + 'postPoll/' + id, {answers: bow}).then(response => {
                    console.log(response);
                    this.$router.push({name: 'PollResult', params: {id: id}});
                }).catch(err => {
                    if (err.response.status == 403 && err.response.data == 'already voted') {
                        this.already_voted_alert = true;
                        this.voteable = false;
                        document.getElementById('already_voted_alert').scrollIntoView();
                    }
                })
            }
        },  
        created() {
            let id = this.$route.params.id;
            axios.post(this.$api + 'getPoll/' + id).then(response => {
                this.title = response.data.title;
                this.questions = response.data.questions;
                //console.log(response);
                //console.log(response.data.questions);
                axios.post(this.$api + 'voteable/' + id).then(response => {
                    this.voteable = response.data.voteable;
                    if (!this.voteable) {
                        this.already_voted_alert = true;
                    }
                })
            }).catch(err => {
                if (err.response.status == 404) {
                    this.title = 'Poll nicht gefunden';
                } else if (err.response.status == 400) {
                    this.title = 'Ungültige Anfrage';
                } else {
                    // an unknown error occured
                    // console.log(err);
                }
            });
        },
        computed: {
            questionCount() {
                return this.questions.length
            }
        }
    }
</script>