<template>
  <div>
    <div class="create">
      <h1>게시글을 작성해주세요</h1>
      <form class="create-form" @submit.prevent="createArticle">
        <input class="create-form-title" placeholder="제목" type="text" id="title" v-model.trim="title"><br>
        <textarea class="create-form-content" placeholder="내용" id="content" cols="30" rows="10" v-model="content"></textarea><br>
        <input class="create-form-submit" type="submit" id="submit">
      </form>

    </div>
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

<style scoped>
.create {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
}
.create-form {
  width: 90%;
  max-width: 500px;
  text-align: left;
  padding: 30px;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.create-form-title {
  width: 100%;
  height: 30px;
  padding: 20px;
  border: none;
  box-shadow: rgba(50, 50, 93, 0.25) 0px 2px 5px -1px,
    rgba(0, 0, 0, 0.3) 0px 1px 3px -1px;
}
.create-form-content {
  width: 100%;
  padding: 20px;
  border: none;
  box-shadow: rgba(50, 50, 93, 0.25) 0px 2px 5px -1px,
    rgba(0, 0, 0, 0.3) 0px 1px 3px -1px;
}
.create-form-submit {
  cursor: pointer;
  width: 100px;
  height: 30px;
  margin-bottom: 20px;
  border: none;
  box-shadow: rgba(50, 50, 93, 0.25) 0px 2px 5px -1px,
    rgba(0, 0, 0, 0.3) 0px 1px 3px -1px;
  transition: all 0.2s;
}
.create-form-submit:hover {
  scale: 110%;
  border-radius: 20px;
}

</style>