import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export const store = new Vuex.Store({
  state: {
    token: localStorage.getItem('token'),
    refreshToken: localStorage.getItem('refreshToken'),
    nickname: localStorage.getItem('nickname'),
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
    },
    getNickname(state) {
      state.nickname = localStorage.getItem('nickname');
    },
    deleteNickname(state) {
      localStorage.removeItem('nickname');
      state.nickname = null;
    },
  },
  actions: {
    
  }
})