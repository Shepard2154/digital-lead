<template>
<div>
    <chart @click="get_messages('CW')"/>

    <v-row justify="center">
        <v-col cols="4">
            <districts :states="dist" label="Укажите свой район"/>
            <districts :states="classes" label="Выберите класс происшествия"/>
            <day-statistics class="ml-4"/>
        </v-col>

        <v-col cols="8" class="p-3 pr-6">
            <Report :isLikable="true" v-for="i in reports" :key="i.text" :data="i"/>
        </v-col>
    </v-row>
</div>
</template>

<script>
import Vue from 'vue'
import DayStatistics from '../components/Statistics/DailyCalendar.vue'
import chart from '../components/Statistics/chart.vue'
import districts from '../components/autocomplete.vue'
import Report from '../components/report.vue'

export default {
    data() {
        return {
            dist: [
                'Выборгский район',
                'Московский район',
                'Петродворцовый район',
                'Курортный район',
                'Приморский район',
                'Пушкинский район',
                'Петроградский район',
                'Василеостровский район',
                'Красносельский район',
                'Невский район',
                'Центральный район',
                'Адмиралтейский район',
                'Фрунзенская район',
                'Калининский район',
                'Кировский район',
                'Кронштадтский район',
                'Колпинский район',
                'Красногвардейский район'
            ],

            classes: [
                'Дтп',
                'Пожар',
                'Свалка',
                'Загрязнение водоемов',
                'Дороги',
                'Благоустройство домов',
                'Благоустройство дворов',
                'Благоустройство придомовых территорий',
                'Нарушение водоснабжения',
                'Нарушение электроснабжения'
            ],

            reports: []
        }
    },


    mounted() {
       this.get_messages('T')
    },

    methods: {
        get_messages(cl) {
            axios({
                method: 'GET',
                url: `http://127.0.0.1:8000/message/get/?event=${cl}&date_before=2020-03-23T12:58:20.204316Z`
            }).then(response => {
                this.reports = response.data.data
            })
        }
    },

    components: {
        DayStatistics,
        districts,
        chart,
        Report
    },
}
</script>

<style scoped>
</style>