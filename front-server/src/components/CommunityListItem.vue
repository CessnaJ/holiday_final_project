<template>
  <div @click="goArticleDetail">
    <span>
      <p>{{ article.id }} {{ article.title }}</p>
    </span>
    <span></span>
    <span><p>작성자 : {{ article.username }}</p></span>
    <span><p>{{articleCreatedAt}}</p></span>
    <hr>
  </div>
</template>

<script>
export default {
    name: 'CommunityListItem',
    props: {
        article: Object
    },
    computed:{
      // 작성시간을 로컬로 변환해주는 함수
      articleCreatedAt(){
        const article = this.article
        const createdAt = new Date(article?.created_at).toLocaleString()
        return createdAt
      }
    },
    methods: {
      goArticleDetail() {
        this.$router.push({ name: 'articledetail',params:{id:this.article.id}})
      }
    }

}
</script>

<style>

</style>