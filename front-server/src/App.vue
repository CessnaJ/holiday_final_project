<template>
  <div id="app">
    <nav v-if="!isLoggedIn">
      
      <router-link :to="{ name: 'HomeView' }">Today's movie</router-link> | 
      <router-link :to="{ name: 'SignUpView' }">SignUp</router-link> | 
      <router-link :to="{ name: 'LogInView' }">Log In</router-link> |
      
    </nav>
    <nav v-else>
      
      <router-link :to="{ name: 'HomeView' }">Today's movie</router-link> |
      <span>Welcome {{$store.state.username}}</span> |
      <router-link :to="{ name: 'MyProfileView' }">My Profile</router-link> | 
      <!-- 아래 로그아웃버튼신설 😀 -->
      <button v-on:click.prevent="signOut()" >Sign Out</button>
    </nav>
    <SearchBar/>
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
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}

button {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;

  background-color: #4CAF50;
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
}
</style>


<script>
import SearchBar from '@/components/SearchBar.vue';

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
        }
    },
    computed: {
        isLoggedIn() {
            return this.$store.state.token;
        }
    },
    
}




</script>