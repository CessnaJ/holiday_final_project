<template>
  <div>
    <div class="flex">
      <h1 class="navyfont">LogIn Page</h1>
    </div>
    
    <div class="verticalclearance"></div>

    <div class="flex">
      <form @submit.prevent="logIn">
        <label class="inputlabel" for="username">username : </label>
        <input class="inputbox" type="text" id="username" v-model="username"><br>

        <label class="inputlabel" for="password"> password : </label>
        <input class="inputbox" type="password" id="password" v-model="password"><br>

        <input class="inputbox" type="submit" value="logIn">
      </form>
    </div>
  </div>

</template>

<script>
export default {
  name: 'LogInView',
  data() {
    return {
      username: null,
      password: null,
    }
  },
  methods: {
    logIn() {
      const username = this.username
      const password = this.password

      const payload = {
        username: username,
        password: password,
      }
      this.$store.dispatch('logIn', payload)
    }
  }
}
</script>


<style>
.inputbox {
  display: block;
  width: 350px;
  margin: 20px auto;
  padding: 10px 45px;
  /* background: white url("@/assets/search-icon.png") no-repeat 15px center; */
  background-size: 15px 15px;
  font-size: 16px;
  border: none;
  border-radius: 5px;
  box-shadow: rgba(50, 50, 93, 0.25) 0px 2px 5px -1px,
    rgba(0, 0, 0, 0.3) 0px 1px 3px -1px;
}

.verticalclearance{
  height: 45px;

}

.flex {
  display: flex;
  justify-content: center;
}

.inputlabel {
  font-size: 20px;
  font:bold;
  color: wheat;
}

.navyfont {
  /* color: #15273E; */
  color: wheat;
  /* font-size: 30px; */
  /* font:bold; */
}

</style>