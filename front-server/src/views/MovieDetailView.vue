<!-- <template>
  <div>
    <h1>Detail</h1>
    <p>글 번호 : {{ article?.id }}</p>
    <p>제목 : {{ article?.title }}</p>
    <p>내용 : {{ article?.content }}</p>
    <p>작성시간 : {{ article?.created_at }}</p>
    <p>수정시간 : {{ article?.updated_at }}</p>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'DetailView',
  data() {
    return {
      article: null,
    }
  },
  created() {
    this.getArticleDetail()
  },
  methods: {
    getArticleDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/articles/${this.$route.params.id}`
      })
        .then((res) => {
          console.log(res)
          this.article = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    }
  }
}
</script> -->


<template>
  <div v-if="movie">
    <div class="bgimg" :style="{backgroundImage:`url(https://image.tmdb.org/t/p/w1280${movie.backdrop_path})`}">
      <h1>{{ movie.title }}</h1>
      <img :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" alt="">
      <p>{{ movie.overview }}</p>
      <p>{{movie.original_title}}</p>
      <img :src="`https://image.tmdb.org/t/p/w500${movie.backdrop_path}`" alt="">
      <p>{{movie.release_date}}</p>
      <p>{{movie.vote_count}}</p>
      <p>{{movie.vote_average}}</p>
      <p>{{movie.genres}}</p>
    </div>
    
  </div>
</template>

<script>
import axios from 'axios'


export default {
    name: 'MovieDetailView',
    components: {
    },
    data() {
        return{
            movie: '',
            movieId: '',
            posterUrl: '',
            avg: 0,
            getMovieDetail:null,
        }
    },

    created() {
            axios({
                method: 'get',
                url: `http://127.0.0.1:8000/movies/${this.$route.params.movie_id}/`,
            })
              .then((res) => {
                this.movieId = this.$route.params.movieId
                this.movie = res.data
                console.log(res.data.poster_path)
                // this.posterurl = `https://image.tmdb.org/t/p/w500` + res.data.poster_path
              })
              .catch((err) => {
                console.log(err)
              })

        
    }

}
</script>

<style>

.bgimg {
  /* width: 100%; */
  width: 100vw;
}

</style>