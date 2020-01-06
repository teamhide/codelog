<template>
  <div class="search-container">
    <input v-model=keyword v-on:keyup.enter=searchFeeds type="text" class="search-bar" placeholder="검색어를 입력하세요."/>
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
      keyword: null,
      offset: null,
    }
  },
  methods: {
    getFeeds() {
      axios.get('http://127.0.0.1:5000/api/feeds/search/?offset=1&keyword=' + this.keyword)
        .then((res) => {
          this.feeds = res.data;
        })
        .catch((err) => {
          alert("검색어는 2글자 이상이어야 합니다.");
        });
    },
    searchFeeds() {
      this.feeds = null;
      this.getFeeds()
    }
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