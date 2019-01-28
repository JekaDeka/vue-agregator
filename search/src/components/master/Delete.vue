<template lang="html">
  <div class="container">
    <div class="row">
      <div class="col col-sm col-lg">
        <div class="">
          Нажмите для удаления
        </div>
        <div class="">
          <button  v-on:click="Delete"type="button" name="button">Delete</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    Delete: function() {
      var url = window.location.pathname
      var list = url.split('/')
      var go_url = list[1] + '/' + 'register' + '/' + 'login/'
      this.$store.dispatch('DELETE_MASTER', this.$store.getters.MASTER)

      window.location.pathname = go_url
    }
  }
}
</script>

<style lang="css" scoped>
</style>
