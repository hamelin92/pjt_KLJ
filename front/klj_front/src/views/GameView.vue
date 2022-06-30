<template>
  <div>
    <div class="mid">
      <div class="blank">
      </div>
      <div class="game">
        <div class="game_title">
          {{this.gamename}}
        </div>
        <div class="game_page">
         <game-list></game-list>
        </div>
      </div>
      <div class="ranking">
       
        랭킹 들어가는 자리
      </div>
    </div>
  </div>
</template>

<script>
import GameList from '@/views/GameList.vue'

export default {
  name: 'GameView',
  components: {
   GameList,
  },
  computed: {
    gamename(){
      return this.$route.params.gamename
    } 
  },
  

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
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: white;
  border : 2px solid brown;
  width : 65vw;
  height : 55vh;
  margin-top : 50px;
}
.ranking{
  border : 2px solid pink;
  width : 10vw;
  height : 50vh;
}
</style>