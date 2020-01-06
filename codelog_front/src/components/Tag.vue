<template>
  <div class="tag-container">
    <div class="tag">
      <div class="tag-name">
        Python
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Tag'
}
</script>

<style scoped>
.tag-container {
  display: flex;
  flex-wrap: wrap;
}
.tag {
  display: grid;
  justify-content: center;
  align-items: center;
  grid-template-columns: auto auto;
  background-color: white;
  border-radius: 10px;
  height: 30px;
  border: 1px solid lightgray;
  padding-left: 10px;
  padding-right: 10px;
  margin: 5px;
}
.tag:hover {
  border-color: #6196ff;
  color: #6196ff;
}
</style>