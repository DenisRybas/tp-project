<template>
  <div class="container col-xxl-8 px-2 py-2 bg-white">
    <h2 class="benefits__title">
      <form>
        <h2>{{ situation }}</h2>
        <h2>Варианты:</h2>
        <li v-for="answer in answers">
          <div class="card mb-3 shadow-lg ">
            <div class="card-body">
              <ul class="diary__title">
                <h4>Ответ: {{ answer.answer }}</h4>
                <h4>Объяснение: {{ answer.explanation }}</h4>
              </ul>
            </div>
          </div>
        </li>
        <h2>Предпочтительный ответ: {{ right_answer }}</h2>
        <h2>Ваш ответ: {{ user_answer }}</h2>
        <div class="buttons">
          <li class="nav-item me-2 mb-2 mb-lg-0 text-center">
            <a class="w-100 btn btn btn-secondary text-light " style="color: white !important">
              <router-link to="/viewing_diary_situations">Вернуться</router-link>
            </a>
          </li>
        </div>
      </form>

    </h2>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "ViewingDiarySituationsId",
  data: () => ({
    answers: [],
    situation: '',
    right_answer: '',
  }),
  async created() {
// GET request using axios with async/await// исправить в зависисмости от url
    const response = await axios.get("http://127.0.0.1:8000/situation_diaries/" + this.$route.params.id);
    this.answers = response.data["answers"];
    this.situation = response.data["situation"];
    this.right_answer = response.data["preferred_answer"];
    this.user_answer = response.data["user_answer"];
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

h4 {
  margin-left: 30px;
}
</style>