<template>
  <div class="container col-xxl-8 px-2 py-2 bg-white" @submit.prevent="submitHandler">
    <h2>Трекер привычек</h2>
    <h2 class="benefits__title">
      <form>
        <h2>Добавление новой привычки:</h2>
        <div class="input-field">
          <textarea v-model.trim="habit" placeholder="введите название привычки"></textarea>
        </div>
        <div class="buttons">
          <button type="submit" class="floating-button">Сохранить</button>
        </div>
      </form>

    </h2>
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
      axios.post('http://127.0.0.1:8000/habit_tracker/new', formData)// исправить в зависисмости от url
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
  font-size: 14px; /* Размер шрифта */
}

h2 {
  text-align: center
}
</style>
No file chosen
Ещё