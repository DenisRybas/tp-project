<template>
    <div class="container bg-white">
        <h1 class="ps-2 display-6">{{ 'FAQ' }}
            <div class="buttons1">
                <button type="submit" class="floating-button">
                  <router-link to="/my_appeals">My appeals</router-link>
                </button>
                <button type="submit" class="floating-button">
                  <router-link to="/technical_support_user">Create an appeal</router-link>
                </button>
            </div>
        </h1>
        <hr>
        <div class="px-4 py-4">
            <p>
                {{ 'FAQ this' }}
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