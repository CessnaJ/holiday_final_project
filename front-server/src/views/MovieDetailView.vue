<template>
  <div v-if="movie">
    <div class="bgimg" 
      :style="{backgroundImage:`url(https://image.tmdb.org/t/p/w1280${movie.backdrop_path})`}">
    <!-- <img :src="require(`https://image.tmdb.org/t/p/w1280${movie.backdrop_path}`)" alt="" width="50px"/> -->
      <h1>{{ movie.title }}</h1>
      <img :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" alt="">
      <p>{{ movie.overview }}</p>
      <p>{{movie.original_title}}</p>
      <!-- <img :src="`https://image.tmdb.org/t/p/w500${movie.backdrop_path}`" alt=""> -->
      <p>{{movie.release_date}}</p>
      <p>{{movie.vote_count}}</p>
      <p>{{movie.vote_average}}</p>
      <p>{{movie.genres}}</p>
      <p>{{genre_list}}</p>
      <p>{{movie}}</p>
    </div>
    
  </div>
</template>

<script>
import axios from 'axios'


export default {
    name: 'MovieDetailView',
    components: {
    },
    // props: {
    //   movie
    // },
    data() {
        return{
            movie: '',
            movieId: '',
            posterUrl: '',
            genreString: '',
            avg: 0,
            getMovieDetail:null,




            genre_list:[],
            genre_dict: {
                        28: '액션',
                        12: '모험',
                        16: '애니메이션',
                        35: '코미디',
                        80: '범죄',
                        99: '다큐멘터리',
                        18: '드라마',
                        10751: '가족',
                        14: '판타지',
                        36: '역사',
                        27: '공포',
                        10402: '음악',
                        9648: '미스터리',
                        10749: '로맨스',
                        878: 'SF',
                        10770: 'TV 영화',
                        53: '스릴러',
                        10752: '전쟁',
                        37: '서부'
                        }
            
        }
    },
    //디테일페이지는 그냥 tmdb에서 디테일 긁고, 장르 object돌면서 가는것도 괜찮아보인다.
    created() {
            axios({
                method: 'get',
                url: `http://127.0.0.1:8000/movies/${this.$route.params.movie_id}/`,
            })
              .then((res) => {
                this.movieId = this.$route.params.movieId
                this.movie = res.data
                this.genreString = res.data.genres
                console.log(res.data)
                // this.posterurl = `https://image.tmdb.org/t/p/w500` + res.data.poster_path

                for (const genre_num in this.genre_dict) {
                  if (genre_num in this.movie.genres) {
                    console.log('forlooping')
                    this.genre_list.push(this.genre_dict[genre_num])
                  }
                }
              })
              .catch((err) => {
                console.log(err)
              })
            }
          }
        
  
        
    
            // axios({
            //     method: 'get',
            //     url: `https://api.themoviedb.org/3/movie/${this.$route.params.movie_id}/`,
            //     params: {
            //       api_key:c45ff232f6fbb4731afd07f09e5b072b,
            //       language: ko-KR
            //     }
            // })
            //   .then((res) => {
            //     this.movieId = this.$route.params.movieId
            //     this.movie = res.data
            //     this.genreString = res.data.genres
            //     console.log(res.data)
            //     // this.posterurl = `https://image.tmdb.org/t/p/w500` + res.data.poster_path

            //     for (const genre_num in this.genre_dict) {
            //       if (genre_num in this.movie.genres) {
            //         console.log('forlooping')
            //         this.genre_list.push(this.genre_dict[genre_num])
            //       }
            //     }
            //   })
            //   .catch((err) => {
            //     console.log(err)
            //   })



</script>

<style>

.bgimg {
  /* width: 100%; */
  /* width: 100%; */
    height: 100vh;
    width: 100vw;
    /* background-image: url('img/signup.jpeg'); */
    background-repeat : no-repeat;
    background-size : cover;
    opacity: 0.5;
    z-index: -1;

}

.bgimg::after {
  /* width: 100%; */
  /* width: 100%; */
    /* height: 100vh;
    width: 100vw; */
    /* background-image: url('img/signup.jpeg'); */
    /* background-repeat : no-repeat; */
    /* background-size : cover; */
    opacity: 0.5;

}

/* .container {
  width: 100%;
  height: 100%;
  text-align: center;
  background: url("./images/sunrise.jpg");
  opacity: 0.5;
} */
</style>