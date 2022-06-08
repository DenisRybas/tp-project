<template>
  <nav class="navbar navbar-expand-lg bg-light-accent">
    <div class="container-fluid">
      <a class="navbar-brand">
        <router-link class="a" to="/">
          <img src="img/logo.png" alt="" width="50" height="50">
        </router-link>

      </a>
      <h1 class="ps-2 display-4">
        <router-link class="a" to="/">{{ ('awareness') }}
        </router-link>
      </h1>
      <ul class="navbar-nav nav-pills ms-auto mb-2 mb-lg-0 justify-content-end">
        <li class="nav-item me-2 mb-2 mb-lg-0 text-center" v-if="!loggedIn">
            <router-link to="/login">Логин</router-link>
        </li>
        <li class="nav-item me-2 mb-2 mb-lg-0 text-center" v-if="!loggedIn">
          <router-link to="/registration">Регистрация</router-link>
        </li>
        <li v-if="loggedIn">
          <ul class="navbar-nav ms-auto mb-2 mb-lg-0 justify-content-end">
            <li class="nav-item me-2 mb-2 mb-lg-0 dropdown">
              <ul class="navbar-nav nav-pills ms-auto mb-2 mb-lg-0 justify-content-end">
                <li class="nav-item me-2 mb-2 mb-lg-0 text-center">
                  <router-link to="/diary">Мои дневники</router-link>
                </li>
                <li class="nav-item me-2 mb-2 mb-lg-0 text-center">
                  <router-link to="/settings">Настройки</router-link>
                </li>
                <li class="nav-item me-2 mb-2 mb-lg-0 text-center">
                  <router-link to="/logout">Выход</router-link>
                </li>
              </ul>
            </li>
          </ul>

        </li>

      </ul>
    </div>
  </nav>
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
</style>
