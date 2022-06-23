<template>
  <footer class="footer navbar navbar-expand navbar-dark bg-dark mt-auto py-3">
    <div class="container-fluid">
      <span class="navbar-text me-auto">Copyright © 2022, This is awareness</span>
      <ul class="navbar-nav ms-auto">
        <li class="nav-item me-2">
          <a class="nav-link" aria-current="page">
            <router-link to="/about">О нас</router-link>
          </a>
        </li>
        <li class="nav-item me-2">
          <a class="nav-link" aria-current="page">
            <router-link to="/contacts">Контакты</router-link>
          </a>
        </li>
        <li class="nav-item me-2" v-if="loggedIn">
          <a class="nav-link" aria-current="page">
            <router-link to="/my_appeals" class="routerLink">Техподдержка</router-link>
          </a>
        </li>
      </ul>
    </div>
  </footer>
</template>

<script>
import {authComputed} from '@/store/helpers'

export default {
  computed: {
    ...authComputed
  }
}
</script>

<style scoped>
a {
  color: white;
  text-decoration: none; /* Отменяем подчеркивание у ссылки */
}

a:hover {
color: #4f73e8; /* Цвет ссылки при наведении */
}

a:focus {
  outline: none;
}

</style>