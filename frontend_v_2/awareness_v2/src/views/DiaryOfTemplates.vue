<template>
  <div class="container col-xxl-8 px-2 py-2 bg-white" @submit.prevent="submitHandler">
    <h2 class="benefits__title">
      <!--      <img src="img/svg/Vector.png" alt="Diary of templates:" class="benefits__card-thumb"> -->
      <h2>Дневник по шаблону</h2>
      <form>
        <h2 class="benefits__title_theme_templates" v-if="!loggedIn">
          Что для Вас счастье?
        </h2>
          <h2 class="benefits__title_theme_templates" v-else-if="loggedIn">
            {{ theme }}
          </h2>

        <div class="input-field">
          <textarea v-model.trim="answer" placeholder="введите несколько строчек"></textarea>
        </div>
        <div class="buttons">
          <button type="submit" class="floating-button">Сохранить</button>
        </div>
      </form>

    </h2>
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
    const response = await axios.get("http://127.0.0.1:8000/template_diaries/new");
    this.theme = response.data["theme"];
  },
  methods: {
    async submitHandler() {
      let formData = {
        theme: this.theme,
        answer: this.answer
      }
      axios.post('http://127.0.0.1:8000/template_diaries/new', formData)// исправить в зависисмости от url
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
  height: 200px; /* Высота */
  box-sizing: border-box; /* Алгоритм расчёта ширины */
  font-size: 14px; /* Размер шрифта */
}

h2 {
  text-align: center
}
</style>