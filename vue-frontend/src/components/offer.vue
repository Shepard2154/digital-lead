<template>
    <v-card class="mr-3 pb-6">
        <v-card-title justify="space-between">
            <v-row justify="space-between" class="px-3 text">
                {{data.date}}
            </v-row>
        </v-card-title>

        <v-card-text class="text" style="font-size: 14px">{{data.text}}</v-card-text>

        <span class="green--text">Жалоба на рассмотрении</span>
    </v-card>
</template>

<script>
export default {
    props: ['data'],

    data() {
        return {
            liked: false
        }
    },

    computed: {
        color() {
            if (this.liked) return 'pink'
            else return "#F58D8E"
        }
    },

    methods: {
        like() {
            if (this.liked) this.data.likes--
            else this.data.likes++
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
    span {
        margin-left: 1000px;
    }
</style>
