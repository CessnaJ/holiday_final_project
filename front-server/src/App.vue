<template>
  <div>
    <div id="app" class="bgnavy bgpadding">
      <nav v-if="!isLoggedIn" >
        <!-- 로그인 안된상태 -->
        <div class="flex txtalign">
          <img class="mainimgsize" src="@/assets/chicken.png"/>
          <router-link :to="{ name: 'HomeView' }">
            <span class="navrightmargin" @click="changeSearchingState">Today's Movie</span>
          </router-link> | 
        </div>

        <div class="flex txtalign">
          <router-link :to="{ name: 'community' }">
            <span class="navrightmargin" @click="changeSearchingState">Community</span>
          </router-link> | 
        
          <router-link :to="{ name: 'SignUpView' }">
            <span class="navrightmargin" @click="changeSearchingState">SignUp</span>
          </router-link> | 
          
          <router-link :to="{ name: 'LogInView' }">
            <span class="navrightmargin" @click="changeSearchingState">Log In</span>
          </router-link> |
        </div>
      </nav>
      
      <nav v-else>
        <!-- 로그인 된 상태 -->
        <div class="flex txtalign">
          <img class="mainimgsize" src="@/assets/chicken.png"/>
          <span class="hello navrightmargin">Welcome {{$store.state.nickname}}</span> |
          
          <router-link :to="{ name: 'HomeView' }">
            <span class="navrightmargin" @click="changeSearchingState">Today's Movie</span>
          </router-link> |
        </div>

        <div class="flex txtalign">
          <router-link :to="{ name: 'community' }">
            <span class="navrightmargin" @click="changeSearchingState">Community</span>
          </router-link> | 
          
          <router-link :to="{ name: 'MyProfileView' }">
            <span @click="changeSearchingState">My Profile</span>
          </router-link> | 
          <!-- 아래 로그아웃버튼신설 😀 -->
          <button class="buttonclass" v-on:click.prevent="signOut()" >
            <span @click="changeSearchingState">Sign Out</span>
          </button>
        </div>
      </nav>
      <SearchBar/>
      
      <div class="verticalclearance">
      </div>

      <router-view/>
    </div>
  <div>
    <Footer/>
  </div>    

  </div>
</template>

<style>

.txtalign {
  text-align: center;
  align-items: center;
}



.navrightmargin {
  /* color: rgb(255, 255, 255); */
  margin-right: 15px;
  
}



* {
  font-family: "Montserrat", sans-serif;
}

.bgpadding {
  padding-bottom: 50px;
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
  /* font-size: 17px; */
  padding: 30px 25px 20px;
}

nav a {
  font-weight: bold;
  color: white;
  font-size: 23px;
}

nav a.router-link-exact-active {
  color: #42b983;
}

.hello {
  font-weight: bold;
  color: white;
  size: 20px;
}



.buttonclass {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;

  /* background-color: #4CAF50; */
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 20px;
  font: bold;
}

.verticalclearance {
  height: 50px;

}

.mainimgsize {
  width: 7rem;
  margin-right: 30px;
}

.bgnavy {
  background-color: #13273ef8;
  /* opacity: 50%; */
  z-index: -1500;
}





</style>


<script>
import SearchBar from '@/components/SearchBar.vue';
import Footer from '@/components/FooterItem.vue'
// import { create } from 'domain';

export default {
    name: "LogInView",
    components: { 
      SearchBar,
      Footer 
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