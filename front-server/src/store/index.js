import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '@/router'

Vue.use(Vuex)


const API_URL = 'http://127.0.0.1:8000'


export default new Vuex.Store({
  plugins: [
    createPersistedState()
  ],
  state: {
    // isLoggedIn: !!this.getItem("token"),
    articles: [],
    token: null,
    username: ''
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    }
  },
  mutations: {
    GET_ARTICLES(state, articles) {
      state.articles = articles
    },
    // 회원가입 && 로그인
    SAVE_TOKEN(state, token) {
      state.token = token
      
      router.push({ name: 'HomeView' })
    },
    //여기서 로그아웃 받는다. 토큰없애고 홈뷰로 이동! 😀
    LOGOUT_USER(state) {
      state.token = null
      //로그아웃하면 사용자 이름 없앰. 😀
      state.username = ''
      console.log(state.username)
      router.push({ name: 'HomeView' })
    }
  },
  actions: {
    getArticles(context) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/articles/`,
        headers: {
          Authorization: `Token ${context.state.token}`
        }
      })
        .then((res) => {
          // console.log(res, context)
          // console.log(res.data)
          context.commit('GET_ARTICLES', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    signUp(context, payload) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username: payload.username,
          password1: payload.password1,
          password2: payload.password2,
        }
      })
        .then((res) => {
          // console.log(res)
          context.commit('SAVE_TOKEN', res.data.key)
        })
        .catch((err) => {
          alert('Verify password again')
          console.log(err)
        })
    },
    logIn(context, payload) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          username: payload.username,
          password: payload.password,
        }
      })
        .then((res) => {
          // 여기서 유저네임을 스토어로 보냄. 😀
          this.state.username = payload.username
          console.log(this.state.username)
          // console.log(res)
          context.commit('SAVE_TOKEN', res.data.key)
        })
        .catch((err) => {
          alert('Incorrect ID or Password')
          console.log(err)
        })
    },

    // 로그아웃버튼 위한 로직 신설 -dispatch로 사용. 😀-> 액션에서 뮤테이션으로 이동!
    logOut({commit}) {
      commit('LOGOUT_USER')
    },

    // 이하 배치 필요한 로직들
    // 커뮤니티 게시글 create 하는 법
    createArticle(context, payload) {
      const article = {
        id: context.state.article_id,
        title: payload.title,
        content: payload.content,
        createAt: new Date().getTime()
      }
      context.commit('CREATE_ARTICLE', article)
    },
    // 리뷰 포스트 목록을 장고에서 불러옴
    getPosts(context) {
      axios({
        method: 'get',
        url: `${API_URL}`,
        headers: {
          Authorization: `Token ${context.state.token}`
        }
      })
        .then((res) => {
          context.commit('GET_POSTS', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    // 포스트 전체글을 받아온다
    GET_POSTS(state, posts) {
      state.posts = posts
    },


  },
  modules: {
  }
})
