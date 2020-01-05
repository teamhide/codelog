import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import Feed from './components/Feed.vue'
import Tag from './components/Tag.vue'

Vue.config.productionTip = false
Vue.use(VueRouter)

const router = new VueRouter({
  routes: [
      {
          path: '/',
          component: Feed
      },
      {
          path: '/tags',
          component: Tag
      }
  ]
})  

new Vue({
  render: h => h(App),
  router
}).$mount('#app')