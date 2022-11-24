<template>
  <div>
    <h1>게시글을 작성해주세요</h1>
    <form @submit.prevent="createArticle">
      <label for="title">제목 : </label>
      <input type="text" id="title" v-model.trim="title"><br>
      <label for="content">내용 : </label>
      <textarea id="content" cols="30" rows="10" v-model="content"></textarea><br>
      <input type="submit" id="submit">
    </form>
    
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
    name: "ArticleCreateView",
    data() {
      return {
        title: null,
        content: null,
      }
    },
    computed: {
        isLogin() {
            return this.$store.getters.isLogin
        }
    },
    methods: {
        createArticle() {
            const title = this.title
            const content = this.content
            if (!title) {
              alert('제목을 입력해주세요')
              return
            } else if (!content) {
              alert('내용을 입력해주세요')
              return
            }
            axios({
              method: 'post',
              url: `${API_URL}/community/`,
              data: {
                title: title,
                content: content,
              },
              headers: {
                Authorization: `Token ${this.$store.state.token}`
              }
            })
              .then((res) => {
                console.log(res)
                this.$router.push({name:'community'})
              })
              .catch((err) => {
                console.log(err)
              })
        },
        goDetail() {
          this.$router.push({ name: 'articledetail'})
        }
    }
}
</script>

<style>

</style>