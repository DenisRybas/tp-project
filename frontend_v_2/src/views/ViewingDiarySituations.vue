<template>
  <div class="container col-xxl-8 px-2 py-2 bg-white cursor">
    <form>
      <h2 class="benefits__title_theme_templates">
        Выберите ситуацию дневника, которую Вы бы хотели просмотреть:</h2>
      <div id="v-model-radiobutton" class="demo">
          <li v-for="diary in diaries">
            <div class="card mb-3 shadow-lg ">
              <div class="card-body">
                <ul class="diary__title">
                  <a class="link_list_diary">
                    <router-link :to="{ path: '/viewing_diary_situations/'+ diary.id}"><a>{{
                        diary.situation
                      }}</a>
                    </router-link>
                  </a>
                </ul>
              </div>
            </div>
          </li>
      </div>
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "ViewingDiarySituations",
  data() {
    return {
      diaries: [],
      errorMsg: `An error occurred, please try again`
    }
  },
  async created() {
// GET request using axios with async/await// исправить в зависисмости от url
    const response = await axios.get("https://eternal-awareness.herokuapp.com/situation_diaries");
    this.diaries = response.data["situation_diaries"];
    console.log(this.diaries)
  },
}
</script>

<style scoped>
h4 {
  margin-left: 30px;
}

li {
  list-style-type: none;
}

h3 {
  margin-left: 100px;
}

a {
  color: black;
  text-decoration: none; /* Отменяем подчеркивание у ссылки */
}

a:hover {
color: #4f73e8; /* Цвет ссылки при наведении */
      cursor: pointer;
}

a:focus {
  outline: none;
}

.cursor {
  cursor: default;
}
</style>