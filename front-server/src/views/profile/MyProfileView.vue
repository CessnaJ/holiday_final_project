<template>
  <div>
    <h1>My profile page</h1>
    <!-- <button @click="logout">Logout</button> 필요없음.-->
  </div>
</template>

<script>
export default {
    name: "MyProfileView",
    data() {
      return {
      }
    },
    methods: {
      logout() {
        this.$store.commit('LOGOUT_USER')
      },
    },
}
</script>

<style>

</style>