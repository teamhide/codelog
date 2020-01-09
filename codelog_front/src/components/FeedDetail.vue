<template>
  <div>
    <div class="feed-container">
      <div class="feed" v-for="feed in feeds" v-bind:key="feed.id">
        <div class="feed-top">
          <div class="feed-top-left">
            <div class="feed-writer">
              {{ feed.nickname !== null && getBufferSize(feed.nickname) < 20 ? feed.nickname : feed.nickname.substr(0, 20) + "..." }}
            </div>
            <div class="feed-date">
              {{ feed.created_at }}
            </div>
          </div>
          <div v-if="feed.nickname !== null && $store.state.nickname == feed.nickname" class="feed-top-right">
            <!-- <button v-on:click="myFunction" class="feed-top-btn"></button>
              <div id="myDropdown" class="dropdown-content">
                <a href="#">Modify</a>
                <a href="#">Delete</a>
              </div> -->
          </div>
        </div>
        <div class="feed-image">
          <template v-if="feed.image !== null">
            <a :href="''+feed.url+''" target="_blank"><img :src="''+feed.image+''" width="100%" height="100%" style="background-size: cover; background-position: center;" /></a>
          </template>
          <template v-else>
            <a :href="''+feed.url+''" target="_blank"><img src="../assets/no-image.jpg" width="100%" height="100%" style="background-size: cover; background-position: center;" /></a>
          </template>
        </div>
        <div class="feed-body">
          <div class="feed-title">
              {{
                feed.title !== null ?
                getBufferSize(feed.title) < 22 ? feed.title : feed.title.substr(0, 22) : 
                "No title"
               }}
          </div>
          <div class="feed-description">
            {{
              feed.description !== null ?
              getBufferSize(feed.description) < 21 ? feed.description : feed.description.substr(0, 21) + "..." :
              "No description"
            }}
          </div>
          <div class="feed-url">
            <a :href="''+feed.url+''" target="_blank">{{ getBufferSize(feed.url) < 32 ? feed.url : feed.url.substr(0, 32) + "..." }}</a>
          </div>
        </div>
      </div>
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
      getBufferSize(str) {
        var b = str.match("/[^\x00-\xff]/g");
        return (str.length + (!b ? 0: b.length)); 
      },
      myFunction() {
        document.getElementById("myDropdown").classList.toggle("show");
      },
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
  border: none;
  cursor: pointer;
}
/* Dropdown button on hover & focus */
.feed-top-btn:hover, .feed-top-btn:focus {

}

/* The container <div> - needed to position the dropdown content */
.dropdown {
  position: relative;
  display: inline-block;
}

/* Dropdown Content (Hidden by Default) */
.dropdown-content {
  display: none;
  position: absolute;
  background-color: #f1f1f1;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  z-index: 1;
}

/* Links inside the dropdown */
.dropdown-content a {
  color: black;
  padding: 10px;
  text-decoration: none;
  display: block;
}

/* Change color of dropdown links on hover */
.dropdown-content a:hover {background-color: #ddd}

/* Show the dropdown menu (use JS to add this class to the .dropdown-content container when the user clicks on the dropdown button) */
.show {
  display:block;
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
.feed-url a {
  text-decoration: none;
}
.feed-body {
  padding: 10px;
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