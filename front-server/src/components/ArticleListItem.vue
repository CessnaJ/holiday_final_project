<!-- <template>
  <div>    
    <div @click="goArticleDetail">
      <div class="comment-list-item-name">
        <div class="w1" >{{ article.id }}</div> 
        <div class="w2">{{ article.title }}</div>
        <div class="w3">{{ article.username }}</div>
        <div class="w4">{{articleCreatedAt}}</div>
      </div>
  </div>

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
.comment-list-item {
  display: flex;
  justify-content: space-between;
  padding-bottom: 1em;
}
.comment-list-item-name {
  display: flex;
  flex-direction: row;
  align-items: center;
  border: 0.5px solid whitesmoke;
  padding: 1em;
}
.w1 {
  width: 20%;
}
.w2 {
  width: 30%;
}
.w3 {
  width: 20%;
  font-weight: bold;
}
.w4 {
  width: 30%;
}

</style> -->