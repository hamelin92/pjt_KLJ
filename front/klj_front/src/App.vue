<template>
  <div id="app">
    <nav-bar></nav-bar>
    <router-view/>
  </div>
</template>
<script>
import NavBar from '@/components/NavBar.vue'

export default {
  name: 'App',
  components: {
    NavBar,
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
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
