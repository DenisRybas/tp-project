<template>
  <p v-show="error" class="text-sm text-red-500">{{ errorMsg }}</p>
  <form class="modal1" @submit.prevent="submitHandler">
    <div class="card-content">
      <h2>
        <img src="img/logo.png" alt="" width="50" height="50">
        <span class="card-title">Awareness</span>
      </h2>
      <div class="input-field">
        <input
            id="email"
            type="email"
            v-model.trim="email"
            placeholder="email"
            required
        >
      </div>
      <div class="input-field">
        <input
            id="password"
            type="password"
            v-model.trim="password"
            placeholder="пароль"
            pattern="^[a-zA-Z0-9]{5,}$" title="Must contain 5 or more characters" required
        >
      </div>
      <div class="input-field">
        <input
            id="name"
            type="text"
            v-model.trim="name"
            placeholder="имя"
            pattern="^[a-zA-Z0-9]+" title="Must contain only letters or numbers" required
        >

      </div>
      <p>
        <input type="checkbox" value="subscribed_on_daily_phrase" v-model="agree">
        <label>Подписка на фразу дня</label>
      </p>
    </div>
    <div class="card-action">
      <div>
        <button class="btn waves-effect waves-light auth-submit" type="submit">
          <a class="w-100 btn btn btn-secondary text-light " style="color: white !important">Зарегистрироваться</a>
        </button>
      </div>

      <p class="center">
        Уже есть аккаунт?
        <router-link to="/login">Войти!</router-link>
      </p>
    </div>
  </form>
</template>

<script>
import axios from "axios";

export default {
  name: 'register',
  data: () => ({
    email: '',
    password: '',
    name: '',
    agree: false,
    error: false,
    errorMsg: `An error occurred, please try again`
  }),
  methods: {
    async submitHandler() {
      let formData = {
        email: this.email,
        password: this.password,
        username: this.name,
        subscribed_on_daily_phrase: this.agree
      }
      axios.post('http://127.0.0.1:8000/register', formData)// исправить в зависисмости от url
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
