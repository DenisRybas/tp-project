<template>
  <div class="container col-xxl-8 px-2 py-2 cursor bg-white">
    <h1 style="text-align: center">Дневник эмоций за {{ date }}</h1>
    <form>
      <h3>Эмоции:</h3>
      <li v-for="emotion in emotions">
        <ul>
          <p style="text-align: left; font-weight: normal">{{ emotion }}</p>
        </ul>
      </li>
      <h3>Действия:</h3>
      <li v-for="action in actions">
        <ul>
          <p style="text-align: left; font-weight: normal">{{ action }}</p>
        </ul>
      </li>
      <div class="buttons">
        <li class="nav-item me-2 mb-2 mb-lg-0 text-center">
          <h3 style="text-align: left">Оценка дня:</h3>
          <p style="text-align: left; margin-left: 76px"> {{ day_rate }} из 5 баллов</p>
          <router-link class="btn btn-outline-dark text-center" to="/viewing_diary_emotions">Вернуться
          </router-link>
        </li>
      </div>
    </form>
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
    const response = await axios.get("https://eternal-awareness.herokuapp.com/emotion_diaries/" + this.$route.params.id);
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

h3 {
  margin-left: 30px;
}

ul {
  display: list-item;
  list-style-type: "🤯";
  margin-left: 100px;
  padding-inline-start: 1ch;
}

.cursor {
  cursor: default;
}

</style>









