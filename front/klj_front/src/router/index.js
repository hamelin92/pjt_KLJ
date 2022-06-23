import Vue from 'vue'
import VueRouter from 'vue-router'

import MainView from '@/views/MainView.vue'
import GameView from '@/views/GameView.vue'
// import OmokGame from '@/views/ArticleDetailView.vue'
// import SingingQuiz from '@/views/SingingQuiz.vue'
// import OneToFifty from '@/components/OneToFifty.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'mainview',
    component: MainView
  },
  // {
  //   path: '/OneToFifty',
  //   name: 'onetofifty',
  //   component: OneToFifty
  // },
  // {
  //   path: '/OmokGame',
  //   name: 'omokgame',
  //   component: OmokGame
  // },
  // {
  //   path: '/SingingQuiz',
  //   name: 'singingquiz',
  //   component: SingingQuiz
  // },
  {
    path: '/games',
    name: 'gameview',
    component: GameView
  },
  
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})


// router.beforeEach((to, from, next) => {
//   // 이전 페이지에서 발생한 에러메시지 삭제
//   store.commit('SET_AUTH_ERROR', null)

//   const { isLoggedIn } = store.getters

//   const noAuthPages = ['login', 'signup',]

//   const isAuthRequired = !noAuthPages.includes(to.name)

//   if (isAuthRequired && !isLoggedIn) {
//     alert('로그인이 필요합니다.')
//     next({ name: 'login' })
//   } else {
//     next()
//   }
  
//   if (!isAuthRequired && isLoggedIn) {
//     next({ name: 'main' })
//   }
// })

// /*
// Navigation Guard 설정
//   (이전 페이지에서 있던 에러 메시지 삭제)

//   로그인(Authentication)이 필요 없는 route 이름들 저장(/login, /signup)

//   0. router 에서 이동 감지

//   1. 현재 이동하고자 하는 페이지가 로그인이 필요한지 확인
  
//   2. 로그인이 필요한 페이지인데 로그인이 되어있지 않다면
//     로그인 페이지(/login)로 이동

//   3. 로그인이 되어 있다면
//     원래 이동할 곳으로 이동
  
//   4. 로그인이 되어있는데 /login, /signup 페이지로 이동한다면
//     메인 페이지(/)로 이동
    

// */


export default router
