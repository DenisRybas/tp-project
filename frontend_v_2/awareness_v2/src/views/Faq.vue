<template>
  <div class="container bg-white">
    <h1 class="ps-2 display-6">{{ 'FAQ' }}
      <div class="buttons1">
        <button type="submit" class="floating-button">
          <router-link to="/my_appeals">Мои обращения</router-link>
        </button>
        <button type="submit" class="floating-button">
          <router-link to="/technical_support_user">Создать обращение</router-link>
        </button>
      </div>
    </h1>
    <hr>
    <div class="px-4 py-4">
      <p>
        {{ 'FAQ содержание' }}
      </p>
    </div>

  </div>
</template>

<script>
export default {
  name: "Faq"
}
</script>

<style scoped>
</style>