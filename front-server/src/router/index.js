import Vue from 'vue'
import VueRouter from 'vue-router'
// import ArticleView from '@/views/ArticleView'
import CreateView from '@/views/CreateView'
import MovieDetailView from '@/views/MovieDetailView'
import SignUpView from '@/views/SignUpView'
import LogInView from '@/views/LogInView'
import HomeView from '@/views/HomeView'
import MyProfileView from '@/views/profile/MyProfileView'

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

  {
    path: '/create',
    name: 'CreateView',
    component: CreateView
  },

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

  {
    path: '/:id',
    name: 'MovieDetailView',
    component: MovieDetailView,
  },
  {
    path: '/myprofile',
    name: 'MyProfileView',
    component: MyProfileView
  },


]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
