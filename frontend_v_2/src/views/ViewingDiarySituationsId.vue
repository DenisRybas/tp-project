<template>
  <div class="container col-xxl-8 px-2 py-2 cursor bg-white">
    <h2 class="benefits__title_theme_templates">
      <form>
        <h1>{{ situation }}</h1>
        <li v-for="answer in answers">
          <div class="card mb-3 shadow-lg ic1">
            <div class="card-body">
              <ul class="diary__title">
                <p>Ответ: {{ answer.answer }}</p>
                <p>Объяснение: {{ answer.explanation }}</p>
              </ul>
            </div>
          </div>
        </li>
        <h4 class="ic3">Предпочтительный ответ: {{ right_answer }}</h4>
        <h4 class="ic3">Ваш ответ: {{ user_answer }}</h4>
        <div class="buttons">
          <router-link class="btn btn-outline-dark text-center" to="/viewing_diary_situations">Вернуться</router-link>
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
    const response = await axios.get("https://eternal-awareness.herokuapp.com/situation_diaries/" + this.$route.params.id);
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
  font-size: 18px; /* Размер шрифта */
  resize: none;
}

h2 {
  text-align: left;
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

p {
  text-align: left;
}

.ic3 {
  margin-top: 10px;
}

.ic1 {
  margin-top: 50px;
}

.cursor {
  cursor: default;
}

</style>