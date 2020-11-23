<template>
    <div>
        <br>
        <v-row>
            <v-col cols="4">
                <yandex-map  id="map"
                    :settings="settings"
                    :coords="mapCenter"
                    :zoom="10" 
                    :use-object-manager="true"
                    :controls="['zoomControl']"
                    @map-was-initialized="getMapInstance"
                >
                </yandex-map>
            </v-col>
            <v-col cols="6" class="p-2 pr-7 report-col">
                <report class="report-msg" :isLikable="true" v-for="(i, index) in reports" :key="index" :data="i"/>
            </v-col>
        </v-row>
        <br>
    </div>
</template>

<script>
    import { yandexMap, ymapMarker } from 'vue-yandex-maps'
    import Report from '../components/report.vue'

    export default{
        props: ["isNeedRefresh", "dynamicFilter"],
        components: {
            yandexMap, 
            ymapMarker,
            Report
        },

        data: () => ({
            settings: {
                apiKey: 'e70694c3-ce7f-4459-b7f6-be3d53e2cc8e',
                lang: 'ru_RU',
                coordorder: 'latlong',
                version: '2.1'
            },

            mapCenter: [59.9370, 30.3089],
            isShow: false,
            filter: [],
            currentMap: null,
            objectManager: null,
            placemarks: [],

            classifier: {
                1: 'yellow',
                2: 'blue',
                3: 'red'
            },
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
            reports: [],
        }),

        methods: {
            onClick(e){
                this.reports = []
                let target = e.get('objectId');

                if (this.objectManager.clusters.getById(target)) {
                    let objects = this.objectManager.clusters.getById(target).properties.geoObjects
                    objects.forEach(element => {
                        axios({
                            method: 'GET',
                            url: `http://127.0.0.1:8000/message/get/${element.id}/`
                        }).then(response => {
                            this.reports.push(response.data)
                        })
                    });
                }
                else {
                    axios({
                            method: 'GET',
                            url: `http://127.0.0.1:8000/message/get/${target}/`
                        }).then(response => {
                            this.reports.push(response.data)
                        })
                }
            },

            async getMapInstance(map) {
                if (map) {

                    axios({
                method: 'GET',
                url: 'http://127.0.0.1:8000/message/get/?date_before=2020-03-23T12:58:20.204316Z'
            }).then(response => {
                this.reports = response.data.data
                for (let i=0;i<this.reports.length;i++){
                    let mapMarker = {
                                    type: 'Feature',
                                    id: this.reports[i]["id"],
                                    geometry: {
                                        type: 'Point',
                                        coordinates: [this.reports[i]["address"]["latitude"], this.reports[i]["address"]["longtitude"]]
                                    },
                                    properties: {
                                        hintContent: this.reports[i]["date"],
                                        balloonContent: this.reports[i]["text"]
                                    },
                                    options: {
                                        preset: "islands#dotIcon",
                                        iconColor: this.classifier[this.reports[i]["danger_level"]]
                                    }
                    }
                    this.placemarks.push(mapMarker)
                    }

                    try {
                    this.currentMap = map
                    this.objectManager = new ymaps.ObjectManager({
                                clusterize: true,
                                gridSize: 32,
                                clusterDisableClickZoom: true
                            })
                        try {
                            this.objectManager.add(this.placemarks)
                            this.currentMap.geoObjects.add(this.objectManager)
                            this.currentMap.geoObjects.events.add('click', this.onClick)
                        } catch (error) {
                            console.log('no placemarks!')
                        }
                        
                } catch (error) {
                    console.log(error)
                }
                this.$emit('for-autocomplete', this.filter)
                })
            }
        }
    },

    watch: {
        isNeedRefresh: function(newIsNeedRefresh, oldIsNeedRefresh){
            if (newIsNeedRefresh){
                
                let myFilter = this.dynamicFilter
                let filteredPlacemarks = []
                
                if (myFilter[0].length == 0){
                    for(let i=0;i<this.filter.length;i++)
                    {
                        myFilter[0].push(this.filter[i]["district"])
                    }
                }

                if (myFilter[1].length == 0){
                    for(let i=0;i<this.filter.length;i++)
                    {
                        myFilter[1].push(this.filter[i]["date"])
                    }
                }

                if (myFilter[2].length == 0){
                    for(let i=0;i<this.filter.length;i++)
                    {
                        myFilter[2].push(this.filter[i]["event_class"])
                    }
                }

                // Предусмотреть повторный запрос на сервер или так и оставить из локальных данных
                for (let i=0;i<reports.length;i++){
                    if (myFilter[0].includes(reports[i].address["district"]) && 
                        myFilter[1].includes(reports[i]["date"]) &&
                        myFilter[2].includes(reports[i]["event_class"])){
                            console.log("here")
                        let mapMarker = {
                                        type: 'Feature',
                                        id: reports[i]["id"],
                                        geometry: {
                                            type: 'Point',
                                            coordinates: [reports[i]["address"]["latitude"], reports[i]["address"]["longtitude"]]
                                        },
                                        properties: {
                                            hintContent: reports[i]["date"],
                                            balloonContent: reports[i]["text"]
                                        },
                                        options: {
                                            preset: "islands#dotIcon",
                                            iconColor: this.classifier[reports[i]["danger_level"]]
                                        }
                        }
                        filteredPlacemarks.push(mapMarker)
                    }
                }

                //console.log("filteredPlacemarks", filteredPlacemarks)
                
                this.objectManager.removeAll()
                this.objectManager.add(filteredPlacemarks)
                
                this.$emit('refreshed')
            }
        },
    }
}
</script>

<style scoped>
    #map{
        width: 800px; 
        height: 800px;
        margin-left: 60px;
    }
    .report-col{
        margin-left: 300px;
    }
    .report-msg{
        margin-bottom: 30px;
    }
</style>
