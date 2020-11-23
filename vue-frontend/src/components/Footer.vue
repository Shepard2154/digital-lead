<template>
    <v-footer
      dark
      padless
      style="position: absolute; bottom:0; width: 100%"
    >
      <v-card
        class="flex"
        flat
      >
        <v-card color="#27646A">
          <v-card-title></v-card-title>
        </v-card>
    
        <v-card-text class="py-2 white--text text-center">
          {{ new Date().getFullYear() }} — <strong>Mozhayka Team</strong>
        </v-card-text>
      </v-card>
    </v-footer>
</template>

<script>
</script>