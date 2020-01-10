<template>
  <div class="write-container">
    <div class="post-url">
      <textarea id="post-url" v-model="url" placeholder="http://" rows="5"/>
    </div>
    <div class="post-tags">
      <input id="post-tags" v-model="tags" type="text" placeholder="#Python #Golang (Maximum 3)" />
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
      failCount: 0,
    }
  },
  created() {
    if (!this.$store.getters.getToken) {
      alert('로그인이 필요한 기능입니다.');
      history.back();
    }

    var params = new URLSearchParams();
    params.append('token', this.$store.getters.getToken);
    axios.post(`${Endpoint.URL}/oauth/verify_token`, params)
    .catch((err) => {
      console.log(err.response);
      this.$store.commit('deleteToken');
      this.$store.commit('deleteRefreshToken');
      this.$store.commit('deleteNickname');
      window.location.replace('/');
    });
  },
  methods: {
    lockInput(flag) {
      document.getElementById("post-url").disabled = flag;
      document.getElementById("post-tags").disabled = flag;
    },
    write() {
      if (this.url.length == 0 && this.tags.length == 0) {
        alert('URL/Tag를 입력해주세요.');
        return
      } else if (this.url.length < 10) {
        alert('유효한 URL을 입력해주세요.');
        return
      } else if (!this.url.startsWith('http://') && !this.url.startsWith('https://')) {
        alert('http:// 또는 https://로 시작하는 주소를 입력해주세요.');
        return
      }
      this.lockInput(true);

      var params = new URLSearchParams();
      params.append('url', this.url);
      params.append('tags', this.tags);

      axios.post(`${Endpoint.URL}/api/feeds/`, params, {
        headers: { Authorization: 'Bearer '+ this.$store.getters.getToken }
      })
      .then((res) => {
        window.location.replace('/');
      })
      .catch((err) => {
        this.lockInput(false);
        alert('글쓰기 실패');
        window.location.replace('/');
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
.post-url {
  display: grid;
  justify-items: center;
  width: 100%;
}
.post-tags {
  display: grid;
  justify-items: center;
  width: 100%;
}
.post-url textarea {
  border: none;
  font-size: 20px;
  padding: 8px;
  width: 100%;
  max-width: 800px;
  margin-top: 20px;
  margin-bottom: 20px;
  resize: none;
  border-radius: 10px;
  font-weight: 200;
}
.post-tags input {
  border: none;
  font-size: 20px;
  width: 100%;
  max-width: 800px;
  padding: 8px;
  border-radius: 10px;
  font-weight: 200;
}
.post-write {
  display: grid;
  width: 100%;
  max-width: 800px;
  margin-top: 20px;
  padding: 8px;
  background-color: #6196ff;
  color: white;
  font-weight: 600;
  cursor: pointer;
  border-radius: 10px;
  text-align: center;
  font-size: 22px;
}
.write-btn {
  display: none;
}
</style>