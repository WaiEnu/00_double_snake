import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    length:'100',
  },
  getters: {
    getLength(state){
      return state.length
    }
  },
  mutations: {
    setLength(state,payload){
      state.length = payload.length
    }
  },
  actions: {
    setLength({ commit }){
      commit('setLength')
    },
  },
  modules: {
  }
})
