<template>
  <div class="container col-xxl-8 px-2 py-2 bg-white" @submit.prevent="submitHandler">
    <h2 class="benefits__title">
      <img src="img/svg/Vector.png" alt="Diary of templates:" class="benefits__card-thumb"> Техническая поддержка
      <form>
        <h2 class="benefits__title_theme_templates">
          Обращение:
        </h2>
        <div class="input-field">
          <textarea v-model.trim="theme" placeholder="enter a few lines"></textarea>
        </div>
        <h2 class="benefits__title_theme_templates">
          Ответ технической поддержки:
        </h2>
        <div class="input-field">
          <textarea v-model.trim="answer" placeholder="enter a few lines"></textarea>
        </div>
      </form>
      <div class="buttons">
        <li class="nav-item me-2 mb-2 mb-lg-0 text-center">
          <a class="w-100 btn btn btn-secondary text-light " style="color: white !important">
            <router-link to="/my_appeals">Вернуться</router-link>
          </a>
        </li>
      </div>
    </h2>
  </div>
</template>
<script>
import axios from "axios";

export default {
  name: "MyAppealsId",
  data: () => ({
    answer: '',
    theme: '',
  }),
  async created() {
// GET request using axios with async/await// исправить в зависисмости от url
    const response = await axios.get("http://127.0.0.1:8000/!!!/" + this.$route.params.id);
    this.theme = response.data["theme"];
    this.answer = response.data["answer"];
    console.log(this.answer)
  },
  methods: {},
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

li {
  list-style-type: none;
}

a {
  text-decoration: none; /* Убираем подчёркивание */
}
</style>
