<template>
  <div>
    <!-- <input type="text" @input="typing" :value="getSearchmovies(value)" placeholder="Search Movies by Title" /> -->
    <input type="text" class="searchbox" v-model="input" v-on:input="getSearchmovies(input)" placeholder="Search Movies by Title" />
    <div class="container">
      <div class="item fruit" v-for="(movie, index) in movies" :key="index">
        <!-- <p>{{ movie }}</p> -->
        <img :src="`https://image.tmdb.org/t/p/w300${movie.poster_path}`" @click="movieDetail(movie)"/>
      </div>
    </div>
    <div class="item error" v-if="input&&!movies.length">
      <p>No results found!</p>
    </div>
  
  </div>
</template>

<script>
import axios from 'axios'
// import { ref } from "vue"


//검색 로직이 들어갑니다.
export default {
  name: 'SearchBar',
  components: {
    
  },

  
  data() {
    return {
      API_URL: 'http://127.0.0.1:8000',
      // input: ref(""),
      input: '',
      movies: [],

    }

  },

  
  methods: {
    // typing(e) {
    //   this.input = e.target.value
    // },
    movieDetail(movie) {
      this.$router.push({name: 'MovieDetailView', params: { movie_id: `${movie.id}`}})
      

    },

    getSearchmovies(input) {
      axios({
        method: 'get',
        url: `${this.API_URL}/movies/search/`,
        params: {keyword:input}
      })
        .then((res) => {
          // // console.log(res, context)
          // // console.log(res.data)
          // context.commit('GET_ARTICLES', res.data)
          // console.log(res)
          // console.log(res.data)
          // console.log(`${this.keyword} 를 입력한건 잘 들어갔음.`)
          // console.log(this.context)
          // console.log(`${input}를 입력했습니다.`)
          this.movies = res.data
          console.log(this.movies)
        })
        .catch((err) => {
          console.log(err)
        })
    },

//     filteredList() {
//       return fruits.filter((fruit) =>
//       fruit.toLowerCase().includes(input.value.toLowerCase())
//   )
// }
  },

  computed: {
    // articles() {
    //   return this.$store.state.articles
    // }
  }
}


</script>



<style>
/* @import url("https://fonts.googleapis.com/css2?family=Montserrat&display=swap"); */

* {
  padding: 0;
  margin: 0;
  box-sizing: border-box;
  font-family: "Montserrat", sans-serif;
}

body {
  padding: 20px;
  min-height: 100vh;
  background-color: rgb(234, 242, 255);
}

.searchbox {
  display: block;
  width: 350px;
  margin: 20px auto;
  padding: 10px 45px;
  background: white url("@/assets/search-icon.png") no-repeat 15px center;
  background-size: 15px 15px;
  font-size: 16px;
  border: none;
  border-radius: 5px;
  box-shadow: rgba(50, 50, 93, 0.25) 0px 2px 5px -1px,
    rgba(0, 0, 0, 0.3) 0px 1px 3px -1px;
}

input {
  display: block;
  width: 350px;
  margin: 20px auto;
  padding: 10px 45px;
  /* background: white url("@/assets/search-icon.png") no-repeat 15px center; */
  background-size: 15px 15px;
  font-size: 16px;
  border: none;
  border-radius: 5px;
  box-shadow: rgba(50, 50, 93, 0.25) 0px 2px 5px -1px,
    rgba(0, 0, 0, 0.3) 0px 1px 3px -1px;
}

.item {
  width: 350px;
  margin: 0 auto 10px auto;
  padding: 10px 20px;
  color: white;
  border-radius: 5px;
  box-shadow: rgba(0, 0, 0, 0.1) 0px 1px 3px 0px,
    rgba(0, 0, 0, 0.06) 0px 1px 2px 0px;
}

.fruit {
  background-color: rgb(97, 62, 252);
  cursor: pointer;
}

.error {
  background-color: tomato;
}
.container {
  display: flex;
}
</style>