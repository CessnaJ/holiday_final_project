<template>
  <div id="app" class="bgnavy">
    
    <nav v-if="!isLoggedIn" >
      <!-- 로그인 안된상태 -->
      <img class="mainimgsize" src="@/assets/chicken.png"/>
      <router-link :to="{ name: 'HomeView' }">
        <span @click="changeSearchingState">Today's Movie</span>
      </router-link> | 
      
      <router-link :to="{ name: 'community' }">
        <span @click="changeSearchingState">Community</span>
      </router-link> | 


      <router-link :to="{ name: 'SignUpView' }">
        <span @click="changeSearchingState">SignUp</span>
      </router-link> | 
      
      <router-link :to="{ name: 'LogInView' }">
        <span @click="changeSearchingState">Log In</span>
      </router-link> |
      
    </nav>
    <nav v-else>
      <!-- 로그인 된 상태 -->
      <img class="mainimgsize" src="@/assets/chicken.png"/>
      <span class="hello">Welcome {{$store.state.nickname}}</span> |
      
      <router-link :to="{ name: 'HomeView' }">
        <span @click="changeSearchingState">Today's Movie</span>
      </router-link> |

      <router-link :to="{ name: 'community' }">
        <span @click="changeSearchingState">Community</span>
      </router-link> | 
      
      <router-link :to="{ name: 'MyProfileView' }">
        <span @click="changeSearchingState">My Profile</span>
      </router-link> | 
      <!-- 아래 로그아웃버튼신설 😀 -->
      <button class="buttonclass" v-on:click.prevent="signOut()" >
        <span @click="changeSearchingState">Sign Out</span>
      </button>
    </nav>
    <SearchBar/>
    
    <div class="verticalclearance">
    </div>

    <router-view/>
  </div>
</template>

<style>

* {
  font-family: "Montserrat", sans-serif;
}


#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center; */
  color: #2c3e50;
}

nav {
  display: flex;
  align-items: center;
  /* padding: 30px; */
  justify-content: space-around;
  font:bold;
  font-size: 17px;
  padding: 30px 25px 20px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}

.hello {
  font-weight: bold;
  color: #2c3e50;
}



.buttonclass {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;

  background-color: #4CAF50;
  border: none;
  color: black;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
}

.verticalclearance {
  height: 50px;

}

.mainimgsize {
  width: 7rem;
}

.bgnavy {
  background-color: #15273E;
  opacity: 50%;
  z-index: -1500;
}





</style>


<script>
import SearchBar from '@/components/SearchBar.vue';
// import { create } from 'domain';

export default {
    name: "LogInView",
    components: { 
      SearchBar 
    },

    data() {
        return {};
    },
    methods: {
        signOut() {
            this.$store.dispatch("logOut");
        },
        // emptySearchbox() {
        //   this.$refs.searchbar.emptySearchbox()
          // SearchBar.movies.splice(0, this.movies.length);
          // this.movies.splice(0, this.movies.length);
          // this.input = ''
      // console.log(this.movies.length)
        // }
          linkClick() {
            console.log('link')
            this.$store.commit("emptySearchbar")
          },
          changeSearchingState() {
            console.log('searchingstate')
            this.$store.commit("changeSearchingState")
          }

    },
    computed: {
        isLoggedIn() {
            return this.$store.state.token;
        }
    },

    // created() {
    //   console.log(this.$store.state.nickname)
    // }
    

}



</script>