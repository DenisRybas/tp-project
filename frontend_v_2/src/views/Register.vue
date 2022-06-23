<template>
  <p v-show="error" class="text-sm text-red-500">{{ errorMsg }}</p>
  <form class="form" @submit.prevent="submitHandler">
    <div class="form-signin text-center mt-4">

      <div class="card-content">
        <h2>
          <span class="title">Awareness</span>
        </h2>
        <div class="input-container ic1">
          <input
              class="input"
              id="email"
              type="email"
              v-model.trim="email"
              placeholder="email"
              required
          >
        </div>
        <div class="input-container ic1">
          <input
              class="input"
              id="password"
              type="password"
              v-model.trim="password"
              placeholder="пароль"
              pattern="^[a-zA-Z0-9]{5,}$" title="Must contain 5 or more characters" required
          >
        </div>
        <div class="input-container ic1">
          <input
              class="input"
              id="name"
              type="text"
              v-model.trim="name"
              placeholder="имя"
              pattern="^[a-zA-Z0-9]+" title="Must contain only letters or numbers" required
          >

        </div>
        <p class="center ic1">
          <input type="checkbox" value="subscribed_on_daily_phrase" v-model="agree">
          <label>Подписка на фразу дня</label>
        </p>
      </div>
      <div>
        <button class="btn waves-effect waves-light auth-submit" type="submit">
          <span class="w-100 btn btn btn-secondary text-light "
                style="color: white !important">Зарегистрироваться</span>
        </button>
      </div>

      <p class="center ic1">
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
      let errcode = 0
      await axios.post('https://eternal-awareness.herokuapp.com/register', formData)// исправить в зависисмости от url
          .then(function (response) {
            errcode = response.data['code']
            console.log(response);
          })
          .catch(function (error) {
            console.log(error);
          });
      console.log(errcode)
      if (errcode === 417)
        await this.$swal.fire({
          scrollbarPadding: false,
          title: 'Ошибка',
          text: 'Такой пользователь уже зарегистрирован'
        });

      await this.$router.push('/')
    },
  }
}
</script>

<style scoped>
a {
  color: #4f73e8;
  text-decoration: none; /* Отменяем подчеркивание у ссылки */
}

a:hover {
  color: #4f73e8; /* Цвет ссылки при наведении */
  text-decoration: underline;
}

a:focus {
  outline: none;
}

.form {
  background-color: rgb(150, 162, 162);
  padding: 100px;
  position: fixed;
  top: 50%;
  left: 50%;
  -webkit-transform: translate(-50%, -50%);
  -ms-transform: translate(-50%, -50%);
  transform: translate(-50%, -50%);
}

.title {
  color: #eee;
  font-family: sans-serif;
  font-size: 36px;
  font-weight: 600;
  margin-top: 30px;
}

.subtitle {
  color: #eee;
  font-family: sans-serif;
  font-size: 16px;
  font-weight: 600;
  margin-top: 10px;
}

.input-container {
  height: 50px;
  position: relative;
  width: 100%;
}

.ic1 {
  margin-top: 20px;
}

.ic2 {
  margin-top: 20px;
}

.input {
  background-color: white;
  border-radius: 12px;
  border: 0;
  box-sizing: border-box;
  color: black;
  font-size: 18px;
  height: 100%;
  outline: 0;
  padding: 4px 20px 0;
  width: 100%;
}

.cut {
  background-color: #15172b;
  border-radius: 10px;
  height: 20px;
  left: 20px;
  position: absolute;
  top: -20px;
  transform: translateY(0);
  transition: transform 200ms;
  width: 76px;
}

.cut-short {
  width: 50px;
}

.input:focus ~ .cut,
.input:not(:placeholder-shown) ~ .cut {
  transform: translateY(8px);
}

.placeholder {
  color: #65657b;
  font-family: sans-serif;
  left: 20px;
  line-height: 14px;
  pointer-events: none;
  position: absolute;
  transform-origin: 0 50%;
  transition: transform 200ms, color 200ms;
  top: 20px;
}

.input:focus ~ .placeholder,
.input:not(:placeholder-shown) ~ .placeholder {
  transform: translateY(-30px) translateX(10px) scale(0.75);
}

.input:not(:placeholder-shown) ~ .placeholder {
  color: #808097;
}

.input:focus ~ .placeholder {
  color: #dc2f55;
}

.submit {
  background-color: #08d;
  border-radius: 12px;
  border: 0;
  box-sizing: border-box;
  color: #eee;
  cursor: pointer;
  font-size: 18px;
  height: 50px;
  margin-top: 38px;
  text-align: center;
  width: 100%;
}

.submit:active {
  background-color: #06b;
}

</style>
