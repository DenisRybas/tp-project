<template>
  <div class="container col-xxl-8 px-2 py-2 bg-white">
    <h2 class="benefits__title">
      <h2>Трекер привычек</h2>
      <form>
        <h2 class="benefits__title_theme_templates">
          Привычка: {{ habit }}
        </h2>
        <div class="input-field">
          <h2 class="benefits__title_theme_templates">
            Привычка ведётся с: {{ count }}
          </h2>
        </div>
        <div class="buttons">
          <li class="nav-item me-2 mb-2 mb-lg-0 text-center">
            <a class="w-40 btn btn btn-secondary text-light " style="color: white !important">
              <router-link to="/viewing_habit_tracker">Вернуться</router-link>
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
  name: "ViewingHabitTrackerId",
  data: () => ({
    habit: '',
    count: '',
  }),
  async created() {
// GET request using axios with async/await// исправить в зависисмости от url
    const response = await axios.get("http://127.0.0.1:8000/habit_tracker/" + this.$route.params.id);
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
No file chosen
Ещё



