<template>
  <div class="wrap">
    <div class="box">
      <div class="box-title biggertext">
        <h1>{{thisArt.title}}</h1>
      </div>
      <div class="box-content generaltext bgcolor">
        <div class="content-box2" >
          <p id="creater">작성자 {{thisArt.username}}</p>
          <hr>
        </div>
        <div id="imageField">
          <img :src="require(`@/assets/${imgSrc}.jpg`)" alt="">
        </div>
        <div class="content-box">
          <p>{{thisArt.content}}</p>
        </div>
        <div class="delete-btn">
          <button @click="deleteArticle" class="btn">삭제</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import _ from 'lodash'

const API_URL = 'http://127.0.0.1:8000'

export default {
    name: 'ArticleDetailView',
    created() {
        this.thisArticle = this.getArticleDetail
    },
    data(){
      return{
        thisArt : this.$store.state.articles.filter((a)=>{return(Number(a.id)===Number(this.$route.params.id))})[0],
        imgSrc: null,
      }
    },
    mounted() {
      const random = _.random(1, 5)
      this.imgSrc = `image_${random}`

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

<style scoped>
.btn {
  width: 250px;
  height: 45px;
  font-size: 18px;
  text-transform: uppercase;
  letter-spacing: 2.5px;
  font-weight: 500;
  color: #000;
  background-color: #fff;
  border: none;
  border-radius: 45px;
  box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease 0s;
  cursor: pointer;
  outline: none;
  }

.btn:hover {
  background-color: #2EE59D;
  box-shadow: 0px 15px 20px rgba(46, 229, 157, 0.4);
  color: #fff;
  transform: translateY(-7px);
}

.box {
  width: 90%;
  max-width: 1000px;
  border: solid 3px #C2D7F3;;
}

.box-title {
  width: 100%;
  height: 80px;
  /* background-color: #C2D7F3; */
  background-color: #79aeb2;
  color: darkslategray;
  display: flex;
  align-items: center;
  justify-content: center;
}

.box-content {
  padding: 60px;
}

.content-box2 {
  width: 100%;
  height: 30px;
  margin-bottom: 20px;
}

.content-box2 > #creater {
  margin-bottom: 10px;
}

.content-box {
  width: 100%;
  height: 400px;
  margin: 30px 0px 0px 0px;
}

.wrap {
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.generaltext {
  /* color: #f9ddd2; */
  color: black;
  font: 16px;
}

.biggertext {
  /* color: #f9ddd2; */
  color: wheat;
  /* color: #79aeb2; */
  font: 20px bold;
}


.bgcolor {
  /* background-color: wheat; */
  background-color: #f9ddd2;

}

.flexright {
  flex-direction: row-reverse;
}

.delete-btn{
  display: flex;
  justify-content: right;
}
</style>