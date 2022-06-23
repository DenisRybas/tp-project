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
              v-model="email"
              placeholder="email"
              required>
        </div>
        <div class="input-container ic2">
          <input
              class="input"
              id="password"
              type="password" v-model="password"
              pattern="^[a-zA-Z0-9]{5,}$"
              placeholder="пароль"
              title="Must contain 5 or more characters" required
          >
        </div>
      </div>
      <div>
        <button type="submit" class="btn waves-effect waves-light auth-submit ic2"><span
            class="w-100 btn btn btn-secondary text-light " style="color: white !important">Войти</span>
        </button>
      </div>

      <p class="center ic2">
        Нет аккаунта?
        <router-link to="/registration"><a>Зарегистрироваться</a></router-link>
      </p>
    </div>
  </form>
</template>

<script>

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
      // axios.post('https://eternal-awareness.herokuapp.com/login', formData)// исправить в зависисмости от url
      //     .then(function (response) {
      //       this.loggedIn = true;
      //     })
      //     .catch(function (error) {
      //       console.log(error);
      //     });
      // console.log(formData)

      let code = await this.$store
          .dispatch('login', {
            email: this.email,
            password: this.password
          })
      if (code === 417) {
        await this.$swal.fire({
          scrollbarPadding: false,
          title: 'Ошибка',
          text: 'Такой пользователь не зарегистирован или введён неверный пароль'
        });
        return
      }
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