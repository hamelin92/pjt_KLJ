<template>
  <div>
    article detail
    <comment-list></comment-list>
  </div>
</template>

<script>
import CommentList from "@/components/CommentList.vue"


export default {
  name: 'ArticleDetailView',
  components: { 
    CommentList 
    },
  
}
</script>

<style>
</style>