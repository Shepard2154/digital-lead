<template>
    <div>
        <v-toolbar dark color="#27646A">

            <v-toolbar-title>
                <v-img
                    max-height="150"
                    max-width="250"
                    src="../assets/g_white.svg"
                    style="margin-top: 40px;"
                ></v-img>
            </v-toolbar-title>

            <v-spacer></v-spacer>

            <v-btn background-color="#27646A" text @click="logout()">
                    <v-icon>mdi-export</v-icon>
                    Выйти
            </v-btn>

            <template v-slot:extension>
                <v-tabs style="margin-left: 300px">
                        <v-tab v-for="(button, index) in menu_buttons" :key="`title-${index}`"
                        :to="{name: button.route}">
                            <v-icon left>
                                {{ button.icon }}
                            </v-icon>
                            {{ button.title }}
                        </v-tab>
                </v-tabs>
            </template>
        </v-toolbar>
    </div>
</template>

<style scoped>
    .no-link-decoration{
        text-decoration: none;
        color: white;
    }
    .toolbar-title{
        font-weight: 300;
        font-family: sans-serif;
        size: 6rem;
        letter-spacing: -.015625em;
        margin-bottom: 41px;
    }
</style>

<script>
import NavbarButtons from './NavbarButtons'

export default {
    name: 'Navbar',
    data: () => ({
      collapseOnScroll: false,
    }),
    computed: {
            menu_buttons() {
                return [
                    {
                        icon: null,
                        title: 'Все сообщения',
                        route: 'home'
                    },
                    {
                        icon: null,
                        title: 'Мои сообщения',
                        route: 'reports'
                    },
                    {
                        icon: null,
                        title: 'Статистика',
                        route: 'statistics'
                    },
                ]
            }
        },
    components: {
        NavbarButtons
    },
  methods: {
    logout(){
      this.$router.push({name: 'login'})
    }
  }
}
</script>