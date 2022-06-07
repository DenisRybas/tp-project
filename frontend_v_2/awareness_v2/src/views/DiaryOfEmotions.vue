<template>
  <div class="container col-xxl-8 px-2 py-2 bg-white" @submit.prevent="submitHandler">
    <form>
      <h2 class="benefits__title">
        <!--        <img src="/img/svg/Subtract.png" alt="emotion_diaries:" class="benefits__card-thumb">-->
        Выберите из списка эмоции, которые вы испытали сегодня:</h2>
      <h3>Эмоции</h3>
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

      <h3>Действия</h3>
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

      <h3>Оценка дня: </h3>
      <div class="rating-area">
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
        <button class="floating-button" type="submit">Сохранить</button>
      </div>
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "DiaryOfEmotions",
  data() {
    return {
      emotions: [],
      selected_emotions: [],
      selected_actions: [],
      actions: [],
      day_rate: 5,
      errorMsg: `An error occurred, please try again`
    }
  },
  async created() {
    // GET request using axios with async/await// исправить в зависисмости от url
    const response = await axios.get("http://127.0.0.1:8000/emotion_diaries/new");
    this.emotions = response.data["emotions"];
    this.actions = response.data["actions"];
  },
  methods: {
    async submitHandler() {
      let formData = {
        emotions: this.selected_emotions,
        actions: this.selected_actions,
        day_rate: this.day_rate,
      }

      axios.post('http://127.0.0.1:8000/emotion_diaries/new', formData)// исправить в зависисмости от url
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
  content: '★';
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

h3 {
  margin-left: 100px;
}
</style>

