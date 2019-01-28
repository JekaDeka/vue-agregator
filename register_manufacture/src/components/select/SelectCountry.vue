<template lang="html">
  <div class="container">
<div class="row">
  <div class="col col-sm col-lg">
    <div class="" v-on:click="showList">
      {{title}}
    </div>
  </div>
</div>
<div class="row">
  <div class="col col-sm col-lg">
    <div class="" v-if = "seen">
      <div class="" v-for ="item in listObj">
        <div class="" v-on:click="selectObj(item)">
          {{item.name}}
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
      hello: 'hello',
      title: 'Выберите страну',
      seen: false
    }
  },
  created: function() {
    this.$store.dispatch('GET_COUNTRYES')
  },
  computed: {
    listObj: function() {
      return this.$store.getters.COUNTRYES
    },
  },
  methods: {
    showList: function() {
      this.seen = !this.seen
    },
    selectObj: function(item) {
      this.seen = false
      this.$store.dispatch('SELECT_COUNTRY', item)
      this.title = this.$store.getters.SELECTED_COUNTRY.name
    }

  }
}
</script>

<style lang="scss" scoped>
</style>
