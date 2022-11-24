<template>
  <div v-if="movie">
    <div class="edgebox footersep flex">
      <div class="postersurrounding">
        <img class="postersurrounding cursor" :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" @click="getvideo" alt="">
      </div>

      <div class="flex-column">
        <div class="verticalseparation"></div>
        <span class="biggertext">{{ movie.title }}</span>
        <span class="mediumtext marginl">{{movie.original_title}}</span>
        <br>
        

        <div class="verticalsep">
          <span v-for="(item, index) in genre_list" :key="`item-${index}`" class="mediumtext genrespace">{{item}}</span>
        </div>
        <div class="verticalsep">
          <span style="font-size: 50px; margin-right: 10px;">⌚</span>
          <span class="semibiggertext">{{movie.runtime}}</span> <span class="mediumtext"> min</span>
        </div>

        <div class="flex verticalslight" style="justify-content: space-evenly">
          <div>
          <p style="font-size: 50px;">😀</p>
          <p class="mediumtext txtalign">{{movie.vote_count}}</p>
          </div>
          <div class="">
            <p style="font-size: 50px;">⭐</p>
            <p class="mediumtext txtalign">{{movie.vote_average}}</p>
          </div>
        </div>
        
        <div class="verticalslight">
          <span style="font-size: 50px;">📅</span>
          <span class="mediumtext">{{movie.release_date}}</span>
        </div>
        <p class="mediumtext verticalsep">{{ movie.overview }}</p>

      </div>
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

    methods: {
      getvideo() {

      }
    },

    //디테일페이지는 그냥 tmdb에서 디테일 긁고, 장르 object돌면서 가는것도 괜찮아보인다.
    created() {
              console.log(`${this.$route.params.movie_id}`)
    
            axios({
                method: 'get',
                url: `https://api.themoviedb.org/3/movie/${this.$route.params.movie_id}`,
                params: {
                  api_key: "c45ff232f6fbb4731afd07f09e5b072b",
                  language: "ko-KR"
                }
            })
              .then((res) => {
                this.movieId = this.$route.params.movieId
                this.movie = res.data
                this.genreString = res.data.genres
                this.genre_list = res.data.genres.map(e=>Object.keys(this.genre_dict).includes(e.id+'') ?e.name :false).filter(e => e)
                console.log(this.genre_list)
              })
              .catch((err) => {
                console.log(err)
              })
              ,


              axios({
                method: 'get',
                url: `https://api.themoviedb.org/3/movie/${this.$route.params.movie_id}/reviews`,
                params: {
                  api_key: "c45ff232f6fbb4731afd07f09e5b072b",
                  language: "en-US"
                }
            })
              .then((res) => {
                console.log(res.data)
                // this.movieId = this.$route.params.movieId
                // this.movie = res.data
                
              })
              .catch((err) => {
                console.log(err)
              })
              ,

              axios({
                method: 'get',
                url: `https://api.themoviedb.org/3/movie/${this.$route.params.movie_id}/videos`,
                params: {
                  api_key: "c45ff232f6fbb4731afd07f09e5b072b",
                  language: "en-US"
                }
            })
              .then((res) => {
                console.log(res.data)
                // this.movieId = this.$route.params.movieId
                // this.movie = res.data
                
              })
              .catch((err) => {
                console.log(err)
              })




            }
          }


</script>

<style>
.cursor {
  cursor: pointer;
}

.txtalign {
  text-align: center;
  /* align-items: center; */
}

.verticalseparation {
  margin-top: 60px;
}

.verticalsep {
  margin-top: 40px;
}

.verticalslight {
  margin-top: 20px;
}

.footersep {
  margin-bottom: 100px ;
}

.biggertext {
  color: wheat;
  font: 40px bold;
  margin-bottom: 20px;

}

.semibiggertext {
  color: wheat;
  font: 30px bold;
  margin-bottom: 20px;

}

.mediumtext {
  color: wheat;
  font: 23px bolder;
}

.edgebox {
  margin: 10px 200px 0px;
  padding: 0px 0px 60px;
  border-radius: 20px;
}


.postersurrounding {
  margin: 0px 50px 0px 0px;
  border-radius: 25px;
}

.genrespace {
  margin-left: 0px;
  margin-right: 20px;
}

.marginl {
  margin-left: 30px;
}
/* .container {
  width: 100%;
  height: 100%;
  text-align: center;
  background: url("./images/sunrise.jpg");
  opacity: 0.5;
} */
</style>