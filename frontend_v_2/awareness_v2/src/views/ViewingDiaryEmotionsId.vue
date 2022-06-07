<template>
  <div class="container col-xxl-8 px-2 py-2 bg-white">
    <h2 class="benefits__title">
      <h2>Дневник эмоций за {{date}}</h2>
      <form>
        <h2>Эмоции</h2>
        <li v-for="emotion in emotions">
          <div class="card mb-3 shadow-lg ">
            <div class="card-body">
              <ul class="diary__title">
                <h4>{{ emotion }}</h4>
              </ul>
            </div>
          </div>
        </li>
        <h2>Действия</h2>
        <li v-for="action in actions">
          <div class="card mb-3 shadow-lg ">
            <div class="card-body">
              <ul class="diary__title">
                <h4>{{ action }}</h4>
              </ul>
            </div>
          </div>
        </li>
        <div class="buttons">
          <li class="nav-item me-2 mb-2 mb-lg-0 text-center">
            <h2>Оценка дня: {{day_rate}} из 5 баллов</h2>

            <a class="w-100 btn btn btn-secondary text-light " style="color: white !important">

              <router-link to="/viewing_diary_emotions">Вернуться</router-link>
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
  name: "ViewingDiaryEmotionsId",
  data: () => ({
    emotions: [],
    actions: [],
    day_rate: 5,
    date: ''
  }),
  async created() {
// GET request using axios with async/await// исправить в зависисмости от url
    const response = await axios.get("http://127.0.0.1:8000/emotion_diaries/" + this.$route.params.id);
    let emotions = response.data["emotions"];
    emotions = emotions.filter(function (value, index, array) {
      return array.indexOf(value) === index;
    });
    this.emotions = emotions;

    let actions = response.data["actions"];
    actions = actions.filter(function (value, index, array) {
      return array.indexOf(value) === index;
    });
    console.log(actions)
    this.actions = actions;

    this.day_rate = response.data['day_rate']
    this.date = response.data['date']
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
No file chosen
Ещё









