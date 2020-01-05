<template>
  <header>
    <div class="header-top">
      <div class="header-top-left">
        <a href="#">검색</a>
      </div>
      <div class="header-top-center">
        <a href="#">Codelog</a>
      </div>
      <div class="header-top-right">
        <a href="#">아이콘</a>
      </div>
    </div>
    <div class="header-bottom">
      <div class="header-bottom-left">
        <router-link to="/">최신</router-link>
      </div>
      <div class="header-bottom-right">
        <router-link to="/tags">태그</router-link>
      </div>
    </div>
  </header>
</template>

<script>
export default {
  name: 'Header',
}
</script>

<style scoped>
header {
  height: 100px;
  background-color: #6196ff;
  display: grid;
  grid-template-rows: auto auto;
}

.header-top {
  display: grid;
  grid-template-columns: auto auto auto;
  border-bottom: 0.5px solid #94b8ff;
}

.header-bottom {
  display: grid;
  grid-template-columns: auto auto;
}

.header-top-left {
  display: grid;
  justify-content: flex-start;
  align-content: center;
  padding-left: 20px;
}

.header-top-left a {
  color: white;
  text-decoration: none;
}

.header-top-center {
  display: grid;
  justify-content: center;
  align-items: center;
}

.header-top-center a {
  color: white;
  text-decoration: none;
  font-size: 25px;
}

.header-top-right {
  display: grid;
  justify-content: flex-end;
  align-content: center;
  padding-right: 20px;
}

.header-top-right a {
  color: white;
  text-decoration: none;
}

.header-bottom-left, .header-bottom-right {
  display: grid;
  justify-content: center;
  align-items: center;
}

.header-bottom a {
  color: white;
  text-decoration: none;
}
</style>