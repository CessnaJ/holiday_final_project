<template>
  <div class="flex">
    <div class="">
      <h1 class="bigtxt textcenter">My profile</h1>
      <img v-if="$store.state.image_select" class="profileimg verticalseperation" :src="require(`@/assets/profile${$store.state.image_select}.png`)" alt="">
      <img v-else class="profileimg verticalseperation" src="@/assets/profile2.png"/>
    </div>
    
    
    <div class="container">
      <p class="midtxt">Username: {{$store.state.username}}</p>
      <p class="midtxt">Nickname: {{$store.state.nickname}}</p>
      <!-- <p>{{$store.state.image_select}}번 이미지를 선택했음.</p> -->
      
      <div class="horizontaldisplay"></div>
        <div class="verticaldisplay">
          <p class="bigtxt">👍</p>
          <p class="bigtxt">0</p>
        </div>
        <div class="verticaldisplay">
          <p>d</p>
          <p>d</p>
        </div>
      <div class="verticaldisplay">
        <p>🏎</p>
      </div>

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
        console.log(this.$store.state.username);
        console.log(this.$store.state.image_select);   
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
      height: 15rem;
      background: transparent;
        }

.container {
  justify-content:center;
}

.bigtxt {
  color: wheat;
  font-size: 40px;
  text-align: center;
}

.midtxt {
  color: wheat;
  font-size: 30px;
}

.flexeven {
  justify-content: space-evenly;
}

.textcenter {
  text-align: center;
}


.verticalseperation {
  margin-top: 30px;
}

.horizontaldisplay {
  display: flex;
  justify-content: space-around;
}


.verticaldisplay {
  flex-direction: column;
  justify-content: space-around;
}

</style>