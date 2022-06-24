<template>
  <div>
    <nav>
      <div class="top">
        <div class="game_top">
          <b-dropdown size="lg" id="dropdown" text="게임들 " class="m-md-2">
            <b-dropdown-item >
                <router-link to="/" class="fw-bold fs-5"><div>홈</div></router-link> 
            </b-dropdown-item>
            <b-dropdown-item>
              <router-link to="/games" class="fw-bold fs-5"><div>1to50</div></router-link>
            </b-dropdown-item>
            <b-dropdown-item>
              <router-link to="/OmokGame" class="fw-bold fs-5"><div>오목</div></router-link>
            </b-dropdown-item>
            <b-dropdown-item>
              <router-link to="/SongQuiz" class="fw-bold fs-5"><div>노래퀴즈</div></router-link>
            </b-dropdown-item>
          </b-dropdown>
        </div>
        <div class="title_top">
          <div class="main_title">
            <h1 class="fw-bold">미니게임천국(임시)</h1>
          </div>
        </div>
        <div class="account_top">
          <router-link to="#" class="text-decoration-none fw-bold fs-2 text-dark"><div class=" ">로그인</div></router-link>
        </div>
      </div>
    </nav>
  </div>
</template>
<script>
  export default {
    name: 'NavBar',
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
