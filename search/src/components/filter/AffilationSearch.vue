<template lang="html">
<div class="container">
<div class="row">
  <div class="col col-sm col-lg">
    <input  class="select-text" v-model="title" placeholder="Устройства" v-on:click="showAll">
    </div>
  </div>
  <div class="row">
    <div class="col col-sm col-lg">
      <div class="">
        <div class="filter-select" v-for="item in FilterAff">
          <div class="select-text" v-on:click="selectDeviceType(item)">
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

          <div class="text-aff">
              {{item.aff.name}}
          </div>
          <div class="" v-for ="device_type in item.device_types">
            <div class="select-text" v-on:click="selectDeviceType(device_type)">
              {{device_type.name}}
            </div>
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
    selectDeviceType: function(device_model) {

      this.seen = !this.seen
      this.seen_err = false
      this.$store.dispatch('SELECT_DEVICE_TYPE', device_model)
      this.$store.dispatch('GET_BRANDS', this.$store.getters.SELECTED_DEVICE_TYPE)
      this.title = this.$store.getters.SELECTED_DEVICE_TYPE.name
    }
  },
  mounted: function() {
    this.$store.dispatch('GET_DEVICE_TYPES_BY_AFFILATION')
  },
  computed: {
    FilterAff: function() {
      if (!this.seen) {
        if (this.$store.getters.BOOL_DEVICE_TYPE) {
          this.title = this.$store.getters.SELECTED_DEVICE_TYPE.name

        } else
          this.title = ''
      }

      if (this.title != '' && (this.seen)) {
        this.$store.dispatch('GET_FILTER_DEVICE_TYPE', this.title)
        if (this.$store.getters.FILTER_DEVICE_TYPE.length != 0) {
          this.seen_err = false
        } else {
          this.seen_err = true
        }
        return this.$store.getters.FILTER_DEVICE_TYPE
      }
      return []
    },
    ListAll: function() {
      return this.$store.getters.DEVICE_TYPES_BY_AFFILATION
    }
  }
}
</script>

<style lang="scss" scoped>
@import '@/assets/scss/filter/filter.scss';
@import '@/assets/scss/proposal.scss';
</style>
