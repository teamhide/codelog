<template>
  <div>
    <div class="feed-container">
      <div class="feed" v-for="feed in feeds" v-bind:key="feed.id">
        <div class="feed-top">
          <div class="feed-top-left">
            <div class="feed-writer">
              {{ feed.nickname.length < 20 ? feed.nickname : feed.nickname.substr(0, 20) + "..." }}
            </div>
            <div class="feed-date">
              {{ feed.created_at }}
            </div>
          </div>
          <div class="feed-top-right">
            <div class="feed-top-btn"></div>
          </div>
        </div>
        <div class="feed-image">
          <a :href="''+feed.url+''" target="_blank"><img :src="''+feed.image+''" width="100%" height="100%" style="background-size: cover; background-position: center;" /></a>
        </div>
        <div class="feed-body">
          <div class="feed-title">
            {{ feed.title.length < 28 ? feed.title : feed.title.substr(0, 28) + "..." }}
          </div>
          <div class="feed-description">
            {{ feed.description.length < 26 ? feed.description : feed.description.substr(0, 26) + "..." }}
          </div>
          <div class="feed-url">
            {{ feed.url.length < 28 ? feed.url : feed.url.substr(0, 28) + "..." }}
          </div>
        </div>
      </div>
    </div>
    <div v-if="this.feeds" class="load-feed">
      <a v-on:click=getFeeds>Load more</a>
    </div>
  </div>
</template>

<script>
export default {
    name: 'FeedDetail',
    props: {
        feeds: Array
    },
    methods: {
        test() {
            alert(this.feeds)
        }
    }
}
</script>

<style scoped>
.feed-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}
.feed {
  display: grid;
  margin: 10px;
  background-color: white;
  border-radius: 5px;
  box-shadow: 0px 0px 0px white inset, 0 0 3px rgba(0, 0, 0, 0.2);
}
.feed-top {
  display: grid;
  grid-template-columns: auto 20px;
  padding: 10px;
}
.feed-top-right {
  display: grid;
  justify-items: center;
}
.feed-top-btn {
  height: 15px;
  width: 15px;
  background: url("../assets/menu-icon.svg") no-repeat;
  background-size: cover;
  background-position: center;
}
.feed-writer {
  display: grid;
  align-items: center;
  font-weight: 600;
}
.feed-date {
  display: grid;
  align-items: center;
  font-size: 13px;
  color: #878787;
}
.feed-image {
  width: 250px;
  height: 150px;
}
.feed-description {
  font-size: 14px;
  color: #878787;
}
.feed-url {
  font-size: 13px;
}
.feed-body {
  padding: 10px;
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
@media screen and (max-width: 510px){
    .feed{
        width: 100%;
        height: 500;
    }
    .feed-image {
      width: 100%;
      height: 250px;
    }
    .feed-top-btn {
        height: 20px;
        width: 20px;
    }
}
</style>