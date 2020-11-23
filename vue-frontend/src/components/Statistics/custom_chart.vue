<template>
    <div>
        <div>
            <canvas id="ch" width="400px" height="200px"></canvas>
        </div>

        <div class="text-center">
            <v-btn
            rounded
            dark
            @click="cur_chart = 'Час'"
            :color = "color('Час')"
            class="mx-2"
            >
            Час
            </v-btn>

            <v-btn
            rounded
            dark
            @click="cur_chart = 'День'"
            :color = "color('День')"
            class="mx-2"
            >
            День
            </v-btn>

            <v-btn
            rounded
            dark
            @click="cur_chart = 'Месяц'"
            :color = "color('Месяц')"
            class="mx-2"
            >
            Месяц
            </v-btn>

            <v-btn
            rounded
            dark
            @click="cur_chart = 'Год'"
            :color = "color('Год')"
            class="mx-2"
            >
            Год
            </v-btn>
        </div>
    </div>
</template>

<script>
import Vue from 'vue'

export default {
    data() {
        return {
            labels: [],
            chart_data: [],
            chart_type: 'bar',
            cur_chart: 'Час'
        }
    },

    watch: {
        cur_chart: function(val) {
            this.change_chart(val);
            this.draw_chart();
        }
    },

    methods: {
        color(val) {
            if (this.cur_chart == val) return "success"
            else return 'primary'
        },

        draw_chart() {
            var ctx = document.getElementById("ch").getContext('2d');
            var myChart = new Chart(ctx, {
                type: this.chart_type,
                data: {
                    labels: this.labels,
                    datasets: [{
                        label: this.cur_chart,
                        data: this.chart_data,
                        backgroundColor: [
                            'rgba(255, 99, 132, 0.2)',
                            'rgba(54, 162, 235, 0.2)',
                            'rgba(255, 206, 86, 0.2)',
                            'rgba(75, 192, 192, 0.2)',
                            'rgba(153, 102, 255, 0.2)',
                            'rgba(255, 159, 64, 0.2)',
                            'rgba(255, 99, 132, 0.2)',
                            'rgba(54, 162, 235, 0.2)',
                            'rgba(255, 206, 86, 0.2)',
                            'rgba(75, 192, 192, 0.2)'
                        ],
                        borderColor: [
                            'rgba(255, 99, 132, 1)',
                            'rgba(54, 162, 235, 1)',
                            'rgba(255, 206, 86, 1)',
                            'rgba(75, 192, 192, 1)',
                            'rgba(153, 102, 255, 1)',
                            'rgba(255, 159, 64, 1)',
                            'rgba(255, 99, 132, 1)',
                            'rgba(54, 162, 235, 1)',
                            'rgba(255, 206, 86, 1)',
                            'rgba(75, 192, 192, 1)'
                        ],
                        borderWidth: 1
                    }]
                },
                options: {
                    scales: {
                        yAxes: [{
                            ticks: {
                                beginAtZero: true
                            }
                        }]
                    }
                }
            });
        },

        change_chart(value) {
            if (value == 'Час') {
                axios.post('http://127.0.0.1:8000/message/dashboard/hour/', {
                    hour: 19,
                    day: 21,
                    month: 7,
                    year: 2020
                }).then((response)=>{
                    let i = null
                    this.chart_data = []
                    this.labels = []
                    for (i in response.data) {
                        this.labels.push(i)
                        this.chart_data.push(response.data[i])
                    }
                })                
            }

            if (value == 'День') {
                axios.post('http://127.0.0.1:8000/message/dashboard/day/', {
                    day: 21,
                    month: 7,
                    year: 2020
                }).then((response)=>{
                    let i = null
                    this.chart_data = []
                    this.labels = []
                    for (i in response.data) {
                        this.labels.push(i)
                        this.chart_data.push(response.data[i])
                    }
                })                
            }

            if (value == 'Месяц') {
                axios.post('http://127.0.0.1:8000/message/dashboard/month/', {
                    month: 7,
                    year: 2020
                }).then((response)=>{
                    let i = null
                    this.chart_data = []
                    this.labels = []
                    for (i in response.data) {
                        this.labels.push(i)
                        this.chart_data.push(response.data[i])
                    }
                })                
            }

            if (value == 'Год') {
                axios.post('http://127.0.0.1:8000/message/dashboard/year/', {
                    year: 2020
                }).then((response)=>{
                    let i = null
                    this.chart_data = []
                    this.labels = []
                    for (i in response.data) {
                        this.labels.push(i)
                        this.chart_data.push(response.data[i])
                    }
                })                
            }
        }
    },

    mounted: function() {
        this.change_chart(this.cur_chart);
        this.draw_chart();
    }
}
</script>