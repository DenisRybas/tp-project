<template>
  <p v-show="error" class="text-sm text-red-500">{{ errorMsg }}</p>
  <form class="card auth-card" @submit.prevent="submitHandler">
    <div class="card-content">
      <span class="card-title">Awareness</span>
      <div class="input-field">
        <input
            id="email"
           type="email" v-model="email">
        <label for="email">Email</label>
      </div>
      <div class="input-field">
        <input
            id="password"
          type="password" v-model="password"
        >
        <label for="password">Пароль</label>
      </div>
    </div>
    <div class="card-action">
      <div>
        <button type="submit" :disabled="password.length < 3" class="btn waves-effect waves-light auth-submit">Войти
          <i class="material-icons right">send</i>
        </button>
      </div>

      <p class="center">
        Нет аккаунта?
        <router-link to="/register">Зарегистрироваться</router-link>
      </p>
    </div>
  </form>
</template>

<script>
    import axios from "axios";

    export default {
        name: 'login',
        data() {
            return {
                email: '',
                password: '',
                error: false,
                errorMsg: `An error occurred, please try again`
            }
        },
        methods: {
     async submitHandler() {
      let formData = {
        email: this.email,
        password: this.password
      }
     axios.post('/login', formData)// исправить в зависисмости от url
    .then(function (response) {
        console.log(response);
     })
     .catch(function (error) {
       console.log(error);
     });
      console.log(formData)

      await this.$router.push('/')
    },
  }
    }
</script>

<style scoped>
</style>