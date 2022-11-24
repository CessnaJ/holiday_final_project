<template>
  <div>
    <div>
      <div class="page-title">
        <h2>holiday 커뮤니티</h2>
      </div>
      <button @click="goCreate">글 작성</button>
    </div>
    
    <div class="outer">
      <div>
        <CommunityList/>
      </div>
    </div>
    
  </div>
</template>

<script>
import CommunityList from '@/components/CommunityList'

export default {
    name: 'CommunityView',
    components: {
        CommunityList,
    },
    data(){
      return{
        articles:this.$store.state.articles
      }
    }
    ,
    created() {
        this.getArticles()
    },
    methods: {
        getArticles() {
            this.$store.dispatch('getArticles')
        },
        goCreate() {
          this.$router.push({name: 'articlecreate'})
        }
    }
}
</script>

<style>
.page-title {
  margin-bottom: 30px;
  margin-top: 30px;
}
.container {
  width: 1100px;
  margin: 0 auto;
}
.outer {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 40px;
}


</style>