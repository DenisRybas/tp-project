<template>
 <div class="container col-xxl-8 px-2 py-2 bg-white" @submit.prevent="submitHandler">
                <h2 class="benefits__title">
                    <img src="img/svg/Vector.png" alt="Diary of templates:" class="benefits__card-thumb"> Creating a request
                    <form>
                    <h2 class="benefits__title_theme_templates">
                      Enter a subject:
                    </h2>
                       <div class="input-field">
                          <textarea class="theme" v-model.trim="theme" placeholder="enter a subject"></textarea>
                       </div>
                    <h2 class="benefits__title_theme_templates">
                      Enter a request:
                    </h2>
                        <div class="input-field">
                          <textarea  v-model.trim="request" placeholder="enter a request"></textarea>
                       </div>
                        <div class="buttons">
                                <button type="submit" class="floating-button">Send</button>
                        </div>
                    </form>

                </h2>
      </div>
</template>

<script>
import axios from "axios";

export default {
  name: 'TechnicalSupportUser',
  data: () => ({
    theme:'',
    request:''
  }),
  methods: {
     async submitHandler() {
      let formData = {
        theme: this.theme,
        request: this.request
      }
     axios.post('/technical_support_user', formData)// исправить в зависисмости от url
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
   textarea.theme {
    background: #f2f3f4;
    border: 2px solid #d0d0d0; /* Параметры рамки */
    padding: 10px; /* Поля */
    width: 100%; /* Ширина */
    height: 50px; /* Высота */
    box-sizing: border-box; /* Алгоритм расчёта ширины */
    font-size: 16px; /* Размер шрифта */
    }
</style>