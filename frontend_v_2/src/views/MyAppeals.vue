<template>
  <div class="container col-xxl-8 px-2 py-2 bg-white cursor" @submit.prevent="submitHandler">

    <h2 class="benefits__title_theme_templates">
      Выберите обращение, которое Вы бы хотели просмотреть: </h2>

    <form>

      <div id="v-model-radiobutton" class="demo">
        <div class="d-flex flex-column flex-grow-1 ms-5">
          <li v-for="appeal in appeals">
            <div class="card mb-3 shadow-lg">
              <div class="card-body">
                <ul>
                  <span class="ic1">
                    <router-link class="a1" :to="{ path: '/my_appeals/'+ appeal.id}"><a>{{ appeal.title }}</a>
                    </router-link>
                  </span>
                </ul>
              </div>
            </div>
          </li>
        </div>
      </div>
    </form>
    <div class="buttons ic3">
      <router-link class="btn btn-outline-dark text-center" to="/technical_support_user">Создать обращение</router-link>
    </div>
  </div>
</template>
<script>
import axios from "axios";

export default {
  name: "MyAppeals",
  data() {
    return {
      appeals: [],
      errorMsg: `An error occurred, please try again`
    }
  },
  async created() {
// GET request using axios with async/await// исправить в зависисмости от url
    const response = await axios.get("https://eternal-awareness.herokuapp.com/technical_support_tickets/users-tickets");
    this.appeals = response.data["tickets"];
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

.cursor {
  cursor: default;
}

h3 {
  margin-left: 100px;
}

button {
  margin-left: 555px;
}

.a1 {
  color: #4f73e8;
  text-decoration: none; /* Отменяем подчеркивание у ссылки */
}

.a1:hover {
  color: #4f73e8; /* Цвет ссылки при наведении */
  text-decoration: underline;
}
.a1:focus {
  outline: none;
}

a {
 text-decoration: none;
}

.ic1 {
  margin-top: 50px;
}
.ic3 {
  margin-top: 30px;
}
</style>


