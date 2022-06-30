<template>
<div>
  <div>
    <div v-if="this.gameName == '1to50main'">
      <one-to-fifty-main></one-to-fifty-main>
    </div>
    <div v-if="this.gameName == '1to50'">
      <one-to-fifty-standard></one-to-fifty-standard>
    </div>
    <div></div>
  </div>
  <div v-if="this.gameName == '오목'">
    <omok-game></omok-game>
  </div>
  <div v-if="this.gameName == '노래퀴즈'">
    <song-quiz></song-quiz>
  </div>
</div>
</template>

<script>
import OneToFiftyMain from '@/components/OneToFiftyMain.vue'
import OneToFiftyStandard from '@/components/OneToFiftyStandard.vue'
import OmokGame from '@/components/OmokGame.vue'
import SongQuiz from '@/components/SongQuiz.vue'
// import RankList from '@/components/RankList.vue'

// import { mapGetters } from 'vuex'
export default {
  name: 'GameList',
  components: {
    OneToFiftyMain,
    OneToFiftyStandard,
    OmokGame,
    SongQuiz,
    // RankList,
  },
  computed: {
    // ...mapGetters(['gameName',]),
    gameName: function(){
      const name = this.$route.params.gamename
      return name
    }
  },
  
}
</script>

<style>

</style>