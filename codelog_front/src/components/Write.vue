<template>
  <div class="write-container">
    <div class="post-url">
      <textarea placeholder="URL" rows="5"/>
    </div>
    <div class="post-tags">
      <input type="text" placeholder="Tags" />
    </div>
    <div class="post-write">
      POST
    </div>
  </div>
</template>

<script>
export default {
  name: 'Write',
  created() {
    if (!this.$store.state.token) {
      alert('Login first');
      history.back();
    }
  }
}
</script>

<style scoped>
.write-container {
  display: grid;
  justify-items: center;
  align-items: center;
}
.post-url textarea {
  border: none;
  font-size: 20px;
  padding: 15px;
  min-width: 410px;
  max-width: 900px;
  margin-top: 20px;
  margin-bottom: 20px;
  resize: none;
  border-radius: 10px;
  font-weight: 200;
}
.post-tags input {
  border: none;
  font-size: 20px;
  min-width: 410px;
  padding: 15px;
  border-radius: 10px;
  font-weight: 200;
}
.post-write {
  margin-top: 20px;
  padding: 20px;
  background-color: #6196ff;
  color: white;
  font-weight: 600;
  width: 400px;
  cursor: pointer;
  border-radius: 10px;
  text-align: center;
  font-size: 22px;
}
.write-btn {
  display: none;
}
</style>