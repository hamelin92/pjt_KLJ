<template>
  <div>
    <div class="mid">
      <div class="community">
        <article-list></article-list>
        게시판
      </div>
    </div>
  </div>
</template>

<script>
import ArticleList from '@/components/ArticleList.vue'

export default {
  name: 'MainView',
  components: {
    ArticleList,
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
  justify-content: center;
  align-items: center;
}
.community{
  border : 2px solid brown;
  width : 60vw;
  height : 50vh;
  margin-top : 100px;
}
</style>