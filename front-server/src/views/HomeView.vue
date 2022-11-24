<template>
  <div>
    <h1>Here's trendy movies</h1>
    <div class="verticalclearance1"></div>
    <hr>
    <div class="main_movie">
      <div class="h1location" v-for="(movie, index) in popularmovies" :key="index" >
      <!-- <p>{{ movie.title }}</p> -->
      <img class="posterbox cursor postersize" :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" alt="" @click="movieDetail(movie)">
      </div>
    </div>
    <div class="verticalclearance1"></div>
    <h1 class="h1location">Latest Releases </h1>
    <hr>
    <div class="main_movie">
      <div class="" v-for="(movie, index) in latestmovies" :key="index" >
      <!-- <p>{{ movie.title }}</p> -->
      <img class="posterbox cursor postersize" :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" alt="" @click="movieDetail(movie)">
      </div>
    </div>
   
  </div>
</template>

<script>
import axios from 'axios'
export default {
    name: "HomeView",
    props: {
      
    },

    data() {
      return{
        popularmovies: '',
        latestmovies: '',
        movieId: '',
        posterurl: '',
        user: [],
      }
    },
    created() {
     this.getMovie(),
     this.getLatest()

    },
    methods: {
      // popular 5개 받아오기
      getMovie() {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/popular/`,
      })
        .then((res) => {
          this.movieId = this.$route.params.movieId
          this.popularmovies = res.data
          // this.posterurl = 'https://image.tmdb.org/t/p/w500/' + res.data[0].poster_path
        })
        .catch((err) => {
          console.log(err)
        } )
    },
    // 최근개봉일중에 평점 7점이상 5개 받아오기
    getLatest() {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/latest/`,
      })
        .then((res) => {
          this.movieId = this.$route.params.movieId
          this.latestmovies = res.data
          // this.posterurl = 'https://image.tmdb.org/t/p/w500/' + res.data[0].poster_path
        })
        .catch((err) => {
          console.log(err)
        } )
    },
    movieDetail(movie) {
      this.$router.push({name: 'MovieDetailView', params: { movie_id: `${movie.id}`}})

    }
  }, 
}
</script>

<style>
.main_movie {
  display: flex;
  justify-content: center;
}

.posterbox {
  /* width: 350px; width가 고정되어 짜부되던걸 수정했습니다. 😀*/

  margin: 0 auto 10px auto;
  padding: 10px 20px;
  /* color: white; */
  border-radius: 5px;
  box-shadow: rgba(0, 0, 0, 0.1) 0px 1px 3px 0px,
    rgba(0, 0, 0, 0.06) 0px 1px 2px 0px;

  display: block;
  /* width: 500px; */
  /* height: ; */
  margin: 20px auto;
  padding: 10px 45px;
  /* background: white url("@/assets/search-icon.png") no-repeat 15px center; */
  background-size: 15px 15px;
  /* font-size: 16px; */
  /* border: none; */
  /* border-radius: 5px; */
  /* box-shadow: rgba(50, 50, 93, 0.25) 0px 2px 5px -1px,
    rgba(0, 0, 0, 0.3) 0px 1px 3px -1px; */
}

.cursor {
  cursor: pointer;
}

.postersize {
  height: 500px;

}

.verticalclearance1 {
  height: 30px;
}

.h1location {
  margin: left 300px;
}
</style>