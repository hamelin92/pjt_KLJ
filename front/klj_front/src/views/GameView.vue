<template>
  <div>
    <div class="mid">
      <div class="blank">
        빈 자리
      </div>
      <div class="game">
        <div class="game_title">
          게임 타이틀
        </div>
        <div class="game_page">
          <one-to-fifty></one-to-fifty>
          <omok-game></omok-game>
          <song-quiz></song-quiz>
          게임 들어가는 자리
        </div>
      </div>
      <div class="ranking">
        <rank-list></rank-list>
        랭킹 들어가는 자리
      </div>
    </div>
  </div>
</template>

<script>
import OneToFifty from '@/components/OneToFifty.vue'
import OmokGame from '@/components/OmokGame.vue'
import SongQuiz from '@/components/SongQuiz.vue'
import RankList from '@/components/RankList.vue'

export default {
  name: 'GameView',
  components: {
    OneToFifty,
    OmokGame,
    SongQuiz,
    RankList,
  }
  
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
  display : flex;
  flex-direction: column;
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
  justify-content: center;
  align-items: center;
}
.game_title{
  border : 2px solid darkblue;
  width : 15rem;
  height : 2rem;
  margin-top : 50px;
}
.game_page{
  border : 2px solid brown;
  width : 60vw;
  height : 50vh;
  margin-top : 50px;
}
.ranking{
  border : 2px solid pink;
  width : 10vw;
  height : 50vh;
}
</style>