<template>
  <section>
    <div class="feed">
      <div class="feed-top">
        <div class="feed-icon">
          icon
        </div>
        <div class="feed-top-right">
          <div class="feed-subject">
            subject
          </div>
          <div class="feed-writer">
            hide
          </div>
          <div class="feed-body">
            http://naver.com
          </div>
          <div class="feed-date">
            2020-01-01 12:10:10
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'Section'
}
</script>

<style scoped>
section {
  padding: 20px;
}
.feed {
  display: grid;
  background-color: white;
  border-radius: 5px;
  box-shadow: 0px 0px 0px white inset, 0 0 10px rgba(0, 0, 0, 0.2);
}

.feed-top {
  display: grid;
  grid-template-columns: 80px auto;
}

.feed-icon {
  display: grid;
  justify-content: center;
  align-items: center;
}

.feed-subject {
  display: grid;
  align-items: center;
  font-weight: 600;
  font-size: 20px;
}

.feed-writer {
  display: grid;
  align-items: center;
}
</style>