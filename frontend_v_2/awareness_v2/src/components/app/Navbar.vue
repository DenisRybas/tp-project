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
        <li class="nav-item me-2 mb-2 mb-lg-0 text-center">
          <a class="nav-link" style="color: black !important;" aria-current="page">
            <router-link to="/faq">FAQ</router-link>
          </a>
        </li>
        <li class="nav-item me-2 mb-2 mb-lg-0 text-center" v-if="!loggedIn">
          <a class="w-100 btn btn btn-secondary text-light " style="color: white !important">
            <router-link to="/login" >Логин</router-link>
          </a>
        </li>
        <li class="nav-item me-2 mb-2 mb-lg-0 text-center">
          <a class="w-100 btn btn btn-secondary text-light " v-if="!loggedIn" style="color: white !important">
            <router-link to="/registration">Регистрация</router-link>
          </a>
        </li>
        <li v-if="loggedIn">
          <ul class="navbar-nav ms-auto mb-2 mb-lg-0 justify-content-end">
            <li class="nav-item me-2 mb-2 mb-lg-0 dropdown">
              <ul class="navbar-nav nav-pills ms-auto mb-2 mb-lg-0 justify-content-end">
                <li class="nav-item me-2 mb-2 mb-lg-0 text-center">
                  <a class="w-100 btn btn btn-secondary text-light " style="color: white !important">
                    <router-link to="/diary">Мои дневники</router-link>
                  </a>
                </li>
                <li class="nav-item me-2 mb-2 mb-lg-0 text-center">
                  <a class="w-100 btn btn btn-secondary text-light " style="color: white !important">
                    <router-link to="/settings">Настройки</router-link>
                  </a>
                </li>
                <li class="nav-item me-2 mb-2 mb-lg-0 text-center">
                  <a class="w-100 btn btn btn-secondary text-light " style="color: white !important">
                    <router-link to="/logout">Выход</router-link>
                  </a>
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
