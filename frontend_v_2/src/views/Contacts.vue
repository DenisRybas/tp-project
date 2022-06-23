<template>
  <div class="container bg-white center-this">
    <h1 class="ps-2 display-4">{{ 'Контакты' }}</h1>
    <hr>
    <div class="px-4 py-4">
      <p>
        {{ 'Соболь Илья' }}: <a href="mailto:ilja-sobol.sobol@yandex.ru" target="_blank">ilja-sobol.sobol@yandex.ru</a>
      </p>
      <p>
        {{ 'Рыбас Денис' }}: <a href="mailto:denis2002.rybas@gmail.com" target="_blank">denis2002.rybas@gmail.com</a>
      </p>
    </div>

  </div>
</template>

<script>
export default {
  name: "Contacts"
}
</script>

<style scoped>
a {
  text-decoration: none;
  color: #0d6efd;
}

h1 {
  text-align: center;
}

.center-this {
    margin-top: 10%;
}
</style>