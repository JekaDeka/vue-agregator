<template lang="html">
<div class="container" v-if="seen_module" >
  <div class="row">
    <div class="col col-sm col-lg">
      <input  class="select-text" v-model="title" placeholder="Бранд" v-on:click="showAll">
    </div>
    <div class="col col-sm col-lg">
      <div class="">
          <button v-on:click="deleteBrand" type="button" name="button">Delete</button>
      </div>
    </div>
    </div>
  <div class="row"  v-if="seen">
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
  <div class="row"  v-if="seen">
    <div class="col col-sm col-lg">
      <div class="select-scroll">
        <div class="" v-for ="item in ListAll">

          <div class="select-text" v-on:click="selectBrand(item)" >
              {{item.name}}
          </div>
        </div>
      </div>
    </div>
  </div>

  <div class="row">
    <div class="col col-sm col-lg">
      <div class="" v-for="(item,i) in breakage_actions_with_mark" >
        <div class="" v-on:click="ShowBreakageAction(i)">
          {{item.mark.name}}
        </div>
        <div class="" v-if="Seens[i]">
          <div class=""  v-for="(br,j) in item.breakage_actions">
            <div class="">
              <input v-model='checks[i][j]' type="checkbox" name="" value="">
              <label for="checkbox">{{br.name}}</label>
              <input v-if ="checks[i][j]" v-model='prices[i][j]' type="text" name="" value="">
            </div>

          </div>
        </div>

      </div>
    </div>

  </div>
  <div class="row">
    <div class="col col-sm col-lg">
      <div class="">
        <button v-on:click="Save()" type="button" name="button">Save</button>
      </div>
    </div>
  </div>
</div>
</template>

<script>
export default {
  data: function() {
    return {
      seen_module: true,
      seen_brakage_action: false,
      checks: [],
      prices: [],
      seens: [],
      title: "",
      seen: true,
      seen_err: false,
      selected_brand: {},
      breakage_actions_with_mark: []
    }
  },
  methods: {
    showAll: function() {
      this.seen = !this.seen
    },
    deleteBrand: function() {
      this.seen_module = false
    },

    selectBrand: function(brand) {
      this.seen_err = false
      this.seen = 0
      this.seen_brakage_action = true

      this.title = brand.name
      this.selected_brand = brand
      this.$store.dispatch('GET_BRAKAGE_ACTIONS_BY_BRAND', brand)
      this.breakage_actions_with_mark = this.$store.getters.BREAKAGE_ACTIONS_WITH_MARK
      this.checks = []
      this.prices = []
      for (var i = 0; i < this.breakage_actions_with_mark.length; i++) {
        var t = []
        var p = []
        for (var j = 0; j < this.breakage_actions_with_mark[i].breakage_actions.length; j++) {
          t.push(false)
          p.push(0)
        }
        this.seens.push(true)
        this.checks.push(t)
        this.prices.push(p)
      }

    },
    Save: function() {

      for (var i = 0; i < this.breakage_actions_with_mark.length; i++) {
        for (var j = 0; j < this.breakage_actions_with_mark[i].breakage_actions.length; j++) {

          if (this.checks[i][j] == true) {
            var manufacture_service = {

              price: null,
              manufacture: null,
              mark: null,
              master: this.$store.getters.MANUFACTURE.id,
              breaking_action: null
            }

            manufacture_service.price = this.prices[i][j]
            manufacture_service.mark = this.breakage_actions_with_mark[i].mark.id
            manufacture_service.breaking_action = this.breakage_actions_with_mark[i].breakage_actions[j].id

            this.$store.dispatch('POST_MANUFACTURE_SERVICE', manufacture_service)
          }

        }

      }
      this.seen_module = false
      this.$store.dispatch('SET_EMPTY_BREAKAGE_ACTIONS_WITH_MARK')
      this.breakage_actions_with_mark = []


    },
    ShowBreakageAction: function(i) {

      this.seens[i] = !this.seens
      this.$nextTick()

    }
  },
  mounted: function() {
    this.$store.dispatch('GET_BRANDS')
  },
  computed: {
    FilterBrand: function() {
      if (this.title != '' && (this.seen)) {
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
    Seens: function() {
      return this.seens
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
