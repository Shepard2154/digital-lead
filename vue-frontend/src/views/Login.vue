<template>
  <v-card elevation="2" style="width: 500px; height: wrap-content;" class="my-5">
    <div class="p-3">
      
      <p style="
      font-family: Century Gothic;
      font-style: normal;
      font-weight: bold;
      font-size: 35px;
      line-height: 43px;
      text-align: center;
      color: #27646A;
      text-transform: uppercase;">Авторизация</p>

      <v-text-field
        v-model="phone"
        label="Логин"
        type="phone"
        required
      ></v-text-field>

      <v-text-field
        v-model="password"
        label="Пароль"
        type="password"
        required
      ></v-text-field>

      <v-btn
        :disabled="!valid"
        color="#27646A"
        @click="signin"
        class="mt-3 but"
        block
        large
      >
        Войти
      </v-btn>

      <v-btn
        :disabled="!valid"
        color="#F58D8E"
        @click="goto" 
        class="mt-3 but"
        block
        large
      >
        Зарегестрироваться
      </v-btn>

    </div>

    <v-row justify="space-around"  class="d-flex align-items-center" style="
    width: 300px;
    margin: 20px auto 20px;">
      <v-btn
          fab
          dark
          style="width: 36px; height: 36px"
          elevation="0"
          color="#27646A"
        >
        <v-icon dark>mdi-google</v-icon>
      </v-btn>

      <v-icon
        x-large
        color="#27646A"
      >mdi-facebook</v-icon>

      <v-icon
        x-large
        color="#27646A"
      >mdi-vk</v-icon>
    </v-row>
  </v-card> 
</template>

<script>

  export default {
    data: () => ({
      valid: true,
      password: null,
      phone: null,
      passwordRules: [
        v => !!v || 'Пароль не может быть пустым',
        v => (v && v.length > 10) || `Пароль должен быть длиннее 10 символов, а сейчас ${v.length}`,
      ],
    }),

    methods: {
      goto() {
        this.$router.push('/signup/')
      },

      signin() {
          fetch(
            `http://127.0.0.1:8000/auth/token/login/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    username: this.phone,
                    password: this.password
                })
            }
          ).then(response => {
              response.json().then(response => {
                  const token = response.auth_token
                  console.log(token)
                  this.$router.push('/main')
              })
          })
      },

      validate () {
        if (this.$refs.form.validate()){
          this.$router.push('/main')
        }
      },

      reset () {
        this.$refs.form.reset()
      }
    }
  }
</script>

<style scoped>
.but {
  font-family: Century Gothic;
  font-style: normal;
  font-weight: bold;
  font-size: 15px;
  line-height: 43px;
  text-align: center;
  color: white;
  text-transform: uppercase;
}
</style>