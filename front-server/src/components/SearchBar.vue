<template>
  <div>
    <input type="text" :value="input" @input="input=$event.target.value; getSearchmovies(input)" placeholder="Search Movies by Title" />
    <!-- <span>{{input}}</span> -->
    <!-- <input type="text" class="searchbox" v-model="input" v-on:input="getSearchmovies(input)" placeholder="Search Movies by Title" /> -->
    <div class="container" v-if="$store.state.issearching">
      <div class="item fruit card" v-for="(movie, index) in movies" :key="index">
        <!-- <p>{{ movie }}</p> -->
        <img class ="" :src="`https://image.tmdb.org/t/p/w300${movie.poster_path}`" @click="movieDetail(movie); emptySearchbox()"/>
        <div class="inner-content">
            <span class="title">{{movie.title}}</span>
            <hr>
            <span class="overview">{{movie.overview.slice(0,100)}}...</span>
        </div>
        <!-- <div class="card">
          <img src="https://image.tmdb.org/t/p/w300_and_h450_bestv2/5AFKp85Bka4mQeaeVNs3evyMYYE.jpg" alt="">
          
        </div> -->
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
  computed: {
    emptySearchbarbool() {
      console.log('hi')
      this.emptySearchbox()
      return this.$store.state.emptySearchbarbool ? 1 : 0
    },


  },
  
  data() {
    return {
      API_URL: 'http://127.0.0.1:8000',
      // input: ref(""),
      input: '',
      movies: [],

    }

  },

  watch:{
    input() {
      this.$store.state.issearching
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
      console.log(this.input)
      this.$store.state.issearching = true

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
    emptySearchbox() {
      this.movies.splice(0, this.movies.length);
      this.input = ''
      console.log('empty')
      // console.log(this.movies.length)
    }

//     filteredList() {
//       return fruits.filter((fruit) =>
//       fruit.toLowerCase().includes(input.value.toLowerCase())
//   )
// }
  },

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
  /* 원래 width 350 */
  /* 아래에 .card때문에 의미없네 css원칙 나중에 온게 우선권 가진다. */
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
  justify-content: center;
}





/* 여기 아래가 카드 호버효과 */
.card {
  position: relative;
  background: linear-gradient(180deg, #441DB2 0%, #0d0425 100%);
  /* 카드 크기 수정되었습니다. 😀 아래 rem이었음. */
  width: 17rem;
  overflow: hidden;
  box-shadow: 15px 15px 25px black;
}
.card img {
  width: 100%;
  height: auto;
  transform: scale(1.1);
  transition: all 0.25s linear;
}
.card:hover img {
  opacity: 0.2;
  transform: scale(1.25);
}
.card .inner-content {
  width: 80%;
  opacity: 0;
  transform: translateX(-50%) translateY(-50%);
  position: absolute;
  top: 80%;
  left: 50%;
  transition: all 600ms ease;
  color: white;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.card:hover .inner-content {
  opacity: 1;
  top: 50%;
}
.card .inner-content .title {
  font-size: 1.2rem;
  font-weight: 700;
}
.card .inner-content .overview {
  font-size: 0.9rem;
  font-weight: 300;
}
.card .inner-content hr {
  border-top: 1px solid #f1f1f1;
  width: 100%;
}

</style>