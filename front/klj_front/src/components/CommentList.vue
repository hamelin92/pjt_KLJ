<template>
  <div>
    comment list
    <comment-list-form></comment-list-form>
    <comment-list-item></comment-list-item>
  </div>
</template>

<script>
import CommentListForm from './CommentListForm.vue'
import CommentListItem from './CommentListItem.vue'

export default {
  components: { CommentListForm,
   CommentListItem 
   },

}
</script>

<style>

</style>