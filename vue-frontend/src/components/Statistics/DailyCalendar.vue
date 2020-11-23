<template>
<div>
    <br>
      <v-date-picker
        v-model="dates"
        multiple
        color="red"
        width="400px"
      ></v-date-picker>
      <v-menu
        ref="menu"
        v-model="menu"
        :close-on-content-click="false"
        :return-value.sync="dates"
        transition="scale-transition"
        offset-y
        min-width="290px"
      >
        <template v-slot:activator="{ on, attrs }">
          <v-combobox
            v-model="dates"
            multiple
            chips
            small-chips
            label="Выбранные даты"
            prepend-icon="mdi-calendar"
            readonly
            v-bind="attrs"
            v-on="on"
            class="dataLine"
          ></v-combobox>
        </template>
      </v-menu>
  <br>
</div>
</template>

<script>
export default {
    data: () => ({
      dates: [],
      menu: true,
  }),
  computed: {
    dateRangeText () {
      return this.dates.join(' - ')
    }
  },
  methods: {
    getDates(){
      console.log(this.dates)
    }
  }
}
</script>

<style scoped>
    .dataLine{
        width: 400px;
    }
</style>