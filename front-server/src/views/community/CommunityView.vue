<template>
  <div>
    <div class="wrap">
      <button class="btn" @click="goCreate">리뷰 작성하세요</button>
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
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

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
            axios({
              method: 'get',
              url: `${API_URL}/community/`,
              headers: {
                Authorization: `Token ${this.$store.state.token}`
              }
            })
              .then((res) => {
                console.log(res)
                this.$router.push({name:'articlecreate'})
              })
              .catch((err) => {
                console.log(err)
                alert('로그인이 필요한 서비스입니다')
                this.$router.push({name:'LogInView'})
              })
        },
    }
}
</script>

<style>
.outer {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 40px;
}
.wrap {
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

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


</style>