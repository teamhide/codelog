<template>
  <div class="search-container">
    <input v-model="keyword" v-on:keyup.enter="searchFeeds" type="text" class="search-bar" placeholder="검색어를 입력하세요."/>
    <FeedDetail :feeds="feeds"></FeedDetail>
    <div v-if="this.isRemain" class="load-feed">
      <a v-on:click="loadMore">Load more</a>
    </div>
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
      prev: null,
      isRemain: false,
    }
  },
  methods: {
    async getFeeds() {
      var url = 'http://127.0.0.1:5000/api/feeds/search?keyword=' + this.keyword
      let data;

      if(this.prev) {
        url += '&prev=' + this.prev
      }
      
      await axios.get(url)
        .then((res) => {
          data = res.data;
        })
        .catch((err) => {
          alert("검색어는 2글자 이상이어야 합니다.");
        });

      return data;
    },
    async searchFeeds() {
      this.feeds = await this.getFeeds();
      if (this.feeds.length > 0) {
        this.isRemain = true;
      }
    },
    async loadMore() {
      this.prev = this.feeds[this.feeds.length - 1].id
      var data = await this.getFeeds();

      if (data.length > 0) {
        data.forEach((value, index) => {
          this.feeds.push(value);
        })
        this.isRemain = true;
      } else {
        this.isRemain = false;
      }
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
.load-feed {
  margin-top: 15px;
  text-align: center;
}
.load-feed a {
  text-decoration: none;
  color: black;
  border: 1px solid lightgray;
  padding: 10px;
  border-radius: 15px;
}
.load-feed a:hover {
  background-color: #6196ff;
  color: white;
}
</style>