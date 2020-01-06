<template>
  <div class="search-container">
    <input v-on:keyup.enter=getFeeds type="text" class="search-bar" placeholder="검색어를 입력하세요."/>
    <FeedDetail :feeds="feeds"></FeedDetail>
  </div>
</template>

<script>
import axios from 'axios'
import FeedDetail from './FeedDetail.vue'

export default {
  name: 'Search',
  components: {
    'FeedDetail': FeedDetail,
  },
  data() {
    return {
      feeds: null,
    }
  },
  methods: {
    getFeeds() {
      axios.get('http://127.0.0.1:5000/api/feeds/')
        .then((res) => {
          this.feeds = res.data;
        })
        .catch((err) => {
          alert(err);
        });
    },
  }
}
</script>

<style scoped>
.search-container {
  display: grid;
  justify-items: center;
}
.search-bar {
  height: 50px;
  border: none;
  padding: 10px;
  font-size: 20px;
  border-radius: 20px;
  width: 90%;
  max-width: 960px;
}
</style>