// import router from '@/router'
// import axios from 'axios'
// import drf from '@/api/drf'

// state에 직접 접근하지 않고 getters를 통해서만 접근하는 방식으로 진행!
export default {
  state: {
    gameName : '',
  },
  getters: {
    gameName: state => state.gameName,
  },
  mutations: {
    SET_GAMENAME: (state, name) => state.gameName = name,
  },
  actions: {
    getGame({ commit }, gamename){
      const name = gamename
      commit('SET_GAMENAME', name)
    }
    },

}
