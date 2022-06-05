<template>
 <div class="container col-xxl-8 px-2 py-2 bg-white" @submit.prevent="submitHandler">
                <h2 class="benefits__title">
                    <img src="img/svg/Vector.png" alt="Diary of templates:" class="benefits__card-thumb"> Technical support
                    <form>
                    <ul id="example-1">
                          <li v-for="item in items" :key="item.message">
                          {{ item.message }}
                          </li>
                    </ul>
                    <h2 class="benefits__title_theme_templates">
                      User's request:
                    </h2>
                       <div class="input-field">
                          <textarea v-model.trim="theme1" placeholder="enter a few lines"></textarea>
                       </div>
                    <h2 class="benefits__title_theme_templates">
                     Technical support response:
                    </h2>
                        <div class="input-field">
                              <textarea v-model.trim="theme2 " placeholder="enter a few lines"></textarea>
                       </div>
                    </form>

                </h2>
      </div>
</template>
<script>
import axios from "axios";

export default {
  name: "MyAppeals",
  data: () => ({
    theme1:'',
    theme2:'',
    results: []
  }),
  methods: {
    async asyncData () {
      const response  = await axios.get('/my_appeals')
      this.results = response.data
    },
    async created() {
      // GET request using axios with async/await// исправить в зависисмости от url
      const response = await axios.get("/diary_of_templates");
      this.theme1 = response.data["theme_1"];
      this.theme2 = response.data["theme_2"];
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