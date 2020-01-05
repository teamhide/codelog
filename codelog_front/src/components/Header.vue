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
        <a href="#">최신</a>
      </div>
      <div class="header-bottom-right">
        <a href="#">태그</a>
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