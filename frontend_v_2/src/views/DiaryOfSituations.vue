<template>
  <div class="container col-xxl-8 px-2 py-2 ic2 cursor bg-white " @submit.prevent="submitHandler">
    <h2 class="benefits__title_theme_templates" v-if="loggedIn">
      {{ situation_name }}
    </h2>
    <h2 class="benefits__title_theme_templates" v-if="!loggedIn">
      Вы поругались с близким человеком. Как стоит поступить?
    </h2>
    <div id="v-model-radiobutton" class="demo">
      <label :for="`situation_1`" v-if="!loggedIn">
        <input type="radio" :id="`situation_1`"
               :value="`Сделать первый шаг и извиниться`"
               name="user_interest"
               v-model="answer">

        <span>
              <label for="`situation_${situationWithAnswer.answer}`">Сделать первый шаг и извиниться</label>
              <a style="color: green"
                 v-if="!isHidden && !loggedIn">✓</a>
            </span>
      </label>
      <label :for="`situation_2`" v-if="!loggedIn">
        <input type="radio" :id="`situation_2`"
               :value="`Попробовать выяснить с ним отношения`"
               name="user_interest"
               v-model="answer">

        <span>
              <label for="`situation_${situationWithAnswer.answer}`">Попробовать выяснить с ним отношения</label>
              <a style="color: green"
                 v-if="!isHidden && loggedIn && preferredAnswer === situationWithAnswer.answer">✓</a>
            </span>
      </label>
      <label :for="`situation_3`" v-if="!loggedIn">
        <input type="radio" :id="`situation_3`"
               :value="`Ждать извинения от него`"
               name="user_interest"
               v-model="answer">

        <span>
              <label for="`situation_${situationWithAnswer.answer}`">Ждать извинения от него</label>
              <a style="color: green"
                 v-if="!isHidden && loggedIn && preferredAnswer === situationWithAnswer.answer">✓</a>
            </span>
      </label>

      <li v-for="situationWithAnswer in situationObj" class="list-group list-group-flush">
        <label :for="`situation_${situationWithAnswer.answer}`">
          <input type="radio" :id="`situation_${situationWithAnswer.answer}`"
                 :value="`${situationWithAnswer.answer}`"
                 name="user_interest"
                 v-model="answer">

          <span>
              <label for="`situation_${situationWithAnswer.answer}`">{{ situationWithAnswer.answer }}</label>
              <a style="color: green"
                 v-if="!isHidden && loggedIn && preferredAnswer === situationWithAnswer.answer">✓</a>
              <a style="color: green" v-if="!isHidden && !loggedIn">✓</a>
            </span>
        </label>
      </li>
    </div>
    <div class="card-body">

    </div>
    <div class="btn-group ic3">
      <div class="buttons justify-content-center">
        <button type="submit" class="floating-button" id="leftBtn" v-if="loggedIn" v-on:click="submitHandler">
          Сохранить
        </button>
        <button type="submit" class="floating-button" id="leftBtn1" v-if="!loggedIn" v-on:click="submitHandler">
          Вернуться обратно
        </button>
      </div>
      <div class="buttons">
        <button type="button" class="floating-button" id="rightBtn" v-on:click="isHidden = !isHidden">Ответ авторов
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import {authComputed} from '@/store/helpers'

export default {
  computed: {
    ...authComputed
  },
  data() {
    return {
      situationObj: [],
      situation_name: '',
      answer: '',
      preferredAnswer: '',
      isHidden: true
    }
  },
  async created() {
// GET request using axios with async/await// исправить в зависисмости от url
    const response = await axios.get("https://eternal-awareness.herokuapp.com/situation_diaries/new");
    this.situationObj = response.data['situation'];
    this.situation_name = response.data['situation_name'];
    this.preferredAnswer = response.data['preferred_answer'];
    console.log(this.situationObj)
  },
  methods: {
    async submitHandler() {
      if (this.answer === '' && this.loggedIn) {
        await this.$swal.fire({
          scrollbarPadding: false,
          title: 'Ошибка',
          text: 'Пожалуйста, выберите что-нибудь'
        });
        return
      }

      if (this.situationObj[0] === undefined)
        await this.$router.push('/')

      let formData = {
        situation: this.situationObj[0].situation,
        answer: this.answer
      }

      console.log(1)
      await axios.post('https://eternal-awareness.herokuapp.com/situation_diaries/new', formData)// исправить в зависисмости от url
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

h2 {
  text-align: center
}

form {
  display: flex;
  flex-wrap: wrap;
  flex-direction: column;
}


#leftBtn {
  margin-left: 449px;
  width: 200px;
}

#leftBtn1 {
  margin-left: 449px;
  width: 200px;
}

#rightBtn {
  width: 200px;
  margin-left: 5px;
}

.cursor {
  cursor: default;
}

.ic3 {
  margin-top: 30px;
}

label {
  display: flex;
  cursor: pointer;
  font-weight: 500;
  position: relative;
  overflow: hidden;
  /*margin-bottom: 0.375em;*/
  /* Accessible outline */
  /* Remove comment to use */
  /*
  	&:focus-within {
  			outline: .125em solid $primary-color;
  	}
  */
}

label input {
  position: absolute;
  left: -9999px;
}

label input:checked + span {
  background-color: #d6d6e5;
}

label input:checked + span:before {
  box-shadow: inset 0 0 0 0.4375em #00005c;
}

label span {
  display: flex;
  align-items: center;
  padding: 0.375em 0.75em 0.375em 0.375em;
  border-radius: 99em;
  transition: 0.25s ease;
}

label span:hover {
  background-color: #d6d6e5;
}

label span:before {
  display: flex;
  flex-shrink: 0;
  content: "";
  background-color: #fff;
  width: 1.5em;
  height: 1.5em;
  border-radius: 50%;
  margin-right: 0.375em;
  transition: 0.25s ease;
  box-shadow: inset 0 0 0 0.125em #00005c;
}

.container1 {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 20px;
}

.ic1 {
  margin-top: 30px;
}

.ic2 {
  margin-top: 10vh;
}

.ic3 {
  margin-top: 20px;
}
</style>