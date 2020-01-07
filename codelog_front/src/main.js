import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import Feed from './components/Feed.vue'
import Tag from './components/Tag.vue'
import Search from './components/Search.vue'
import Write from './components/Write.vue'
import Login from './components/Login.vue'

Vue.config.productionTip = false
Vue.use(VueRouter)

const router = new VueRouter({
  mode: 'history',
  routes: [
    {
      path: '/',
      component: Feed
    },
    {
      path: '/tags',
      component: Tag
    },
    {
      path: '/search',
      component: Search
    },
    {
      path: '/write',
      component: Write
    },
    {
      path: '/login',
      component: Login
    },
  ]
})  

new Vue({
  render: h => h(App),
  router
}).$mount('#app')