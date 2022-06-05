<template>
  <h2 class="benefits__title">
 <img src="/img/svg/OpenBook.png" alt="Diary_of_situations" class="benefits__card-thumb">Diary of situations
  </h2>
 <h2 class="benefits__title_theme_templates">
   {{ question }}Test questions
 </h2>
<div id="v-model-radiobutton" class="demo">
    <div class="card mb-3 shadow-lg ">
                   <div class="card-body">
                       <ul class="diary__title">
                           <input type="radio" id="test1" value="test1" v-model="picked" />
                            <label for="test1">{{ test1 }}</label>
                        <br />
                       </ul>
                   </div>
    </div>
      <div class="card mb-3 shadow-lg ">
                   <div class="card-body">
                       <ul class="diary__title">
                             <input type="radio" id="test2" value="test2" v-model="picked" />
                         <label for="test2">{{ test2 }}</label>
                             <br />
                       </ul>
                   </div>
    </div>
      <div class="card mb-3 shadow-lg ">
                   <div class="card-body">
                       <ul class="diary__title">
                         <input type="radio" id="test3" value="test3" v-model="picked" />
                         <label for="test3">{{ test3 }}</label>
                         <br />
                       </ul>
                   </div>
    </div>
    <span>Picked: {{ picked }}</span>
  </div>
  <div class="buttons">
    <button type="submit" class="floating-button">Save</button>
  </div>
   <div class="buttons">
    <button type="submit" class="floating-button">
      <router-link to="/registration">Right answer</router-link></button>
  </div>

</template>

<script>
  import axios from "axios";

  export default {
  data() {
    return {
      question:'',
      picked: '',
      test1: '',
      test2: '',
      test3: ''
    }
  },
    methods: {
    async created() {
      // GET request using axios with async/await// исправить в зависисмости от url
      const response = await axios.get("/diary_of_situations");
      this.question = response.data["question"];
      this.test1 = response.data["test1"];
      this.test2 = response.data["test2"];
      this.test3 = response.data["test3"];
    },

     async submitHandler() {
      let formData = {
        picked: this.picked,
      }
     axios.post('/diary_of_situations', formData)// исправить в зависисмости от url
    .then(function (response) {
        console.log(response);
     })
     .catch(function (error) {
       console.log(error);
     });
      console.log(formData)

      await this.$router.push('/')
    },
  },
  }
</script>

<style scoped>

</style>

