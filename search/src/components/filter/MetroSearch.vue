<template lang="html">
<div class="container">
<div class="row">
  <div class="col col-sm col-lg">
    <input  class="select-text" v-model="title" placeholder="Метро" v-on:click="showAll">
    </div>
  </div>
  <div class="row">
    <div class="col col-sm col-lg">
      <div class="">
        <div class="filter-select" v-for="item in FilterMetro">

          <div class="select-text" v-on:click="selectMetro(item)">
            {{item.name}}
          </div>
        </div>
        <div class="filter-select" v-if="seen_err">
          <div class="select-text">
            Ничего не найдено
          </div>
        </div>

      </div>

    </div>
  </div>
  <div class="row">
    <div class="col col-sm col-lg">
      <div class="select-scroll" v-if="seen">
        <div class="" v-for ="item in ListAll">

          <div class="select-text" v-on:click="selectMetro(item)" >
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
      title: "",
      seen: false,
      seen_err: false,
    }
  },
  methods: {
    showAll: function() {
      this.seen = !this.seen
    },
    selectMetro: function(item) {
      this.seen = false
      this.seen_err = false
      this.$store.dispatch('SELECT_METRO', item)
      this.title = this.$store.getters.SELECTED_METRO.name
    }
  },
  computed: {
    FilterMetro: function() {
      if (!this.seen) {
        if (this.$store.getters.BOOL_METRO)
          this.title = this.$store.getters.SELECTED_METRO.name
        else
          this.title = ''
      }

      if (this.title != '' && (this.seen)) {
        this.$store.dispatch('GET_FILTER_METRO', this.title)
        if (this.$store.getters.FILTER_METRO.length != 0) {
          this.seen_err = false
        } else {
          this.seen_err = true
        }
        return this.$store.getters.FILTER_METRO
      }
      return []
    },
    ListAll: function() {
      return this.$store.getters.METRO_LIST
    }
  }
}
</script>

<style lang="scss" scoped>
@import '@/assets/scss/filter/filter.scss';
@import '@/assets/scss/proposal.scss';
</style>
