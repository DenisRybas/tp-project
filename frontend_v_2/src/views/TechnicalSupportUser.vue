<template>
  <div class="container col-xxl-8 px-2 py-2 bg-white cursor" @submit.prevent="submitHandler">
    <form>
      <h2 class="ic1">
        Введите тему:
      </h2>
      <div class="ic1">
        <textarea class="theme" v-model.trim="title" placeholder="введите тему" required></textarea>
      </div>
      <h2 class="ic1">
        Введите содержиние:
      </h2>
      <div class="ic1">
        <textarea v-model.trim="content" placeholder="введите содержание" required></textarea>
      </div>
      <div class="buttons ic3">
        <button type="submit" class="floating-button">Отправить</button>
      </div>
    </form>

  </div>
</template>

<script>
import axios from "axios";

export default {
  name: 'TechnicalSupportUser',
  data: () => ({
    title: '',
    content: ''
  }),
  methods: {
    async submitHandler() {
      let formData = {
        title: this.title,
        content: this.content
      }
      await axios.post('https://eternal-awareness.herokuapp.com/technical_support_tickets/new', formData)// исправить в зависисмости от url
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
  font-size: 18px; /* Размер шрифта */
  resize: none;
}

textarea.theme {
  background: #f2f3f4;
  border: 2px solid #d0d0d0; /* Параметры рамки */
  padding: 10px; /* Поля */
  width: 100%; /* Ширина */
  height: 70px; /* Высота */
  box-sizing: border-box; /* Алгоритм расчёта ширины */
  font-size: 18px; /* Размер шрифта */
}

.cursor {
  cursor: default;
}

h2 {
  text-align: center
}

.ic3 {
  margin-top: 30px;
}

.ic1 {
  margin-top: 50px;
}
</style>