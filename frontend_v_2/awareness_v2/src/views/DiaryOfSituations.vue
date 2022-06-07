<template>
  <h2 class="benefits__title">
    <!--    <img src="/img/svg/OpenBook.png" alt="Diary_of_situations" class="benefits__card-thumb">-->
    Дневник ситуаций
  </h2>
  <div class="container col-xxl-8 px-2 py-2 bg-white" @submit.prevent="submitHandler">
    <h2 class="benefits__title_theme_templates">
      {{ situation }}
    </h2>
    <div id="v-model-radiobutton" class="demo">
      <h3>Варианты ответа:</h3>
      <li v-for="situationWithAnswer in situationObj">
        <div class="card mb-3 shadow-lg ">
          <div class="card-body">
            <ul class="diary__title">
              <label class="container" :for="`situation_${situationWithAnswer.answer}`">
                <input type="radio" :id="`situation_${situationWithAnswer.answer}`" :value="`${situationWithAnswer.answer}`"
                       name="user_interest"
                       v-model="answer">

                <label for="`situation_${situationWithAnswer.answer}`"><h4>{{ situationWithAnswer.answer }}</h4></label>

              </label>
            </ul>
          </div>
        </div>
      </li>
      <h3>Выбран: {{ answer }}</h3>
    </div>
    <h3 v-if="!isHidden">Правильный ответ: {{preferredAnswer}}</h3>
    <div class="card-body">

    </div>
    <div class="buttons">
      <button type="submit" class="floating-button" v-on:click="submitHandler">Сохранить</button>
    </div>
    <div class="buttons">
      <button type="button" class="floating-button" v-on:click="isHidden = !isHidden">Правильный ответ</button>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      situationObj: [],
      situation: '',
      answer: '',
      preferredAnswer: '',
      isHidden: true
    }
  },
  async created() {
// GET request using axios with async/await// исправить в зависисмости от url
    const response = await axios.get("http://127.0.0.1:8000/situation_diaries/new");
    this.situationObj = response.data['situation'];
    this.situation = response.data['situation'].situation;
    this.preferredAnswer = response.data['preferred_answer'];
    console.log(this.situationObj)
  },
  methods: {
    async submitHandler() {
      let formData = {
        situation: this.situationObj[0].situation,
        answer: this.answer
      }

      console.log(1)
      axios.post('http://127.0.0.1:8000/situation_diaries/new', formData)// исправить в зависисмости от url
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
li {
  list-style-type: none;
}

h4 {
  margin-left: 30px;
}

h2 {
  text-align: center
}
</style>