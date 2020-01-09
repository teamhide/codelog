<template>
  <div class="write-container">
    <div class="post-url">
      <textarea v-model="url" placeholder="URL" rows="5"/>
    </div>
    <div class="post-tags">
      <input v-model="tags" type="text" placeholder="Tags" />
    </div>
    <div v-on:click="write" class="post-write">
      POST
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { Endpoint } from '../enum'

export default {
  name: 'Write',
  data() {
    return {
      url: '',
      tags: '',
    }
  },
  created() {
    if (!this.$store.state.token) {
      alert('로그인이 필요한 기능입니다.');
      history.back();
    }
  },
  methods: {
    write() {
      var params = new URLSearchParams();
      params.append('url', this.url);
      params.append('tags', this.tags);
      axios.post(`${Endpoint.URL}/api/feeds/`, params, {
          headers: { Authorization: 'Bearer '+ this.$store.state.token }
        })
        .then((res) => {
          window.location.replace('/');
        })
        .catch((err) => {
          alert('글쓰기 실패');
        });
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