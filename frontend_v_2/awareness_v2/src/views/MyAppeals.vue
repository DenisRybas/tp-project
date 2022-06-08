<template>
  <div class="container col-xxl-8 px-2 py-2 bg-white" @submit.prevent="submitHandler">
    <h2 class="benefits__title">
      <h2>Техническая поддержка
        <button type="submit" class="floating-button">
          <router-link to="/technical_support_user">Создать обращение</router-link>
        </button>
      </h2>
      <form>
        <h2 class="benefits__title">
          Выберите обращение, которое вы бы хотели просмотреть:</h2>
        <div id="v-model-radiobutton" class="demo">
          <div class="d-flex flex-column flex-grow-1 ms-5">
            <li v-for="appeal in appeals">
              <div class="card mb-3 shadow-lg ">
                <div class="card-body">
                  <ul class="diary__title">
                    <a class="link_list_diary">
                      <router-link :to="{ path: '/my_appeals/'+ appeal.id}"><a>{{ appeal.title }}</a>
                      </router-link>
                    </a>
                  </ul>
                </div>
              </div>
            </li>
          </div>
        </div>
      </form>
    </h2>
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
    const response = await axios.get("http://127.0.0.1:8000/technical_support_tickets/users-tickets");
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

h3 {
  margin-left: 100px;
}

button {
  float: right;
}
</style>


