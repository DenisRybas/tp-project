<template>
  <div class="container col-xxl-8 px-2 py-2 ic2 bg-white cursor" @submit.prevent="submitHandler">
    <form>
      <h2 class="ic3" v-if="!loggedIn">
        Что для Вас счастье?
      </h2>
      <h2 class="ic3" v-else-if="loggedIn">
        {{ theme }}
      </h2>

      <div class="input-field ic1">
        <textarea v-model.trim="answer" placeholder="Введите несколько строчек" required v-if="loggedIn"></textarea>
        <textarea v-model.trim="answer" placeholder="Введите несколько строчек" v-if="!loggedIn"></textarea>
      </div>
      <div class="buttons ic1">
        <button type="submit" class="floating-button" v-if="loggedIn">Сохранить</button>
      </div>
      <div class="buttons ic1">
        <button type="submit" class="floating-button" v-if="!loggedIn">Вернуться обратно</button>
      </div>
    </form>

  </div>
</template>

<script>
import axios from "axios";

import {authComputed} from '@/store/helpers'

export default {
  name: 'diary_of_templates',
  data: () => ({
    answer: '',
    theme: '',
  }),
  computed: {
    ...authComputed
  },
  async created() {
    // GET request using axios with async/await// исправить в зависисмости от url
    const response = await axios.get("https://eternal-awareness.herokuapp.com/template_diaries/new");
    this.theme = response.data["theme"];
  },
  methods: {
    async submitHandler() {
      let formData = {
        theme: this.theme,
        answer: this.answer
      }
      await axios.post('https://eternal-awareness.herokuapp.com/template_diaries/new', formData)// исправить в зависисмости от url
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
textarea {
  background: #f2f3f4;
  border: 2px solid #d0d0d0; /* Параметры рамки */
  padding: 10px; /* Поля */
  width: 100%; /* Ширина */
  height: 400px; /* Высота */
  box-sizing: border-box; /* Алгоритм расчёта ширины */
  font-size: 18px; /* Размер шрифта */
  resize: none;
}

h2 {
  text-align: center;
}

.ic1 {
  margin-top: 50px;
}

.ic3 {
  margin-top: 30px;
}

.cursor {
  cursor: default;
}

.ic2 {
  margin-top: 10vh;
}
</style>