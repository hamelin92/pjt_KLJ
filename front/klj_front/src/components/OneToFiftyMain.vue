<template>
  <div class="onetofiftymain">
    <button class="standard" @click="getGame('1to50standard')">Standard</button>
    <button class="infinity">Infinity</button>
  </div>
</template>

<script>
import { mapActions } from 'vuex'
export default {
  name: 'OneToFiftyMain',
  methods:{
    ...mapActions(['getGame']),
  }
}
</script>

<style>
.onetofiftymain{
  display: flex;
  flex-direction: column;
  align-items: center;
  
}
.standard{
  width: 25vw;
  height: 13vh;
  margin: 5vh;
}
.infinity{
  width: 25vw;
  height: 13vh;
  margin: 5vh;
}
</style>