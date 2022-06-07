<template>
  <p v-show="error" class="text-sm text-red-500">{{ errorMsg }}</p>
    <form class="modal1" @submit.prevent="submitHandler">
      <div class="form-signin text-center mt-4">
        <div class="card-content">
          <span class="card-title">Awareness</span>
          <div class="input-field">
            <input
                id="email"
                type="email"
                v-model="email"
                placeholder="email"
                required>
          </div>
          <div class="input-field">
            <input
                id="password"
                type="password" v-model="password"
                pattern="^[a-zA-Z0-9]{5,}$"
                placeholder="пароль"
                title="Must contain 5 or more characters" required
            >
          </div>
        </div>
        <div class="card-action">
          <div>
            <button type="submit" class="btn waves-effect waves-light auth-submit"><a
                class="w-100 btn btn btn-secondary text-light " style="color: white !important">Войти</a>
            </button>
          </div>

          <p class="center">
            Нет аккаунта?
            <router-link to="/register">Зарегистрироваться</router-link>
          </p>
        </div>
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
      // axios.post('http://127.0.0.1:8000/login', formData)// исправить в зависисмости от url
      //     .then(function (response) {
      //       this.loggedIn = true;
      //     })
      //     .catch(function (error) {
      //       console.log(error);
      //     });
      // console.log(formData)

      this.$store
          .dispatch('login', {
            email: this.email,
            password: this.password
          })
      await this.$router.push('/')
    },
  }
}
</script>

<style scoped>
</style>