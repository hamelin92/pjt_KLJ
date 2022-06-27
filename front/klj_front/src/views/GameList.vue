<template>
<div>
  <div v-if="gameName == '1to50'">
    <one-to-fifty></one-to-fifty>
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
import OneToFifty from '@/components/OneToFifty.vue'
import OmokGame from '@/components/OmokGame.vue'
import SongQuiz from '@/components/SongQuiz.vue'
// import RankList from '@/components/RankList.vue'

import { mapGetters } from 'vuex'
export default {
  name: 'GameList',
  components: {
    OneToFifty,
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