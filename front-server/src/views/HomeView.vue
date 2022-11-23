<template>
  <div>
    <h1>Here's trendy movies</h1>
    <hr>
    <div class="main_movie">
      <div class="" v-for="(movie, index) in movies" :key="index" >
      <p>{{ movie.title }}</p>
      <img class="poseterbox" :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" alt="" @click="movieDetail(movie)">
      </div>
    </div>
   
  </div>
</template>

<script>
import axios from 'axios'
export default {
    name: "HomeView",
     data() {
      return{
        movies: '',
        movieId: '',
        posterurl: '',
        user: [],
      }
    },
    created() {
     this.getMovie()
    },
    methods: {
      getMovie() {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/popular/`,
      })
        .then((res) => {
          this.movieId = this.$route.params.movieId
          this.movies = res.data
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
  /* width: 350px; */
  margin: 0 auto 10px auto;
  padding: 10px 20px;
  /* color: white; */
  border-radius: 5px;
  box-shadow: rgba(0, 0, 0, 0.1) 0px 1px 3px 0px,
    rgba(0, 0, 0, 0.06) 0px 1px 2px 0px;

  display: block;
  width: 350px;
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


</style>