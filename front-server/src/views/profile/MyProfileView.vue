<template>
  <div>
    <h1>My profile page</h1>
    <!-- <button @click="logout">Logout</button> 필요없음.-->
    <div class="container">
      <img v-if="$store.state.c" class="profileimg" :src="`@/assets/profile${imagesource}.png`" alt="">
      <img v-else class="profileimg" src="@/assets/profile2.png"/>
      <span>{{$store.state.image_select}}누칼협오리 뜨면 문제있는거야.'s Profile{{$store.state.image_select}}</span>
    </div>
    
  </div>
</template>

<script>
export default {
    name: "MyProfileView",
    data() {
      return {
        defaultProfile: '@/'
      }
    },
    methods: {
      logout() {
        this.$store.commit('LOGOUT_USER')
      },
    },
    computed: {
      imagesource() {
        console.log(this.$store.state.username);
        console.log(this.$store.username)    
        return this.$store.state.image_select;
        }
    },

    created() {
        console.log("Child created")
        console.log(this.$store.username)
    },
    mounted() {
        console.log("Child mounted")
    }
}



</script>

<style>
.profileimg {
      /* border: 1px solid black; */
      border-radius: 100%;
      width: 15rem;
      background: transparent;
        }

.container {
  justify-content:center;
}
</style>