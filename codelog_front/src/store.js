import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export const store = new Vuex.Store({
  state: {
    token: localStorage.getItem('token'),
    refreshToken: localStorage.getItem('refreshToken'),
  },
  mutations: {
    getToken(state) {
      state.token = localStorage.getItem('token');
    },
    deleteToken(state) {
      localStorage.removeItem('token');
      state.token = null;
    },
    getRefreshToken(state) {
      state.refreshToken = localStorage.getItem('refreshToken');
    },
    deleteRefreshToken(state) {
      localStorage.removeItem('refreshToken');
      state.refreshToken = null;
    }
  },
  actions: {
    
  }
})