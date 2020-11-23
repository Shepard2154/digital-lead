<template>
<div>
    <br>
    <v-date-picker
    v-model="months"
    type="month"
    multiple
    width="400px"
    ></v-date-picker>

    <v-menu
        ref="menu"
        v-model="menu"
        :close-on-content-click="false"
        :return-value.sync="months"
        transition="scale-transition"
        offset-y
        min-width="290px"
      >
        <template v-slot:activator="{ on, attrs }">
          <v-combobox
            v-model="months"
            multiple
            chips
            small-chips
            label="Выбранные месяцы"
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
        months: [],
        menu: true
  }),
  computed: {
    dateRangeText () {
      console.log(this.months)
      return this.months.join(' - ')
    }
  }
}
</script>

<style scoped>
    .dataLine{
        width: 400px;
    }
</style>