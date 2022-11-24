<template>
  <div>
    <h1>게시글 디테일</h1>
    <p>글 번호: {{thisArt.id}}</p>
    <p>글 제목: {{thisArt.title}}</p>
    <p>글 내용: {{thisArt.content}}</p>
    <button @click="deleteArticle">삭제</button>
    
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
    name: 'ArticleDetailView',
    created() {
        this.thisArticle = this.getArticleDetail
    },
    data(){
      return{
        thisArt : this.$store.state.articles.filter((a)=>{return(Number(a.id)===Number(this.$route.params.id))})[0],
      }
    },

    methods:{
      getArticleDetail() {
        this.$store.dispatch('getArticles')
      },
 
      deleteArticle() {
        axios({
              method: 'delete',
              url: `${API_URL}/community/${this.$route.params.id}`,
              headers: {
                
              Authorization: `Token ${this.$store.state.token}`
            },
              data:{
                user:this.thisArt.user
              }
            })
              .then((res) => {
                console.log(res)
                this.$store.dispatch('getArticles')
                alert('게시글이 삭제되었습니다')
                this.$router.push({name: 'community'})
              })
              .catch((err) => {
                alert('작성자가 아닙니다. 어서 꺼지세요')
                this.$router.push({name: 'community'})
                console.log(err)
              })



        // if (this.$store.getters.isLogin === true) {
        //   if(this.$store.state.user === this.thisArt.user) {
        //     axios({
        //       method: 'delete',
        //       url: `${API_URL}/community/${this.$route.params.id}`,
        //       headers: {
        //       Authorization: `Token ${this.$store.state.token}`
        //     }
        //     })
        //       .then((res) => {
        //         console.log(res)
        //         this.$store.dispatch('getArticles')
        //         alert('게시글이 삭제되었습니다')
        //         this.$router.push({name: 'community'})
        //       })
        //       .catch((err) => {
        //         console.log(err)
        //       })
        //   } else {
        //       alert('작성자가 다르다')
        //       this.$router.push({ name: 'community'})
        //   }} else {
        //       alert('로그인 안되어 있음')
        //       // 삭제하는 유저와 게시글 유저가 같은지 어떻게 알지?
        //       this.$router.push({ name: 'LogInView'})
        //   }
        }
    }
}
</script>

<style>

</style>