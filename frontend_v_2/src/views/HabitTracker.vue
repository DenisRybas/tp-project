<template>
  <div class="container col-xxl-8 px-2 py-2 ic2 cursor bg-white" @submit.prevent="submitHandler">
      <form>
        <h2 class="ic3">Добавление новой привычки</h2>
        <div class="input-field ic1" >
          <textarea v-model.trim="habit" placeholder="Введите название привычки" required v-if="loggedIn"></textarea>
          <textarea v-model.trim="habit" placeholder="Введите название привычки" v-if="!loggedIn"></textarea>
        </div>
        <div class="buttons ic1">
          <button type="submit" class="floating-button" v-if="loggedIn">Сохранить</button>
        </div>
        <div class="buttons ic1">
          <button type="submit" class="floating-button" v-if="!loggedIn">Вернуться обратно</button>
        </div>
      </form>

  </div>
</template>

<script>
import axios from "axios";

import {authComputed} from '@/store/helpers'

export default {
  name: 'HabitTracker',
  data: () => ({
    habit: '',
  }),
  computed: {
    ...authComputed
  },
  methods: {
    async submitHandler() {
      let formData = {
        habit_name: this.habit
      }
      axios.post('https://eternal-awareness.herokuapp.com/habit_tracker/new', formData)// исправить в зависисмости от url
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

h2 {
  text-align: center
}

.cursor {
  cursor: default;
}

.ic1 {
  margin-top: 50px;
}
.ic3 {
  margin-top: 30px;
}
.ic2 {
  margin-top: 10vh;
}
</style>
