<template>
  <div class="container col-xxl-8 px-2 py-2 cursor bg-white">
      <form>
        <h2 class="ic3">
          {{ theme }}
        </h2>
        <div class="input-field ic1">
          <textarea disabled=""> {{ answer }}</textarea>
        </div>
        <div class="buttons ic1">
              <router-link class="btn btn-outline-dark text-center" to="/viewing_diary_templates">Вернуться</router-link>
        </div>
      </form>

  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "ViewingDiaryTemplatesId",
  data: () => ({
    answer: '',
    theme: '',
  }),
  async created() {
// GET request using axios with async/await// исправить в зависисмости от url
    const response = await axios.get("https://eternal-awareness.herokuapp.com/template_diaries/"+this.$route.params.id);
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
  font-size: 18px; /* Размер шрифта */
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

.ic3 {
  margin-top: 30px;
}

.ic1 {
  margin-top: 50px;
}

.cursor {
  cursor: default;
}

</style>