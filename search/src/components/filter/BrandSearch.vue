<template lang="html">
<div class="container">
<div class="row">
  <div class="col col-sm col-lg">
    <input  class="select-text" v-model="title" placeholder="Бранд" v-on:click="showAll">
    </div>
  </div>
  <div class="row">
    <div class="col col-sm col-lg">
      <div class="">
        <div class="filter-select" v-for="item in FilterBrand">

          <div class="select-text" v-on:click="selectBrand(item)">
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

          <div class="select-text" v-on:click="selectBrand(item)" >
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
    selectBrand: function(brand) {
      this.seen_err = false
      this.seen = 0

      this.$store.dispatch('SELECT_BRAND', brand)
      this.$store.dispatch('GET_DEVICE_MODEL_BY_BRAND', [this.$store.getters.SELECTED_DEVICE_TYPE.id, brand.id])
      this.title = this.$store.getters.SELECTED_BRAND.name

    },
  },
  mounted: function() {
    this.$store.dispatch('GET_DEVICE_TYPES_BY_AFFILATION')
  },
  computed: {
    FilterBrand: function() {
      if (!this.seen) {
        if (this.$store.getters.BOOL_BRAND) {
          this.title = this.$store.getters.SELECTED_BRAND.name
        } else
          this.title = ''
      }

      if (this.title != '' && (this.seen) && this.$store.getters.BOOL_DEVICE_TYPE) {
        this.$store.dispatch('GET_BRAND_FILTER', this.title)
        if (this.$store.getters.FILTER_BRAND.length != 0) {
          this.seen_err = false
        } else {
          this.seen_err = true
        }
        return this.$store.getters.FILTER_BRAND
      }
      return []
    },
    ListAll: function() {
      return this.$store.getters.BRANDS
    }
  }
}
</script>

<style lang="scss" scoped>
@import '@/assets/scss/filter/filter.scss';
@import '@/assets/scss/proposal.scss';
</style>
