<template>
<div>
  <div>
    <div v-if="gameName == '1to50main'">
      <one-to-fifty-main></one-to-fifty-main>
    </div>
    <div v-if="gameName == '1to50standard'">
      <one-to-fifty-standard></one-to-fifty-standard>
    </div>
    <div></div>
  </div>
  <div v-if="gameName == '오목'">
    <omok-game></omok-game>
  </div>
  <div v-if="gameName == '노래퀴즈'">
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

import { mapGetters } from 'vuex'
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
    ...mapGetters(['gameName',])
  }
}
</script>

<style>

</style>