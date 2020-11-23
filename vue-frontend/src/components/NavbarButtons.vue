<template>
    <div class="text-center navbuttons">
    
    <v-btn
      class="ma-2"
      outlined
      color="white"
      v-for="navButton in navButtons"
      :key="navButton.title"
      @click="pressedNavButton(navButton.url)"
    >
      {{ navButton.title }}
    </v-btn>

    </div>
</template>

<style scoped>
    .navbuttons {
        margin-top: 30px;
        margin-left: 225px;
    }
</style>

<script>
export default {
    data:  () => ({
        navButtons: [
          {title: 'Статистика', url: '/statistics'},
          {title: 'Отчеты', url: '/reports'},
          {title: 'Карта', url: '/'}
        ]
    }),
    methods: {
      pressedNavButton(navUrl) {
        this.$router.push(navUrl)
      }
    }
}
</script>