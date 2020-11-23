<template>
    <v-card class="mr-3 my-4 pb-6">
        <v-card-title justify="space-between">
            <v-row justify="space-between" class="px-3 text">
                <v-row>
                    <p v-if="isLikable">Предложение от пользователя:</p>
                    <p>
                        <b class="ml-3">{{data.author.name}}</b>
                        <b class="ml-3">{{data.author.second_name}}</b>
                    </p>
                </v-row>
                {{data.date}}
            </v-row>
        </v-card-title>

        <v-card-text class="text" style="font-size: 14px">{{data.text}}</v-card-text>

        <v-btn v-if="isLikable" style="position: absolute; right: 20px; bottom: 10px;"
            class="mx-2"
            rounded
            dark
            small
            :color="color"
            @click="like()"
        >
            Поддержать жалобу
            <v-icon dark class="mx-2">
            mdi-heart
            </v-icon>
            {{likes}}
        </v-btn>
    </v-card>
</template>

<script>
export default {
    props: ['data', 'isLikable'],

    data() {
        return {
            liked: false,
            likes: Math.floor(Math.random() * Math.floor(100))
        }
    },

    computed: {
        color() {
            if (this.liked) return 'pink'
            else return "#F58D8E"
        }
    },

    mounted(){
        let date = new Date(this.data.date)
        this.data.date = date.getDate() + '-' + (date.getMonth()+1) + '-' + date.getFullYear()
    },

    methods: {
        like() {
            if (this.liked) this.likes--
            else this.likes++
            this.liked = !this.liked
        }
    }
}
</script>


<style scoped>
.text {
    font-family: Roboto;
    font-style: normal;
    font-size: 20px;
    line-height: 21px;
}
</style>