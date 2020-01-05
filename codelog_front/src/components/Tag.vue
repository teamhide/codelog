<template>
  <div class="tag-container">
    <div class="tag">
      <div class="tag-name">
        Python
      </div>
      <div class="tag-count">
        100
      </div>
    </div>
    <div class="tag">
      <div class="tag-name">
        Container Python
      </div>
      <div class="tag-count">
        100
      </div>
    </div>
    <div class="tag">
      <div class="tag-name">
        Container Orchestration
      </div>
      <div class="tag-count">
        100
      </div>
    </div>
    <div class="tag">
      <div class="tag-name">
        Container Python
      </div>
      <div class="tag-count">
        100
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
.tag-name {
  padding-right: 5px;
}
.tag-count {
  padding-left: 5px;
  font-size: 12px;
  color: #878787;
}
</style>