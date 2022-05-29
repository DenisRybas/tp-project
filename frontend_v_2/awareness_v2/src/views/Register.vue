<template>
  <form class="card auth-card" @submit.prevent="submitHandler">
    <div class="card-content">
      <span class="card-title">Awareness</span>
      <div class="input-field">
        <input
            id="email"
            type="text"
            v-model.trim="email"
        >
        <label for="email">Email</label>
      </div>
      <div class="input-field">
        <input
            id="password"
            type="password"
            v-model.trim="password"
        >
        <label for="password">Пароль</label>
        <small
        >
          Введите пароль
        </small>
      </div>
      <div class="input-field">
        <input
            id="name"
            type="text"
            v-model.trim="name"
        >

        <label for="name">Имя</label>
        <small
          class="helper-text invalid"
        >
          Введите ваше имя
        </small>
      </div>
      <p>
        <label>
          <input type="checkbox"  />
          <span>С правилами согласен</span>
        </label>
      </p>
    </div>
    <div class="card-action">
      <div>
        <button class="btn waves-effect waves-light auth-submit" type="submit">
          Зарегистрироваться
          <i class="material-icons right"></i>
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
import {email, required, minLength} from 'vuelidate/lib/validators'
import axios from "axios";

export default {
  name: 'register',
  data: () => ({
    email: '',
    password: '',
    name: '',
    agree: false
  }),
  methods: {
     async submitHandler() {
      let formData = {
        email: this.email,
        password: this.password,
        name: this.name
      }
     axios.post('/register', formData)// исправить в зависисмости от url
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
