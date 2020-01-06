<template>
  <div>
    <FeedDetail :feeds="feeds"></FeedDetail>
  </div>
</template>

<script>
import axios from 'axios'
import FeedDetail from './FeedDetail.vue'

export default {
  name: 'Feed',
  components: {
    'FeedDetail': FeedDetail,
  },
  data() {
    return {
      feeds: null,
      next: '',
    }
  },
  mounted() {
    this.getFeeds()
  },
  methods: {
    getFeeds() {
      axios.get('http://127.0.0.1:5000/api/feeds/')
        .then((res) => {
          this.feeds = res.data;
        })
        .catch((err) => {
          alert("err");
        });
    },
  }
}
</script>