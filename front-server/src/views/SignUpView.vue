<template>
  <div>
    <div class="flex">
      <h1>Sign Up Page</h1>
    </div>

    <div class="verticalclearance1"></div>
    <div class="flex">
      <form @submit.prevent="signUp">
        <label class="inputlabel" for="username">username : </label>
        <input class="inputbox" type="text" id="username" v-model="username"><br>

        <label class="inputlabel" for="nickname">nickname : </label>
        <input class="inputbox" type="text" id="nickname" v-model="nickname"><br>

        <div class="verticalclearance1"></div>

        <label class="inputlabel" for="password1"> password : </label>
        <input class="inputbox" type="password" id="password1" v-model="password1"><br>

        <label class="inputlabel" for="password2"> password confirmation : </label>
        <input class="inputbox" type="password" id="password2" v-model="password2">

        <div class="verticalclearance2"></div>
        
        <label class="inputlabel" for="image_select">Select profile image by typing 1-5 : </label>
        <input class="inputbox" type="image_select" id="image_select" v-model="image_select">

        <input class="inputbox signupbutton" type="submit" value="SignUp">
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SignUpView',
  data() {
    return {
      username: null,
      nickname: null,
      password1: null,
      password2: null,
      image_select: null,
    }
  },
  methods: {
    signUp() {
      const username = this.username
      const nickname = this.nickname
      const password1 = this.password1
      const password2 = this.password2
      const image_select = this.image_select

      const payload = {
        // username,
        // password1,
        // password2,
        username: username,
        nickname: nickname,
        password1: password1,
        password2: password2,
        image_select: image_select,
      }

      this.$store.dispatch('signUp', payload)

    }
  }
}
</script>

<style>
.inputbox {
  /* display: block; */
  width: 350px;
  /* margin:  */
  /* padding: 10px 45px; */
  /* background: white url("@/assets/search-icon.png") no-repeat 15px center; */
  background-size: 15px 15px;
  font-size: 16px;
  border: none;
  border-radius: 5px;
  box-shadow: rgba(50, 50, 93, 0.25) 0px 2px 5px -1px,
    rgba(0, 0, 0, 0.3) 0px 1px 3px -1px;
}

.inputlabel {
  font-size: 20px;
  font:bold;
  color: wheat;
}

.signupbutton {
  font: bold;
  font-size: 20px;
}


.verticalclearance1 {
  height: 40px;
}

.verticalclearance2 {
  height: 70px;
}

.flex {
  display: flex;
  justify-content: center;
}
</style>
