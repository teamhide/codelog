<template>
  <div id="app">
    <Header />
    <Section />
    <Footer />
    <div class="write">
      <span>Write</span>
    </div>
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
.write {
  position: fixed;
  bottom: 20px;
  right: 20px;
  width: 80px;
  height: 80px;
  border-radius: 50%;
  background: white;
  font-size: 16px;
  display: grid;
  align-items: center;
  justify-content: center;
}
</style>
