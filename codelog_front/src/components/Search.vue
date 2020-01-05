<template>
  <div class="search-container">
    <input type="text" class="search-bar" placeholder="태그 또는 검색어를 입력하세요."/>
  </div>
</template>

<script>
export default {
  name: 'Search'
}
</script>

<style scoped>
.search-container {
  display: grid;
  height: 100vh;
}

.search-bar {
  height: 50px;
  border: none;
  padding: 10px;
  font-size: 20px;
  border-radius: 20px;
}
</style>