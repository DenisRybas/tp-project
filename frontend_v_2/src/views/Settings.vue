<template>
  <div class="container col-xxl-8 px-2 py-2 bg-white cursor">
    <div class="row flex-lg-row align-items-center g-0 py-5">
      <div class="text-center">
        <span class="display-5 lh-1 mb-3 ms-3"> {{ nickname }} </span>
      </div>
    </div>

    <div class="container-fluid pb-3">
      <div class="d-flex align-items-start">
        <div class="mt-2 nav ps-2 flex-column nav-pills me-3"
             aria-orientation="vertical">
          <a class="nav-link btn btn-lg remove-glow"
             aria-selected="false">
            <router-link class="a" to="/diary">Мои дневники</router-link>
          </a>
          <a class="w-100 btn btn-lg btn-secondary text-light"
             aria-selected="true">
            <router-link class="a" to="/settings">Настройки</router-link>
          </a>
        </div>
        <div class="d-flex flex-column flex-grow-1 ms-5">
          <div class="mb-3">
            <form method="post" @submit.prevent="submitHandler">
              <div class="mb-3 ic1">
                <label  class="form-label">{{ 'Новое имя' }}</label>
                <input
                    class="form-control"
                    type="text"
                    v-model.trim="nickname"
                    placeholder="имя"
                    pattern="^[a-zA-Z0-9]+" title="Must contain only letters or numbers"
                    id="name"
                    required
                >
              </div>
              <div class="mb-3 ic1">
                <label for="InputNewPassword" class="form-label">{{ 'Новый пароль' }}</label>
                <input type="password" name="new_password" minlength="8"
                       class="form-control remove-glow" id="InputNewPassword" v-model="password"
                       >
              </div>
              <button type="submit" name="password-change"
                      class="floating-button ic1">{{ 'Подтвердить' }}
              </button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Settings",
  data() {
    return {
      nickname: '',
      password: '',
      subscribed_on_daily_phrase: false,
      errorMsg: `An error occurred, please try again`
    }
  },
  async created() {
    // GET request using axios with async/await// исправить в зависисмости от url
    const response = await axios.get("https://eternal-awareness.herokuapp.com/edit_account");
    this.nickname = response.data["username"];
    this.subscribed_on_daily_phrase = response.data['subscribed_on_daily_phrase']
  },
  methods: {
    async submitHandler() {
      let formData = {
        username: this.nickname,
        password: this.password,
        subscribed_on_daily_phrase: this.subscribed_on_daily_phrase
      }
      await axios.post('https://eternal-awareness.herokuapp.com/edit_account', formData)// исправить в зависисмости от url
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
a {
  color: black;
  text-decoration: none; /* Отменяем подчеркивание у ссылки */
}

a:hover {
  color: #4f73e8; /* Цвет ссылки при наведении */
  cursor: pointer;
}

a:focus {
  outline: none;
}

.cursor {
  cursor: default;
}

.ic1 {
  margin-top: 30px;
}
</style>