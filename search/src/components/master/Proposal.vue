<template lang="html">
  <div class="container">
    <div class="row">
      <div class="">
        <div class="" v-for="item in list">
          <div class="">
            {{item.metro.name}}
          </div>
          <div class="" v-for="prop in item.proposals">
            <div class="">
              {{prop.name}}
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data: function() {
    return {
      list: [],
    }
  },
  mounted: function() {
    this.$store.dispatch('GET_PROPOSAL_BY_METRO', this.$store.getters.MANUFACTURE)
    this.list = this.$store.getters.PROPOSAL_METRO_LIST
  }
}
</script>

<style lang="css" scoped>
</style>
