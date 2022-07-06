<template>
<div class="stan">
  <div class="stan-main">
    <h2>1 to INFINITY</h2>
    <div class="text-decoration-underline fw-bold text-primary" @click="[gameStart()]">[START]</div>
    <div class="fw-bold fs-3">
      {{this.seconds}}.{{this.mseconds}} 초
    </div>

    <h3> MISS:{{ $store.state.games.miss_inf}} </h3>
    <div>
      <span class="test" id="q">
        <span style="font-weight: bold; font-size: 2rem">{{ $store.state.games.numbers_now['q']}}</span>
      </span>
      <span class="test" id="w">
        <span style="font-weight: bold; font-size: 2rem">{{ $store.state.games.numbers_now['w']}}</span>
      </span>
      <span class="test" id="e">
        <span style="font-weight: bold; font-size: 2rem">{{ $store.state.games.numbers_now['e']}}</span>
      </span>
    </div>
    <div>
      <span class="test" id="a">
        <span style="font-weight: bold; font-size: 2rem">{{ $store.state.games.numbers_now['a']}}</span>
      </span>
      <span class="test" id="s">
        <span style="font-weight: bold; font-size: 2rem">{{ $store.state.games.numbers_now['s']}}</span>
      </span>
      <span class="test" id="d">
        <span style="font-weight: bold; font-size: 2rem">{{ $store.state.games.numbers_now['d']}}</span>
      </span>
    </div>
    <div>
      <span class="test" id="z">
        <span style="font-weight: bold; font-size: 2rem">{{ $store.state.games.numbers_now['z']}}</span>
      </span>
      <span class="test" id="x">
        <span style="font-weight: bold; font-size: 2rem">{{ $store.state.games.numbers_now['x']}}</span>
      </span>
      <span class="test" id="c">
        <span style="font-weight: bold; font-size: 2rem">{{ $store.state.games.numbers_now['c']}}</span>
      </span>
    </div>
  </div>
  <div class="stan-bottom">
    <h3>
       <button class="back" @click="[getGame('1to50main'), clearState(), clearEvent()]">Back</button>
    </h3>
    <h3>
      <button class="restart" @click="[gameStart()]">Restart</button>
    </h3>
  </div>
</div>
</template>

<script>
// import _ from 'lodash'
import { mapActions } from 'vuex'
export default {
  name: 'OneFiftyInf',
  data() {
    return {
      title: 'Timer',
      timer: null,
      totalTime: (1 * 6000),
      resetButton: false, 
      infKeyDown: function (e) {
        const key = document.getElementById(e.key);
        if (key) key.classList.add('pressed');
      },
      infKeyUp: (e) => {
        const key2 = document.getElementById(e.key);
        if (key2) key2.classList.remove('pressed');
        if (this.$store.state.games.numbers_now[e.key] == this.$store.state.games.number+1) {
          this.$store.commit('INF_NUM_SETTER', e.key)
          if (this.$store.state.games.number%9 == 0) {
            this.$store.commit('EXTENSION', this.$store.state.games.number)
          }
        } else if ((e.key in this.$store.state.games.numbers_now)) {
          this.$store.commit('COUNT_MISS_INF')
          this.totalTime -= 100
        }
        if (this.totalTime <= 0) {
          this.$store.commit('STANDARD_FINISHED')
          console.log('finished')
        }
      }
    }
  },
  methods: {
    ...mapActions(['clearState', 'getGame']),
    gameStart() {
      this.resetTimer()
      this.startTimer()
      this.$store.commit('START')
      this.$store.commit('SETTER')
      this.$store.commit('INF_NEXT_NUMS')
      document.addEventListener("keydown", this.infKeyDown);
      document.addEventListener("keyup", this.infKeyUp)
    },
    startTimer: function() {
      this.timer = setInterval(() => this.countdown(), 10);
      this.resetButton = true;
    },
    stopTimer: function() {
      clearInterval(this.timer);
      this.timer = null
      this.resetButton = true;
    },
    resetTimer: function() {
      this.totalTime = (1 * 6000);
      clearInterval(this.timer);
      this.timer = null;
      this.resetButton = false;
    },
    padTime: function(time) {
      return (time < 10 ? '0' : '') + time;
    },
    countdown: function() {
      if(this.totalTime >= 1) {
        this.totalTime--;
      } else {
        this.totalTime = 0;
        this.resetTimer;
      }
    },
  },
  created() {
    this.clearState()
    // this.gameStart()
  },
  computed: {
    seconds: function() {
      const seconds = Math.floor(this.totalTime/100 );
      return this.padTime(seconds);
    },
    mseconds: function() {
      const mseconds = this.totalTime - (this.seconds * 100);
      return this.padTime(mseconds);
    },
  },
  mounted() {
  }
}
</script>

<style>
/* div {
  margin: 80px;
} */
span {
  margin: 5px;
}
.stan{
  width: 70vh;
}
.test {
  font-size: 0.5rem;
  text-align: center;
  color: white;
  background: gray;
  border-radius: 1rem;
  padding: 1rem;
  transition: all .2s ease;
  margin-top: 3px;
}
.pressed {
  background: tomato;
  transform: scale(1.2);
}
.stan-bottom{
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-content: space-between;
  margin-top: 4vh;
}
.back{
  background-color: transparent !important;
  border: none;
}
.restart{
  background-color: transparent !important;
  border: none;
}
</style>