<template>
  <div class="container col-xxl-8 px-2 py-2 cursor bg-white" @submit.prevent="submitHandler">
    <form>
      <h2 class="benefits__title_theme_templates">
        Выберите из списка эмоции и действия за сегодня:</h2>
      <h3>Эмоции</h3>
      <p class="ic1"></p>
      <div class="card mb-3 shadow-lg " v-if="!loggedIn">
        <div class="card-body">
          <ul class="diary__title">
            <label class="container" :for="`emotion_1`">
              <input type="checkbox" :id="`emotion_1`" :value="`Радость`"
                     name="user_interest"
                     class="check-highload"
                     v-model="selected_emotions">
              <span class="highload2"></span>
              <h4>Радость</h4>
            </label>
          </ul>
        </div>
      </div>
      <div class="card mb-3 shadow-lg " v-if="!loggedIn">
        <div class="card-body">
          <ul class="diary__title">
            <label class="container" :for="`emotion_2`">
              <input type="checkbox" :id="`emotion_2`" :value="`Грусть`"
                     name="user_interest"
                     class="check-highload"
                     v-model="selected_emotions">
              <span class="highload2"></span>
              <h4>Грусть</h4>
            </label>
          </ul>
        </div>
      </div>

      <li v-for="emotion in emotions">
        <div class="card mb-3 shadow-lg ">
          <div class="card-body">
            <ul class="diary__title">
              <label class="container" :for="`interest_${emotion.emotion}`">
                <input type="checkbox" :id="`interest_${emotion.emotion}`" :value="`${emotion.emotion_id}`"
                       name="user_interest"
                       class="check-highload"
                       v-model="selected_emotions">
                <span class="highload2"></span>
                <h4>{{ emotion.emotion }}</h4>
              </label>
            </ul>
          </div>
        </div>
      </li>

      <h3 class="ic1">Действия</h3>
      <p class="ic1"></p>
      <div class="card mb-3 shadow-lg " v-if="!loggedIn">
        <div class="card-body">
          <ul class="diary__title">
            <label class="container" :for="`action_1`">
              <input type="checkbox" :id="`action_1`" :value="`Прогулка`"
                     name="user_interest"
                     class="check-highload"
                     v-model="selected_actions">
              <span class="highload2"></span>
              <h4>Прогулка</h4>
            </label>
          </ul>
        </div>
      </div>
      <div class="card mb-3 shadow-lg " v-if="!loggedIn">
        <div class="card-body">
          <ul class="diary__title">
            <label class="container" :for="`action_2`">
              <input type="checkbox" :id="`action_2`" :value="`Общение с близкими`"
                     name="user_interest"
                     class="check-highload"
                     v-model="selected_actions">
              <span class="highload2"></span>
              <h4>Общение с близкими</h4>
            </label>
          </ul>
        </div>
      </div>


      <li v-for="action in actions">
        <div class="card mb-3 shadow-lg ">
          <div class="card-body">
            <ul class="diary__title">
              <label class="container" :for="`action_${action.action}`">
                <input type="checkbox" :id="`action_${action.action}`" :value="`${action.action_id}`"
                       name="user_interest"
                       class="check-highload"
                       v-model="selected_actions">
                <span class="highload2"></span>
                <h4>{{ action.action }}</h4>
              </label>
            </ul>
          </div>
        </div>
      </li>

      <h3 class="ic1">Оценка дня: </h3>
      <div class="rating-area ic1">
        <input type="radio" id="star-5" name="rating" v-model="day_rate" value="5">
        <label for="star-5" title="Оценка «5»"></label>

        <input type="radio" id="star-4" name="rating" v-model="day_rate" value="4">
        <label for="star-4" title="Оценка «4»"></label>

        <input type="radio" id="star-3" name="rating" v-model="day_rate" value="3">
        <label for="star-3" title="Оценка «3»"></label>

        <input type="radio" id="star-2" name="rating" v-model="day_rate" value="2">
        <label for="star-2" title="Оценка «2»"></label>

        <input type="radio" id="star-1" name="rating" v-model="day_rate" value="1">
        <label for="star-1" title="Оценка «1»"></label>
      </div>


      <div class="buttons">
        <button class="floating-button" type="submit" v-if="loggedIn">Сохранить</button>
        <button class="floating-button" type="submit" v-if="!loggedIn">Вернуться обратно</button>
      </div>
    </form>
  </div>
</template>

<script>
import {authComputed} from '@/store/helpers'
import axios from "axios";

export default {
  computed: {
    ...authComputed
  },
  name: "DiaryOfEmotions",
  data() {
    return {
      emotions: [],
      selected_emotions: [],
      selected_actions: [],
      actions: [],
      day_rate: 0,
      errorMsg: `An error occurred, please try again`
    }
  },
  async created() {
    // GET request using axios with async/await// исправить в зависисмости от url
    const response = await axios.get("https://eternal-awareness.herokuapp.com/emotion_diaries/new");
    this.emotions = response.data["emotions"];
    this.actions = response.data["actions"];
  },
  methods: {
    async submitHandler() {
      if (this.loggedIn) {
        await this.$swal.fire({
          scrollbarPadding: false,
          title: 'Предупреждение',
          text: 'Если у Вас уже есть дневник эмоций за сегодня, он будет перезаписан после сохранения текущего'
        });
        return
      }

      if (this.selected_emotions[0] === undefined && this.loggedIn) {
        await this.$swal.fire({
          scrollbarPadding: false,
          title: 'Ошибка',
          text: 'Пожалуйста, выберите хотя бы одну эмоцию'
        });
        return
      }

      if (this.selected_actions[0] === undefined && this.loggedIn) {
        await this.$swal.fire({
          scrollbarPadding: false,
          title: 'Ошибка',
          text: 'Пожалуйста, выберите хотя бы одно действие'
        });
        return
      }

      let formData = {
        emotions: this.selected_emotions,
        actions: this.selected_actions,
        day_rate: this.day_rate,
      }

      await axios.post('https://eternal-awareness.herokuapp.com/emotion_diaries/new', formData)// исправить в зависисмости от url
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
h4 {
  margin-left: 30px;
}

li {
  list-style-type: none;
}

.rating-area {
  overflow: hidden;
  margin-left: 30px;
  width: 265px;
}

.rating-area:not(:checked) > input {
  display: none;
}

.rating-area:not(:checked) > label {
  float: right;
  width: 42px;
  padding: 0;
  cursor: pointer;
  font-size: 32px;
  line-height: 32px;
  color: lightgrey;
  text-shadow: 1px 1px #bbb;
}

.rating-area:not(:checked) > label:before {
  content: '☆';
}

.rating-area > input:checked ~ label {
  color: gold;
  text-shadow: 1px 1px #c60;
}

.rating-area:not(:checked) > label:hover,
.rating-area:not(:checked) > label:hover ~ label {
  color: gold;
}

.rating-area > input:checked + label:hover,
.rating-area > input:checked + label:hover ~ label,
.rating-area > input:checked ~ label:hover,
.rating-area > input:checked ~ label:hover ~ label,
.rating-area > label:hover ~ input:checked ~ label {
  color: gold;
  text-shadow: 1px 1px goldenrod;
}

.rate-area > label:active {
  position: relative;
}

h2 {
  text-align: center
}

.cursor {
  cursor: default;
}

h3 {
  margin-left: 100px;
}

.ic1 {
  margin-top: 30px;
}
</style>

