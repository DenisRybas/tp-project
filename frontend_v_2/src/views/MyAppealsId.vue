<template>
  <div class="container col-xxl-8 px-2 py-2 bg-white cursor" @submit.prevent="submitHandler">
    <form>
      <h2 class="ic1">
        Обращение:
      </h2>
      <div class="input-field ic1">
        <textarea class="title" v-model.trim="title"></textarea>
      </div>
      <h2 class="ic1">
        Содержание:
      </h2>
      <div class="input-field ic1">
        <textarea v-model.trim="content"></textarea>
      </div>
    </form>
    <div class="buttons ic3">
      <router-link class="btn btn-outline-dark text-center" to="/my_appeals">Вернуться</router-link>
    </div>
  </div>
</template>
<script>
import axios from "axios";

export default {
  name: "MyAppealsId",
  data: () => ({
    title: '',
    content: '',
  }),
  async created() {
// GET request using axios with async/await// исправить в зависисмости от url
    const response = await axios.get("https://eternal-awareness.herokuapp.com/technical_support_tickets/" + this.$route.params.id);
    this.title = response.data["title"];
    this.content = response.data["content"];
    console.log(this.title)
    console.log(this.content)
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

.cursor {
  cursor: default;
}

textarea.title {
  background: #f2f3f4;
  border: 2px solid #d0d0d0; /* Параметры рамки */
  padding: 10px; /* Поля */
  width: 100%; /* Ширина */
  height: 70px; /* Высота */
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
</style>
