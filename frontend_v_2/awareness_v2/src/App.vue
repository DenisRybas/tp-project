<template>
  <div id="app">
    <component :is="layout">
      <router-view/>
    </component>
  </div>
</template>

<script>
import MainLayout from '@/layouts/MainLayout'
export default {
  computed: {
    layout() {
      return (this.$route.meta.layout || 'empty') + '-layout'
    }
  },
  components: {
     MainLayout
  }
}
</script>


<style lang="scss">
@import 'materialize/css/materialize.min.css';
@import 'assets/index.css';
@import 'assets/style.css';
@import 'assets/main.css';
@import 'assets/theme.min.css';
</style>
