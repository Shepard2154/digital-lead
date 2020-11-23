<template>
    <div class="map-filter">
        <v-card
        class="mx-auto for-filter"
        max-width="344"
        outlined>
        <h4>Фильтр по классу событий</h4>
            <div class="text-center">
               <v-checkbox
        v-model="colors"
        label="Пожар"
        color="primary"
        value="prymary1"
        hide-details
      ></v-checkbox>

      <v-checkbox
        v-model="colors"
        label="ДТП"
        color="primary"
        value="primary2"
        hide-details
      ></v-checkbox>

      <v-checkbox
        v-model="colors"
        label="Отключение горячей воды"
        color="primary"
        value="primary3"
        hide-details
      ></v-checkbox>
            </div>
        </v-card>
    </div>
</template>

<script>
import {mapGetters, mapMutations} from 'vuex'

export default {
  data () {
    return {
      colors: ['red', 'indigo', 'orange', 'primary', 'secondary', 'success', 'info', 'warning', 'error', 'red darken-3', 'indigo darken-3', 'orange darken-3', 'yellow', 'blue'],
    }
  },
  computed: {
      ...mapGetters(["getAllMessages"])
  },

  methods: {
      ...mapMutations(["updateMessages"])
  }
}
</script>

<style scoped>
  .for-filter{
    padding: 10px 10px;
  }

  
</style>