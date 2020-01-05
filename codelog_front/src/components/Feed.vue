<template>
  <div class="feed">
    <div class="feed-top">
      <div class="feed-top-right">
        <div class="feed-writer">
          Hide
        </div>
        <div class="feed-date">
          2020-01-01 10:10:10
        </div>
        <div class="feed-body">
          <a href="#">http://naver.com?????</a>
        </div>
        <div class="feed-tag">
          #Go, #Python
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
.feed {
  display: grid;
  background-color: white;
  border-radius: 5px;
  box-shadow: 0px 0px 0px white inset, 0 0 3px rgba(0, 0, 0, 0.2);
  padding: 10px;
  margin: 10px;
}

.feed-writer {
  display: grid;
  align-items: center;
  font-weight: 600;
}

.feed-date {
  display: grid;
  align-items: center;
  padding-bottom: 5px;
  font-size: 13px;
}

.feed-body {
  font-size: 20px;
  padding-top: 5px;
}
.feed-body a {
  text-decoration: none;
  color: #2e2182;
  font-weight: 600;
}
.feed-body a:hover {
  color: #4e37de;
}

.feed-tag {
  padding-top: 10px;
  font-size: 14px;
  color: #878787;
}
</style>