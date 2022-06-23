<template>
  <div class="benefits__wrap">
    <h2 class="benefits__title">
      Выберите функцию:
    </h2>
    <div class="benefits__cards">
      <div class="benefits__card">
        <div class="benefits__card-pic">
          <img src="img/svg/Vector.png" alt="" class="benefits__card-thumb">
        </div>
        <h3 class="benefits__card-title">
          Дневник по шаблону
        </h3>
        <p class="benefits__card-desc">
          Ответ на задаваемые приложением вопросы
        </p>
        <div class="link">
          <router-link class="a" to="/diary_of_templates"> Начать</router-link>
        </div>
      </div>
      <div class="benefits__card">
        <div class="benefits__card-pic">
          <img src="img/svg/Subtract.png" alt="" class="benefits__card-thumb">
        </div>
        <h3 class="benefits__card-title">
          Дневник эмоций
        </h3>
        <p class="benefits__card-desc">
          Указание эмоций, испытанных за сегодня и Ваших действий
        </p>
        <router-link class="a" to="/diary_of_emotions"> Начать</router-link>
      </div>
      <div class="benefits__card">
        <div class="benefits__card-pic">
          <img src="img/svg/OpenBook.png" alt="" class="benefits__card-thumb">
        </div>
        <h3 class="benefits__card-title">
          Дневник ситуаций
        </h3>
        <p class="benefits__card-desc">
          Постановка Вас приложением в различные ситуации
        </p>
        <router-link class="a" to="/diary_of_situations" tag="button"> Начать</router-link>
      </div>

      <div class="benefits__card">
        <div class="benefits__card-pic">
          <img src="img/svg/Outline.png" alt="" class="benefits__card-thumb">
        </div>
        <h3 class="benefits__card-title">
          Трекер привычек
        </h3>
        <p class="benefits__card-desc">
          Отслеживание Ваших привычек
        </p>
        <div class="link">
          <router-link class="a" to="/habit_tracker"> Начать</router-link>
        </div>
      </div>
    </div>
  </div>
</template>
<script>

export default {
  name: 'HomeView',
}

</script>
document.body.style.zoom="80%"
<style scoped>
a:hover {
  color: #4f73e8; /* Цвет ссылки при наведении */
}
html{
zoom: 80%;
}
a:focus {
  outline: none;
}
</style>