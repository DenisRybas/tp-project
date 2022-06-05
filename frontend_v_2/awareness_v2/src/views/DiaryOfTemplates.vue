<template>
      <div class="container col-xxl-8 px-2 py-2 bg-white" @submit.prevent="submitHandler">
                <h2 class="benefits__title">
                    <img src="img/svg/Vector.png" alt="Diary of templates:" class="benefits__card-thumb"> Diary of templates
                    <form>
                    <h2 class="benefits__title_theme_templates">
                        {{ theme1 }}
                    </h2>
                       <div class="input-field">
                          <textarea v-model.trim="test1" placeholder="введите несколько строчек"></textarea>
                       </div>
                    <h2 class="benefits__title_theme_templates">
                      {{ theme2 }}
                    </h2>
                        <div class="input-field">
                              <textarea v-model.trim="test2" placeholder="введите несколько строчек"></textarea>
                       </div>
                        <div class="buttons">
                                <button type="submit" class="floating-button">Save</button>
                        </div>
                    </form>
                  <ul id="example-1">
                        <li v-for="item in items" :key="item.message">
                          {{ item.message }}
                        </li>
                  </ul>
                </h2>
      </div>
</template>

<script>
import axios from "axios";

export default {
  name: 'diary_of_templates',
  data: () => ({
    test1: '',
    test2: '',
    theme1:'',
    theme2:''
  }),
  methods: {
    async created() {
      // GET request using axios with async/await// исправить в зависисмости от url
      const response = await axios.get("/diary_of_templates");
      this.theme1 = response.data["theme_1"];
      this.theme2 = response.data["theme_2"];
      this.diary = response.data["theme_2"];
    },

     async submitHandler() {
      let formData = {
        test1: this.test1,
        test2: this.test2
      }
     axios.post('/diary_of_templates', formData)// исправить в зависисмости от url
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
</style>