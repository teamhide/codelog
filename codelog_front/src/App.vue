<template>
  <div id="app">
    <Header />
    <Section />
    <Footer />
  </div>
</template>

<script>
import Header from './components/Header.vue'
import Section from './components/Section.vue'
import Footer from './components/Footer.vue'

export default {
  name: 'app',
  components: {
    Header,
    Section,
    Footer,
  }
}
</script>

<style>
html, body {
  padding: 0;
  margin: 0;
  background-color: #edededed;
}

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
</style>
