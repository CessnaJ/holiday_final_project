<template>
  <div>
    <div class="titlebox">
      <span class="h1style">Trendy movies</span>
    </div>
    <!-- <div class="verticalclearance1"></div> -->
    <!-- <hr> -->
    <div class="main_movie">
      <div class="h1style" v-for="(movie, index) in popularmovies" :key="index" >
      <!-- <p>{{ movie.title }}</p> -->
      <img class="posterbox cursor postersize posterinside" :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" alt="" @click="movieDetail(movie)">
      </div>
    </div>


    <div class="verticalclearance1"></div>
    <div class="titlebox">
      <span class="h1style">Latest Releases </span>
    </div>
    <!-- <hr> -->
    <div class="main_movie">
      <div class="" v-for="(movie, index) in latestmovies" :key="index" >
      <!-- <p>{{ movie.title }}</p> -->
      <img class="posterbox cursor postersize posterinside" :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" alt="" @click="movieDetail(movie)">
      </div>
    </div>


    <div class="verticalclearance1"></div>
    <div class="titlebox">
      <span class="h1style">Recommendations Released in {{year}} </span>
    </div>
    <!-- <hr> -->
    <div class="main_movie">
      <div class="" v-for="(movie, index) in randomyearmovies" :key="index" >
      <!-- <p>{{ movie.title }}</p> -->
      <img class="posterbox cursor postersize posterinside" :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" alt="" @click="movieDetail(movie)">
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
        randomyearmovies: '',
        movieId: '',
        posterurl: '',
        user: [],

        year: 2022,
        max: 2022,
        min: 1992
      }
    },
    created() {
     this.getMovie(),
     this.getLatest()
     this.getRandomyear()

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





    // 랜덤해의 영화뽑기 위에는 랜덤숫자뽑는 로직 있음. 랜덤 숫자도 자동으로 뽑아서 뿌림
    getRandomyear() {
      
      this.year = Math.floor(Math.random() * (this.max - this.min + 1)) + this.min;
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/randomyear/${this.year}/`,
      })
        .then((res) => {
          this.movieId = this.$route.params.movieId
          this.randomyearmovies = res.data
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

  margin: 0 auto 0px auto;
  padding: 10px 20px;
  /* color: white; */
  border-radius: 5px;
  box-shadow: rgba(0, 0, 0, 0.1) 0px 1px 3px 0px,
    rgba(0, 0, 0, 0.06) 0px 1px 2px 0px;

  display: block;
  /* margin: 20px auto; */
  /* padding: 10px 45px; */

  /* background-size: 15px 15px; */
  border-radius: 5px;
  box-shadow: rgba(50, 50, 93, 0.25) 0px 2px 5px -1px,
  rgba(0, 0, 0, 0.3) 0px 1px 3px -1px;
}

.cursor {
  cursor: pointer;
}

.postersize {
  height: 500px;

}

.verticalclearance1 {
  height: 40px;
}



.titlebox{
  display: flex;
  justify-content: center;
}


.h1style {
  margin: left 20px;
  color: wheat;
  font-weight: bold;
  font-size: 30px;
  width: 90%;
  max-width: 2000px;
  /* text-align: ; */
  /* float: left; */
}

.posterboxeffect {
  cursor: pointer;
  box-shadow: rgba(50, 50, 93, 0.25);
}

.posterinside {
  
  border: none;
  border-radius: 45px;
  box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease 0s;
  cursor: pointer;
  outline: none;
  }

.posterinside:hover {
  background-color: #13273ef8;
  /* box-shadow: 0px 15px 20px rgba(46, 229, 157, 0.4); */

  box-shadow: rgba(50, 50, 93, 0.25) 0px 2px 5px -1px,
  rgba(0, 0, 0, 0.3) 0px 1px 3px -1px;

  color: #fff;
  transform: translateY(-10px);
}

</style>