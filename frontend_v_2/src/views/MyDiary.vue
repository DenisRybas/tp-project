<template>
  <div class="container col-xxl-8 px-2 py-2 bg-white cursor">
    <div class="row flex-lg-row align-items-center g-0 py-5">
      <div class="text-center">
        <h1 class="display-5 lh-1 mb-3 ms-3"> {{nickname}} </h1>
      </div>
    </div>

    <div class="container-fluid">
      <div class="d-flex align-items-start">
        <div class="mt-2 nav ps-2 flex-column nav-pills me-3" id="v-pills-tab" role="tablist"
             aria-orientation="vertical">
          <a class="w-100 btn btn-lg btn-secondary text-light"
             aria-selected="true">
            <router-link class="a" to="/diary">Мои дневники</router-link>
          </a>
          <a class="nav-link btn btn-lg remove-glow"
             aria-selected="false">
            <router-link class="a" to="/settings">Настройки</router-link>
          </a>
        </div>
        <div class="d-flex flex-column flex-grow-1 ms-5">


          <div class="card mb-3 shadow-lg ">
            <div class="card-body">
              <ul class="diary__title">
                <a class="link_list_diary">
                  <router-link class="a" to="/viewing_diary_templates">Дневники по шаблону</router-link>
                </a>
              </ul>
            </div>

          </div>
          <div class="card mb-3 shadow-lg ">
            <div class="card-body">
              <ul class="diary__title">
                <a class="link_list_diary">
                  <router-link class="a" to="/viewing_diary_emotions">Дневники эмоций</router-link>
                </a>
              </ul>
            </div>
          </div>
          <div class="card mb-3 shadow-lg ">
            <div class="card-body">
              <ul class="diary__title">
                <a class="link_list_diary">
                  <router-link class="a" to="/viewing_diary_situations">Дневники ситуаций</router-link>
                </a>
              </ul>
            </div>
          </div>
          <div class="card mb-3 shadow-sm ">
            <div class="card-body">
              <ul class="diary__title">
                <a class="link_list_diary">
                  <router-link class="a" to="/viewing_habit_tracker">Трекер привычек</router-link>
                </a>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "MyDiary",
  data() {
    return {
      nickname: '',
      errorMsg: `An error occurred, please try again`
    }
  },
  async created() {
    // GET request using axios with async/await// исправить в зависисмости от url
    const response = await axios.get("https://eternal-awareness.herokuapp.com/edit_account");
    this.nickname = response.data["username"];
  },
}
</script>

<style scoped>
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
