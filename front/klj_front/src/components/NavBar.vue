<template>
  <div>
    <nav>
      <div class="top">
        <div class="game_top">
          <b-dropdown size="lg" id="dropdown" text="메뉴" class="m-md-2">
            <b-dropdown-item >
                <router-link to="/" class="fw-bold fs-5"><div>홈</div></router-link> 
            </b-dropdown-item>
            <b-dropdown-item>
              <router-link to="/games" class="fw-bold fs-5"><div @click="getGame('1to50')">1to50</div></router-link>
            </b-dropdown-item>
            <b-dropdown-item>
              <router-link to="/games" class="fw-bold fs-5"><div @click="getGame('오목')">오목</div></router-link>
            </b-dropdown-item>
            <b-dropdown-item>
              <router-link to="/games" class="fw-bold fs-5"><div @click="getGame('노래퀴즈')">노래퀴즈</div></router-link>
            </b-dropdown-item>
          </b-dropdown>
        </div>
        <div class="title_top">
          <div class="main_title">
            <h1 class="fw-bold">미니게임천국(임시)</h1>
          </div>
        </div>
        <div class="account_top">
          <div v-if="!isLoggedIn">
            <router-link to="login" class="text-decoration-none fw-bold fs-2 text-dark"><div>로그인</div></router-link>
            <router-link to="signup" class="text-decoration-none fw-bold fs-2 text-dark"><div>회원가입</div></router-link>
          </div>
          <router-link right v-if="isLoggedIn" to="logout" class="text-decoration-none fw-bold fs-2 text-dark"><div>로그아웃</div></router-link>
        </div>
      </div>
    </nav>
  </div>
</template>
<script>
  import { mapGetters, mapActions } from 'vuex'
  export default {
    name: 'NavBar',
    computed: {
      ...mapGetters(['isLoggedIn'])
    },
    methods: {
      ...mapActions(['getGame',])
    }

  }
</script>


<style>
.top{
  display : flex;
  flex-direction: row;
  justify-content: space-between;
  margin-top : 20px;
}
.main_title{

}
.account_top{
  width : 10vw;
}
</style>
