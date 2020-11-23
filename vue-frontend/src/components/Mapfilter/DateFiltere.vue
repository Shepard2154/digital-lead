<template>
    <div class="map-filter">
        <v-card
        class="mx-auto for-filter"
        max-width="344"
        outlined>
        <h4>Фильтр по дате/времени</h4>
        <v-text-field
          v-model="dateRangeText"
          label="Выберите даты"
          prepend-icon="mdi-calendar"
          placeholder="2020-11-01 ~ 2020-11-20"
        ></v-text-field>
        <v-dialog
          ref="dialog"
          v-model="modal2"
          :return-value.sync="time"
          persistent
          width="290px"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-text-field
              v-model="time"
              label="Выберите временной диапазон"
              prepend-icon="mdi-clock-time-four-outline"
              readonly
              v-bind="attrs"
              v-on="on"
            ></v-text-field>
          </template>
          <v-time-picker
            v-if="modal2"
            v-model="time"
            full-width
          >
            <v-spacer></v-spacer>
            <v-btn
              text
              color="primary"
              @click="modal2 = false"
            >
              Cancel
            </v-btn>
            <v-btn
              text
              color="primary"
              @click="$refs.dialog.save(time)"
            >
              OK
            </v-btn>
          </v-time-picker>
        </v-dialog>
        </v-card>
    </div>
</template>

<script>
export default {
    data: () => ({
    dates: ['2020-11-01', '2020-11-20'],
    time: null,
    menu2: false,
    modal2: false,
  }),
  computed: {
    dateRangeText () {
      return this.dates.join(' ~ ')
    }
  }
}
</script>

<style scoped>
  .for-filter{
    padding: 10px 10px;
  }
</style>