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
      <div class="blank">
        빈 자리
      </div>
      <div class="game">
        <div class="game_title">
          게임 타이틀
        </div>
        <div class="game_page">
          게임 들어가는 자리
        </div>
      </div>
      <div class="ranking_blank">
        빈 자리
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
}
.game_top{
  border : 2px solid red;
  width : 2rem;
  height : 2rem;
}
.title_top{
  display : flex;
  flex-direction: column;
}
.main_title{
  border : 2px solid green;
  width : 2rem;
  height : 2rem;
}
.account_top{
  border : 2px solid black;
  width : 2rem;
  height : 2rem;
}
.mid{
  display : flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
}
.blank{
  width : 4rem;
  height : 3rem;
}
.game{
  display : flex;
  flex-direction: column;
}
.game_title{
  border : 2px solid darkblue;
  width : 2rem;
  height : 2rem;
}
.game_page{
  border : 2px solid brown;
  width : 2rem;
  height : 2rem;
}
.ranking_blank{
  width : 4rem;
  height : 2rem;
}
</style>