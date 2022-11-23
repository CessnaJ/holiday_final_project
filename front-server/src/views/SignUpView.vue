<template>
  <div>
    <h1>Sign Up Page</h1>
    <form @submit.prevent="signUp">
      <label for="username">username : </label>
      <input type="text" id="username" v-model="username"><br>

      <label for="nickname">nickname : </label>
      <input type="text" id="nickname" v-model="nickname"><br>

      <label for="password1"> password : </label>
      <input type="password" id="password1" v-model="password1"><br>

      <label for="password2"> password confirmation : </label>
      <input type="password" id="password2" v-model="password2">
      
      <label for="image_select"> image_select image_select : </label>
      <input type="image_select" id="image_select" v-model="image_select">

      <input type="submit" value="SignUp">
    </form>
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
