import Vue from 'vue'
import VueRouter from 'vue-router'
// import ArticleView from '@/views/ArticleView'
// import CreateView from '@/views/CreateView'
import MovieDetailView from '@/views/MovieDetailView'
import SignUpView from '@/views/SignUpView'
import LogInView from '@/views/LogInView'
import HomeView from '@/views/HomeView'
import MyProfileView from '@/views/profile/MyProfileView'

import CommunityView from '@/views/community/CommunityView'
import ArticleCreateView from '@/views/community/ArticleCreateView'
import ArticleDetailView from '@/views/community/ArticleDetailView'

Vue.use(VueRouter)

const routes = [
  // {
  //   path: '/',
  //   name: 'ArticleView',
  //   component: ArticleView
  // },
  {
    path: '/',
    name: 'HomeView',
    component: HomeView
  },

  // {
  //   path: '/create',
  //   name: 'CreateView',
  //   component: CreateView
  // },

  {
    path: '/signup',
    name: 'SignUpView',
    component: SignUpView
  },

  {
    path: '/login',
    name: 'LogInView',
    component: LogInView
  },
  // 아래 movie/:id가 추가 된거야. 😀
  {
    path: '/movie/:id',
    name: 'MovieDetailView',
    component: MovieDetailView,
  },
  // 아래 이걸 주석처리할거야. 😀🤪
  // {
  //   path: '/:id',
  //   name: 'MovieDetailView',
  //   component: MovieDetailView,
  // },
  {
    path: '/myprofile',
    name: 'MyProfileView',
    component: MyProfileView
  },
  // 아래 3개가 추가되었습니다. 😀
  {
    path: '/community',
    name: 'community',
    component: CommunityView
  },
  {
    path: '/articlecreate',
    name: 'articlecreate',
    component: ArticleCreateView
  },
  {
    path: '/article/:id',
    name: 'articledetail',
    component: ArticleDetailView,
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
