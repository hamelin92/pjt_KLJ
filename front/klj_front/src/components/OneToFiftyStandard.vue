<template>
<div class="stan">
  <div class="stan-main">
    <h2>Standard Mode</h2>
    <div style="background-color: brown; font-weight: bold;" @click="[gameStart(), startTimer()]">START</div>
    {{this.title}}
    {{this.minutes}}
    {{this.seconds}}
    <input type="button" @click="startTimer" value="start">
    <input type="button" @click="resetTimer" value="reset">
    <input type="button" @click="stopTimer" value="stop">
    <h1> MISS:{{ $store.state.games.miss}} </h1>
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
      <button class="restart" @click="[gameStart(), resetTimer(), startTimer()]">Restart</button>
    </h3>
  </div>
</div>
</template>

<script>
// import _ from 'lodash'
import { mapActions } from 'vuex'
export default {
  name: 'OneFifty',
  data() {
    return {
      title: 'Timer',
      timer: null,
      totalTime: (1 * 60),
      resetButton: false, 
      keyDown: function (e) {
        const key = document.getElementById(e.key);
        if (key) key.classList.add('pressed');
      },
      keyUp: (e) => {
        const key2 = document.getElementById(e.key);
        if (key2) key2.classList.remove('pressed');
        if (this.$store.state.games.numbers_now[e.key] == this.$store.state.games.number+1) {
          this.$store.commit('NUMBER_SETTER', e.key)
        } else if ((e.key in this.$store.state.games.numbers_now)) {
          this.$store.commit('COUNT_MISS')
        }
        if (this.$store.state.games.number == 50) {
          this.$store.commit('STANDARD_FINISHED')
          console.log('finished')
        }
      }
    }
  },
  methods: {
    ...mapActions(['clearState', 'getGame']),
    gameStart() { 
      this.$store.commit('START')
      this.$store.commit('SETTER')
      this.$store.commit('STAN_NEXT_NUMS')
      document.addEventListener("keydown", this.keyDown)
      document.addEventListener("keyup", this.keyUp)
    },
    startTimer: function() {
      this.timer = setInterval(() => this.countdown(), 1000);
      this.resetButton = true;
    },
    stopTimer: function() {
      clearInterval(this.timer);
      this.timer = null
      this.resetButton = true;
    },
    resetTimer: function() {
      this.totalTime = (1 * 60);
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
    clearEvent(){
      document.removeEventListener("keydown", this.eventFunc);
      document.removeEventListener("keyup", this.eventFunc2)
    },
  },
  created() {
    this.clearState()
    this.gameStart()
  },
  computed: {
    minutes: function() {
      const minutes = Math.floor(this.totalTime / 60);
      return this.padTime(minutes);
    },
    seconds: function() {
      const seconds = this.totalTime - (this.minutes * 60);
      return this.padTime(seconds);
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