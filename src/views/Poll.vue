<template>
    
    <v-breadcrumbs :items="breadcrumps">
        <template v-slot:prepend>
            <v-icon size="small" icon="$vuetify"></v-icon>
        </template>
    </v-breadcrumbs>
    
    <v-container class="text-center">
        <h1>{{ title }}</h1>
        
        <v-container class="border rounded-xl my-5" style="min-height: 60vh">
            <div>
                <h3 class="text-h5 text-center">{{ questions[page - 1].title }}</h3>
                
                <p class="text-center w-50 mx-auto my-5">{{ questions[page - 1].text }}</p>
                
                <v-slider 
                v-if="questions[page - 1].answers[0].component == 'v-slider'"
                color="orange"
                :min="questions[page - 1].answers[0].range[0]"
                :max="questions[page - 1].answers[0].range[1]"
                :step="questions[page - 1].answers[0].steps"
                thumb-label></v-slider>
                
                <v-select
                v-if="questions[page - 1].answers[0].component == 'v-select'"
                label="Select"
                :items="['California', 'Colorado', 'Florida', 'Georgia', 'Texas', 'Wyoming']"
                ></v-select>
                
            </div>
            
            <v-btn v-show="page < questionCount" @click="next_question">Weiter</v-btn>
            <v-btn v-show="page == questionCount">Absenden</v-btn>
            
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
                    params: { id: ":id" },
                }
            }
            ],
            title: "<Poll Titel>",
                page: 1,
                questions: [],
            }
        },
        methods: {
            next_question() {
                if (this.page < this.questionCount) {
                    this.page++;
                }
            }
        },  
        created() {
            let id = this.$route.params.id;
            axios.get('/api/getPoll/' + id).then(response => {
                console.log(response)
            });
            // should get the title, questions
            this.title = 'Umfragen Titel';
            this.questions = [
            {
                title: 'Question 1',
                text: `Culpa cupidatat deserunt occaecat ipsum Lorem anim officia duis eu Lorem non. Cupidatat do commodo sunt tempor Lorem fugiat reprehenderit incididunt qui. Id anim dolor minim ex labore exercitation laboris cupidatat. Minim non duis laborum anim irure labore nostrud enim nostrud aliqua. Commodo consectetur sunt cillum dolor sit consequat. Labore nostrud adipisicing labore nisi ut aliqua minim aute deserunt ullamco ex velit eiusmod. Voluptate occaecat magna ea aute id duis deserunt.
                
                Quis exercitation culpa et commodo velit id anim esse. Consectetur magna elit occaecat Lorem mollit. Amet nostrud aliqua ea excepteur. Ad incididunt enim sit elit adipisicing eu tempor Lorem dolore sunt eiusmod. Dolore elit amet officia pariatur cupidatat anim reprehenderit voluptate anim ex aliquip proident cillum ad.`,
                answers: [
                {
                    component: 'v-select',
                    // TODO: multiple support, chip support also beide mit true, false
                }
                ]
            },
            {
                title: 'Question 2',
                text: `Question 2 ist sehr kurz ...`,
                answers: [
                {
                    component: 'v-slider',
                    range: [1, 10],
                    steps: 0.1,
                }
                ]
            },
            {
                title: 'Question 3',
                text: `Culpa cupidatat deserunt occaecat ipsum Lorem anim officia duis eu Lorem non. Cupidatat do commodo sunt tempor Lorem fugiat reprehenderit incididunt qui. Id anim dolor minim ex labore exercitation laboris cupidatat. Minim non duis laborum anim irure labore nostrud enim nostrud aliqua. Commodo consectetur sunt cillum dolor sit consequat. Labore nostrud adipisicing labore nisi ut aliqua minim aute deserunt ullamco ex velit eiusmod. Voluptate occaecat magna ea aute id duis deserunt.
                
                Quis exercitation culpa et commodo velit id anim esse. Consectetur magna elit occaecat Lorem mollit. Amet nostrud aliqua ea excepteur. Ad incididunt enim sit elit adipisicing eu tempor Lorem dolore sunt eiusmod. Dolore elit amet officia pariatur cupidatat anim reprehenderit voluptate anim ex aliquip proident cillum ad.`,
                answers: [
                {
                    component: 'v-slider',
                    range: [0, 100],
                    steps: 10,
                }
                ]
            },
            {
                title: 'Question 4',
                text: `Culpa cupidatat deserunt occaecat ipsum Lorem anim officia duis eu Lorem non. Cupidatat do commodo sunt tempor Lorem fugiat reprehenderit incididunt qui. Id anim dolor minim ex labore exercitation laboris cupidatat. Minim non duis laborum anim irure labore nostrud enim nostrud aliqua. Commodo consectetur sunt cillum dolor sit consequat. Labore nostrud adipisicing labore nisi ut aliqua minim aute deserunt ullamco ex velit eiusmod. Voluptate occaecat magna ea aute id duis deserunt.
                
                Quis exercitation culpa et commodo velit id anim esse. Consectetur magna elit occaecat Lorem mollit. Amet nostrud aliqua ea excepteur. Ad incididunt enim sit elit adipisicing eu tempor Lorem dolore sunt eiusmod. Dolore elit amet officia pariatur cupidatat anim reprehenderit voluptate anim ex aliquip proident cillum ad.`,
                answers: [
                {
                    component: 'v-slider',
                    range: [1, 10],
                    steps: 0.1,
                }
                ]
            },
            {
                title: 'Question 5',
                text: `Culpa cupidatat deserunt occaecat ipsum Lorem anim officia duis eu Lorem non. Cupidatat do commodo sunt tempor Lorem fugiat reprehenderit incididunt qui. Id anim dolor minim ex labore exercitation laboris cupidatat. Minim non duis laborum anim irure labore nostrud enim nostrud aliqua. Commodo consectetur sunt cillum dolor sit consequat. Labore nostrud adipisicing labore nisi ut aliqua minim aute deserunt ullamco ex velit eiusmod. Voluptate occaecat magna ea aute id duis deserunt.
                
                Quis exercitation culpa et commodo velit id anim esse. Consectetur magna elit occaecat Lorem mollit. Amet nostrud aliqua ea excepteur. Ad incididunt enim sit elit adipisicing eu tempor Lorem dolore sunt eiusmod. Dolore elit amet officia pariatur cupidatat anim reprehenderit voluptate anim ex aliquip proident cillum ad.`,
                answers: [
                {
                    component: 'v-slider',
                    range: [1, 10],
                    steps: 0.1,
                }
                ]
            },
            {
                title: 'Question 6',
                text: `Culpa cupidatat deserunt occaecat ipsum Lorem anim officia duis eu Lorem non. Cupidatat do commodo sunt tempor Lorem fugiat reprehenderit incididunt qui. Id anim dolor minim ex labore exercitation laboris cupidatat. Minim non duis laborum anim irure labore nostrud enim nostrud aliqua. Commodo consectetur sunt cillum dolor sit consequat. Labore nostrud adipisicing labore nisi ut aliqua minim aute deserunt ullamco ex velit eiusmod. Voluptate occaecat magna ea aute id duis deserunt.
                
                Quis exercitation culpa et commodo velit id anim esse. Consectetur magna elit occaecat Lorem mollit. Amet nostrud aliqua ea excepteur. Ad incididunt enim sit elit adipisicing eu tempor Lorem dolore sunt eiusmod. Dolore elit amet officia pariatur cupidatat anim reprehenderit voluptate anim ex aliquip proident cillum ad.`,
                answers: [
                {
                    component: 'v-slider',
                    range: [1, 10],
                    steps: 0.1,
                }
                ]
            },
            {
                title: 'Question 7',
                text: `Culpa cupidatat deserunt occaecat ipsum Lorem anim officia duis eu Lorem non. Cupidatat do commodo sunt tempor Lorem fugiat reprehenderit incididunt qui. Id anim dolor minim ex labore exercitation laboris cupidatat. Minim non duis laborum anim irure labore nostrud enim nostrud aliqua. Commodo consectetur sunt cillum dolor sit consequat. Labore nostrud adipisicing labore nisi ut aliqua minim aute deserunt ullamco ex velit eiusmod. Voluptate occaecat magna ea aute id duis deserunt.
                
                Quis exercitation culpa et commodo velit id anim esse. Consectetur magna elit occaecat Lorem mollit. Amet nostrud aliqua ea excepteur. Ad incididunt enim sit elit adipisicing eu tempor Lorem dolore sunt eiusmod. Dolore elit amet officia pariatur cupidatat anim reprehenderit voluptate anim ex aliquip proident cillum ad.`,
                answers: [
                {
                    component: 'v-slider',
                    range: [1, 10],
                    steps: 0.1,
                }
                ]
            },
            ]
        },
        computed: {
            questionCount() {
                return this.questions.length
            }
        }
    }
</script>