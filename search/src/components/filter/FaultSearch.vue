<template lang="html">
<div class="container">
<div class="row">
  <div class="col col-sm col-lg">
    <input  class="select-text" v-model="title" placeholder="Неисправности" v-on:click="showAll">
    </div>
  </div>
  <div class="row">
    <div class="col col-sm col-lg">
      <div class="">
        <div class="filter-select" v-for="item in FilterFault">

          <div class="select-text" v-on:click="selectFault(item)">
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

          <div class="text-aff"  >
              {{item.spare_part.name}}
          </div>

          <div class="" v-for="fault in item.faults">
            <div class="select-text" v-on:click="selectFault(fault)">
              {{fault.name}}
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
    selectFault: function(fault) {

      this.seen = !this.seen
      this.$store.dispatch('SELECT_FAULT', fault)
      // this.$store.dispatch('GET_BREAKAGE_ACTIONS_BY_FAULT', this.$store.getters.SELECTED_FAULT)
      this.title = this.$store.getters.SELETED_FAULT.name

    },
  },
  computed: {
    FilterFault: function() {
      if (!this.seen) {
        if (this.$store.getters.BOOL_FAULT)
          this.title = this.$store.getters.SELETED_FAULT.name
        else
          this.titel = ''
      }

      if (this.title != '' && (this.seen) && (this.$store.getters.BOOL_DEVICE_MODEL)) {
        this.$store.dispatch('GET_FILTER_FAULT', this.title)
        if (this.$store.getters.FILTER_FAULT.length != 0) {
          this.seen_err = false
        } else {
          this.seen_err = true
        }
        return [this.$store.getters.FILTER_FAULT[0]]
      }
      return []
    },
    ListAll: function() {
      return this.$store.getters.FAULTS_BY_SPARE_PART
    }
  }
}
</script>

<style lang="scss" scoped>
@import '@/assets/scss/filter/filter.scss';
@import '@/assets/scss/proposal.scss';
</style>
