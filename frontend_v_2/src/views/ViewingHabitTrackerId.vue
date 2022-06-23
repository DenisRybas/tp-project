<template>
  <div class="container col-xxl-8 px-2 py-2 cursor bg-white">
      <form>
        <h1 class="ic1">
          Привычка: {{ habit }}
        </h1>
          <h3 class="ic3">
            Привычка ведётся с: {{ count }}
          </h3>
        <div class="buttons ic3">
          <router-link class="btn btn-outline-dark text-center" to="/viewing_habit_tracker">Вернуться</router-link>
        </div>
      </form>

  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "ViewingHabitTrackerId",
  data: () => ({
    habit: '',
    count: '',
  }),
  async created() {
// GET request using axios with async/await// исправить в зависисмости от url
    const response = await axios.get("https://eternal-awareness.herokuapp.com/habit_tracker/" + this.$route.params.id);
    this.habit = response.data["habit_name"];
    this.count = response.data["date_started"];
    console.log(this.count)
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
  text-align: center
}

li {
  list-style-type: none;
}

a {
  text-decoration: none; /* Убираем подчёркивание */
}

h3 {
  font-weight: normal;
}

.cursor {
  cursor: default;
}

.ic3 {
  margin-top: 50px;
}

.ic1 {
  margin-top: 50px;
  text-align: center;
}

</style>




