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
        text-transform: uppercase;">Регистрация</p>

        <v-text-field
        v-model="firstname"
        label="Имя"
        type="text"
        required
        ></v-text-field>

        <v-text-field
        v-model="lastname"
        label="Фамилия"
        type="text"
        required
        ></v-text-field>

        <v-text-field
        v-model="mail"
        label="Почтовый ящик"
        type="email"
        required
        ></v-text-field>

        <v-text-field
            v-model="phone"
            label="Номер телефона"
            type="phone"
            required
        ></v-text-field>

        <v-text-field
            v-model="password"
            label="Пароль"
            type="password"
            required
        ></v-text-field>

        <v-text-field
            v-model="confirm_password"
            label="Повторите пароль"
            type="password"
            required
        ></v-text-field>

        <v-btn
            color="#F58D8E"
            @click="signUp"
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
      password: null,
      phone: null,
      mail: null,
      confirm_password: null,
      firstname: null,
      lastname: null,

      isCreated: false,
      error: []
    }),

    methods: {
        signUp() {
            fetch(
                `http://127.0.0.1:8000/auth/users/`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        username: this.firstname,
                        password: this.password,
                        email: this.email
                    })
                }
            ).then(response => {
                response.json().then(response => {
                    if (response.username === this.firstname) {
                        this.$router.go(-1)
                    }
                    else {
                        this.isCreateFault = true
                        this.error = response
                    }
                })
            })
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