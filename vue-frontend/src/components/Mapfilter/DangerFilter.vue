<template>
    <div class="map-filter">
    <br>
    <v-card
    class="mx-auto for-filter"
    max-width="344"
    outlined
    >
    <h4>Фильтр по классу опасности</h4>
      <v-checkbox
        v-model="colors"
        label="Высокий уровень опасности"
        color="red"
        value="red"
        hide-details
      ></v-checkbox>

      <v-checkbox
        v-model="colors"
        label="Средний уровень опасности"
        color="blue"
        value="blue"
        hide-details
      ></v-checkbox>

      <v-checkbox
        v-model="colors"
        label="Низкий уровень опасности"
        color="yellow"
        value="yellow"
        hide-details
      ></v-checkbox>
    </v-card>
  </div>
</template>

<script>
export default {
    data () {
    return {
      colors: ['red', 'indigo', 'orange', 'primary', 'secondary', 'success', 'info', 'warning', 'error', 'red darken-3', 'indigo darken-3', 'orange darken-3', 'yellow', 'blue'],
    }
  },
}
</script>

<style scoped>
  .for-filter{
    padding: 10px 10px;
    margin-left: 100px;
  }
</style>