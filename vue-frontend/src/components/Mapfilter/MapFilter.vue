<template>
  <div map-filter>
    <danger-filter />
    <br>
    <event-filter />
    <br>
    <date-filter />
  </div>
</template>

<script>
import DangerFilter from './DangerFilter'
import EventFilter from './EventFilter'
import DateFilter from './DateFiltere'

export default {
  components: {
    DangerFilter,
    EventFilter,
    DateFilter
  }
}
</script>

<style scoped>
  .map-filter{
    margin-left: 100px;
  }
</style>