<template>
  <div>123</div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'Login',
    data() {
      return {
        code: null,
      }
    },
    mounted() {
      this.code = this.$route.query.code;
      this.getToken();
    },
    methods: {
      getToken() {
        axios.get('http://localhost:8000/oauth/github/login?code=' + this.code)
          .then((res) => {
            localStorage.setItem('token', res.data.token);
            localStorage.setItem('refreshToken', res.data.refresh_token);
            window.location.replace('/');
          })
          .catch((err) => {
            alert("로그인 실패");
          });
      }
    }
}
</script>

<style scoped>

</style>