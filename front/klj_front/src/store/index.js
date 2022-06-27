import Vue from 'vue'
import Vuex from 'vuex'

import accounts from './modules/accounts'
import games from './modules/games'
Vue.use(Vuex)

export default new Vuex.Store({
  modules: { accounts, games },
})