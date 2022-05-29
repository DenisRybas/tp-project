<template>
<body class="d-flex flex-column min-vh-100">
    <Navbar/>
    <main class="flex-grow-1">
      <div class="app-page">
        <body>
        <router-view />
        </body>
      </div>
    </main>
    <Footer/>
    <div class="fixed-action-btn">
      <a class="btn-floating btn-large blue" href="#">
        <i class="large material-icons">add</i>
      </a>
    </div>
</body>
</template>

<script>
import Navbar from '@/components/app/Navbar'
import Footer from '@/components/app/Footer'

export default {
  name: 'main-layout',
  data: () => ({
    isOpen: true
  }),
  components: {
    Navbar, Footer
  }
}
</script>
