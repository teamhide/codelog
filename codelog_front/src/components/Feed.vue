<template>
  <div class="feed-container">
    <div class="feed">
      <div class="feed-top">
        <div class="feed-top-left">
          <div class="feed-writer">
            Hide
          </div>
          <div class="feed-date">
            2010-01-10 10:12:00
          </div>
        </div>
        <div class="feed-top-right">
          <div class="feed-top-btn"></div>
        </div>
      </div>
      <div class="feed-image">
        <img />
      </div>
      <div class="feed-body">
        <div class="feed-title">
          Profile
        </div>
        <div class="feed-description">
          풀스택 개발자라는 용어가 가끔...
        </div>
        <div class="feed-url">
          http://hides.kr
        </div>
      </div>
    </div>
    <div class="feed">
      <div class="feed-top">
        <div class="feed-top-left">
          <div class="feed-writer">
            Hide
          </div>
          <div class="feed-date">
            2010-01-10 10:12:00
          </div>
        </div>
        <div class="feed-top-right">
          <div class="feed-top-btn"></div>
        </div>
      </div>
      <div class="feed-image">
        <img />
      </div>
      <div class="feed-body">
        <div class="feed-title">
          Profile
        </div>
        <div class="feed-description">
          풀스택 개발자라는 용어가 가끔...
        </div>
        <div class="feed-url">
          http://hides.kr
        </div>
      </div>
    </div>
    <div class="feed">
      <div class="feed-top">
        <div class="feed-top-left">
          <div class="feed-writer">
            Hide
          </div>
          <div class="feed-date">
            2010-01-10 10:12:00
          </div>
        </div>
        <div class="feed-top-right">
          <div class="feed-top-btn"></div>
        </div>
      </div>
      <div class="feed-image">
        <img />
      </div>
      <div class="feed-body">
        <div class="feed-title">
          Profile
        </div>
        <div class="feed-description">
          풀스택 개발자라는 용어가 가끔...
        </div>
        <div class="feed-url">
          http://hides.kr
        </div>
      </div>
    </div>
    <div class="feed">
      <div class="feed-top">
        <div class="feed-top-left">
          <div class="feed-writer">
            Hide
          </div>
          <div class="feed-date">
            2010-01-10 10:12:00
          </div>
        </div>
        <div class="feed-top-right">
          <div class="feed-top-btn"></div>
        </div>
      </div>
      <div class="feed-image">
        <img />
      </div>
      <div class="feed-body">
        <div class="feed-title">
          Profile
        </div>
        <div class="feed-description">
          풀스택 개발자라는 용어가 가끔...
        </div>
        <div class="feed-url">
          http://hides.kr
        </div>
      </div>
    </div>
    <div class="feed">
      <div class="feed-top">
        <div class="feed-top-left">
          <div class="feed-writer">
            Hide
          </div>
          <div class="feed-date">
            2010-01-10 10:12:00
          </div>
        </div>
        <div class="feed-top-right">
          <div class="feed-top-btn"></div>
        </div>
      </div>
      <div class="feed-image">
        <img />
      </div>
      <div class="feed-body">
        <div class="feed-title">
          Profile
        </div>
        <div class="feed-description">
          풀스택 개발자라는 용어가 가끔...
        </div>
        <div class="feed-url">
          http://hides.kr
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Feed'
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
.feed-image img {
  background: url("../assets/hide.png") no-repeat;
  background-size: cover;
  background-position: center;
  width: 100%;
  height: 100%;
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
@media screen and (max-width: 510px){
    .feed{
        width: 100%;
        height: 500;
    }
    .feed-image {
      width: 100%;
      height: 250px;
    }
}
</style>