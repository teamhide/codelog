<template>
  <section>
    <Feed />
    <Feed />
    <Feed />
    <Feed />
    <Feed />
  </section>
</template>

<script>
import Feed from './Feed.vue';

export default {
  name: 'Section',
  components: {
    Feed
  }
}
</script>

<style scoped>
section {
  display: grid;
  justify-content: center;
  grid-template-columns: auto auto auto auto;
  padding: 20px;
}
</style>