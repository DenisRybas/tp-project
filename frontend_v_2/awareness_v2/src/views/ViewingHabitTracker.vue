<template>
  <div class="container col-xxl-8 px-2 py-2 bg-white">
    <form>
      <h2 class="benefits__title">
        Выберите привычку, которую вы бы хотели просмотреть:</h2>
      <div id="v-model-radiobutton" class="demo">
        <div class="d-flex flex-column flex-grow-1 ms-5">
          <li v-for="habit in habits">
            <div class="card mb-3 shadow-lg ">
              <div class="card-body">
                <ul class="diary__title">
                  <a class="link_list_diary">
                    <router-link :to="{ path: '/viewing_habit_tracker/'+ habit.id}"><a>{{ habit.name }}</a>
                    </router-link>
                  </a>
                </ul>
              </div>
            </div>
          </li>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "ViewingHabitTracker",
  data() {
    return {
      habits: [],
      errorMsg: `An error occurred, please try again`
    }
  },
  async created() {
// GET request using axios with async/await// исправить в зависисмости от url
    const response = await axios.get("http://127.0.0.1:8000/habit_tracker");
    this.habits = response.data["habits"];
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
</style>



