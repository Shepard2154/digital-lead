<template>
    <div>
        <div class="filter-block">
            <span class="first-header-filter">Район</span>
            <span class="header-filter">Дата</span>
            <span class="header-filter">Объект возникновения проблемы</span>
        </div>
        <v-row class="autocomplete-block">
            <v-autocomplete class="autocomplete-item" 
            :items="districts"
            v-model="used[0]"
            ></v-autocomplete>

            <v-autocomplete class="autocomplete-item" 
            :items="date"
            v-model="used[1]"
            ></v-autocomplete>

            <v-autocomplete class="autocomplete-item" 
            :items="classes"
            v-model="used[2]"
            ></v-autocomplete>
        </v-row>            
        <v-row>
        <Map :isNeedRefresh="isNeedRefresh" :dynamicFilter="filter" @refreshed="isNeedRefresh = false" @for-autocomplete="getData" />
        </v-row>
    </div>
</template>

<script>
import Map from '../components/Map'


export default {
    components: {
        Map
    },
    data: () => ({
        districts: [
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
        date: [],
        eventClass: [],
        used: [false, false, false],
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
        filter: [],
        isNeedRefresh: false
    }),
    methods: {
        getData(filter){
            for(let i=0; i<filter.length;i++){
                if (filter[i]["district"]){
                    this.districts.push(filter[i]["district"])
                }
                    this.date.push(filter[i]["date"])

                    this.eventClass.push(filter[i]["event_class"])
            }
        }
    },
    watch: {
        used: function(newUsed, oldUsed){   
                this.isNeedRefresh = true

                this.filter = []

                let uniqueDistrict = []
                let uniqueDate = []
                let uniqueEventClass = []

                if (newUsed[0]) uniqueDistrict = newUsed[0]
                if (newUsed[1]) uniqueDate = newUsed[1]
                if (newUsed[2]) uniqueEventClass = newUsed[2]
                
                

                this.filter.push(uniqueDistrict, uniqueDate, uniqueEventClass)
        }
    }
}
</script>


<style scoped>
    .first-header-filter{
        margin-left: 60px;
    }
    .header-filter{
        margin-left: 350px;
    }
    .first-header-filter, .header-filter{
        font-family: Century Gothic;
        font-style: normal;
        font-weight: normal;
        font-size: 20px;
        line-height: 25px;
    }
    .filter-block{
        margin-top: 50px;
    }
    .autocomplete-block{
        margin-left: 60px;
        margin-bottom: 30px;
    }
    .autocomplete-item{
        margin-right: 100px;
        max-width: 300px;
    }
</style>

