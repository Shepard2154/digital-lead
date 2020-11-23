<template>
    <div>
        <v-row>
            <v-col cols="3">
                <div class="menu">
                    <v-col>
                        <a v-bind:class="{ 'red--text': isActive1 }" @click="getComplaints">Мои жалобы</a>
                    </v-col>
                    <v-col>
                        <a v-bind:class="{ 'red--text': isActive2 }" @click="getOffers">Мои предложения</a>
                    </v-col>
                    <v-col>
                        <a v-bind:class="{ 'red--text': isActive3 }" @click="getOffers2">Избранное</a>
                    </v-col>
                </div>
            </v-col>
            <v-col cols="8" class="p-3 pr-6">
                <report :isLikable="false" v-for="i in reports" :key="i.text" :data="i"/>
            </v-col>
        </v-row>
    </div>
</template>

<script>
import report from '../components/report.vue'

export default {
    components: {
      report
    },
    data: () => ({
        reports: [],
        isActive1: true,
        isActive2: false,
        isActive3: false,
    }),

    mounted() {
        axios({
            method: 'GET',
            url: 'http://127.0.0.1:8000/message/get/?event=T&author=6'
        }).then(response => {
            this.reports = response.data.data
        })
    },
    methods: {
        getComplaints(){
            this.isActive2 = false
            this.isActive3 = false
            this.isActive1 = true
            axios({
                method: 'GET',
                url: 'http://127.0.0.1:8000/message/get/?event=T&author=6'
            }).then(response => {
                this.reports = response.data.data
            })
        },

        getOffers(){
            this.isActive1 = false
            this.isActive3 = false
            this.isActive2 = true
            axios({
                method: 'GET',
                url: 'http://127.0.0.1:8000/message/get/?event=Y&author=6'
            }).then(response => {
                this.reports = response.data.data
            })
        },

        getOffers2(){
            this.isActive1 = false
            this.isActive2 = false
            this.isActive3 = true
                axios({
                method: 'GET',
                url: 'http://127.0.0.1:8000/message/get/?event=CW&author=6'
            }).then(response => {
                this.reports = response.data.data
            })
        }
    }
}
</script>

<style scoped>
    a{
        font-family: Century Gothic;
        font-size: 30px;
        line-height: 25px;
        padding-bottom: 40px;
        font-weight: 900;
        padding-top: 30px;
    }
    .menu{
        padding-top: 80px;
        padding-left: 60px;
    }
    .report-msg{
        margin-bottom: 30px;
    }
    .divider{
        margin-top: 50px;
    }
</style>
