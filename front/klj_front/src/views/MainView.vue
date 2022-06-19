<template>
  <div>
    <div class="top">
      <div class="game_top">
        <b-dropdown id="dropdown-1" text="게임들" class="m-md-2">
          <b-dropdown-item >
              <router-link to="/">홈</router-link> 
          </b-dropdown-item>
          <b-dropdown-item>
            <router-link to="/OneToFifty">1to50</router-link>
          </b-dropdown-item>
          <b-dropdown-item>
            <router-link to="/OmokGame">오목</router-link>
          </b-dropdown-item>
          <b-dropdown-item>
            <router-link to="/SingingQuiz">노래퀴즈</router-link>
          </b-dropdown-item>
          <b-dropdown-divider></b-dropdown-divider>
          <b-dropdown-item active>Active action</b-dropdown-item>
          <b-dropdown-item disabled>Disabled action</b-dropdown-item>
        </b-dropdown>
      </div>
      <div class="title_top">
        <div class="main_title">
          미니게임천국
        </div>
      </div>
      <div class="account_top">
        로그인하는 유저
      </div>
    </div>
    <div class="mid">
      <div class="community">
        게시판
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'MainView',
  
}
</script>

<style scoped>
.top{
  display : flex;
  flex-direction: row;
  justify-content: space-between;
  margin-top : 20px;
}
.game_top{
  
}
.title_top{
  
}
.main_title{
  border : 2px solid green;
  width : 30vw;
  height : 3rem;
}

.account_top{
  border : 2px solid black;
  width : 10vw;
  height : 2rem;
}
.mid{
  display : flex;
  justify-content: center;
  align-items: center;
}
.community{
  border : 2px solid brown;
  width : 60vw;
  height : 50vh;
  margin-top : 100px;
}
</style>