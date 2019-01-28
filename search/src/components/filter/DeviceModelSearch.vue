<template lang="html">
<div class="container">
<div class="row">
  <div class="col col-sm col-lg">
    <input  class="select-text" v-model="title" placeholder="Модель" v-on:click="showAll">
    </div>
  </div>
  <div class="row">
    <div class="col col-sm col-lg">
      <div class="">
        <div class="filter-select" v-for="item in FilterDeviceModel">

          <div class="select-text" v-on:click="selectDeviceModel(item)">
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

          <div class="select-text" v-on:click="selectDeviceModel(item)" >
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
    selectDeviceModel: function(item) {
      this.seen_err = false
      this.seen = false

      this.$store.dispatch('SELECT_DEVICE_MODEL', item)
      this.$store.dispatch('GET_FAULTS_BY_SPARE_PART', item)
      this.title = this.$store.getters.SELECTED_DEVICE_MODEL.name
    },
  },
  computed: {
    FilterDeviceModel: function() {
      if (!this.seen) {
        if (this.$store.getters.BOOL_DEVICE_MODEL) {
          this.title = this.$store.getters.SELECTED_DEVICE_MODEL.name
        } else {
          this.title = ''
        }
      }

      if (this.title != '' && (this.seen) && (this.$store.getters.BOOL_BRAND)) {
        this.$store.dispatch('GET_FILTER_DEVICE_MODEL', this.title)
        if (this.$store.getters.FILTER_DEVICE_MODEL.length != 0) {
          this.seen_err = false
        } else {
          this.seen_err = true
        }
        return this.$store.getters.FILTER_DEVICE_MODEL
      }
      return []
    },
    ListAll: function() {
      return this.$store.getters.DEVICE_MODELS
    }
  }
}
</script>

<style lang="scss" scoped>
@import '@/assets/scss/filter/filter.scss';
@import '@/assets/scss/proposal.scss';
</style>
