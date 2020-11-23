<template>
  <div class="my-app">
    
    <D3BarChart
      :config="chart_config"
      :datum="to_chart"
    ></D3BarChart>
    

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
    import { D3BarChart } from 'vue-d3-charts';

    export default {
        name: 'chart',
        

        components: {
            D3BarChart,
        },

        data() {
            return {
                to_chart: [
                    {"messages":7, "year":0},
                    {"messages":12, "year":5},
                    {"messages":1, "year":10},
                    {"year":15, "messages":5},
                    {"year":20,"messages":1},
                    {"year":25,"messages":1},
                    {"year":30,"messages":2},
                    {"year":35,"messages":2},
                    {"year":40,"messages":0},
                    {"year":45,"messages":1},
                    {"year":50,"messages":1},
                    {"year":55,"messages":1}
                ],
                chart_config: {
                    key: 'year',
                    values: ['messages']
                },
                count: 2010,
                resp: null,
                cur_chart: 'Час'
            }
        },

        watch: {
            cur_chart: function(val) {
                this.change_chart(val);
                this.datum = this.to_chart
            }
        },

        methods: {
            color(val) {
                if (this.cur_chart == val) return "success"
                else return 'primary'
            },

            change_chart(value) {
                if (value === 'Час') {
                    axios.post('http://127.0.0.1:8000/message/dashboard/hour/', {
                        hour: 19,
                        day: 21,
                        month: 7,
                        year: 2020
                    }).then((response)=>{
                        this.resp = null
                        Vue.set(this.$data, 'resp', response.data)
                        let i = null
                        this.to_chart = []
                        for (i in this.resp) {
                            this.to_chart.push({
                                messages: this.resp[i],
                                year: i
                            })
                        }
                    })
                }

                if (value === 'День') {
                    axios.post('http://127.0.0.1:8000/message/dashboard/day/', {
                        day: 21,
                        month: 7,
                        year: 2020
                    }).then((response)=>{
                        this.resp = null
                        Vue.set(this.$data, 'resp', response.data)
                        let i = null
                        this.to_chart = []
                        for (i in this.resp) {
                            this.to_chart.push({
                                messages: this.resp[i],
                                year: i
                            })
                        }
                    })
                }

                if (value === 'Месяц') {
                    axios.post('http://127.0.0.1:8000/message/dashboard/month/', {
                        month: 7,
                        year: 2020
                    }).then((response)=>{
                        this.resp = null
                        Vue.set(this.$data, 'resp', response.data)
                        let i = null
                        this.to_chart = []
                        for (i in this.resp) {
                            this.to_chart.push({
                                messages: this.resp[i],
                                year: i
                            })
                        }
                    })
                }
                
                if (value=='Год') {
                    axios.post('http://127.0.0.1:8000/message/dashboard/year/', {
                        year: 2020
                    }).then((response)=>{
                        this.resp = null
                        Vue.set(this.$data, 'resp', response.data)
                        let i = null
                        this.to_chart = []
                        for (i in this.resp) {
                            this.to_chart.push({
                                messages: this.resp[i],
                                year: i
                            })
                        }
                    })
                }
        }
}
}
</script>
