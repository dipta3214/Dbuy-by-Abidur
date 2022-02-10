import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    access: '',
    refresh: '',
    authenticated: false,
    id: '',
    username: ''
  },
  mutations: {
    initializeStore(state){
      if(localStorage.getItem('access')) {
        state.access = localStorage.getItem('access')
        state.refresh = localStorage.getItem('refresh')
        state.authenticated = true
        state.id = localStorage.getItem('id')
        state.username = localStorage.getItem('username')
      } else {
        state.access = ''
        state.refresh = ''
        state.authenticated = false
      }
    },
    setAccess(state, access) {
      state.access = access
      state.authenticated = true
    },
    setRefresh(state, refresh){
      state.refresh = refresh
    },
    setUserId(state, id){
      state.id = id
    },
    setUsername(state, username){
      state.username = username
    }
  },
  actions: {
  },
  modules: {
  }
})
