<template lang="html">
  <div class="container">
    <div class="row">
      <div class="col col-sm col-lg">
        <div class="">
          <button v-on:click="addBrand" type="button" name="button">Add Brand</button>
        </div>
      </div>

    </div>
    <div class="row" v-for="index in creates">
      <div class="col col-sm col-lg">
        <TheAdd></TheAdd>
      </div>
    </div>
    <div class="row">
      <div class="col col-sm col-lg">
        <div class="">
          Выбранные вами ранее услуги
        </div>
        <div class="">
          <button v-on:click = "ShowService" type="button" name="button">Show</button>
        </div>
        <div class="" v-if="seen">
          <TheService></TheService>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import TheAdd from './search/Add'
import TheService from './search/Service'
export default {
  data: function() {
    return {
      creates: [],
      manufacture_services: [],
      brands: [],
      count: -1,
      seen: false,

    }
  },
  methods: {
    ShowService: function() {
      this.seen = !this.seen
    },
    addBrand: function() {
      this.count += 1
      this.creates.push(this.count)
    },
    deleteBrand: function(index) {

      this.creates.splice(index, 1)
      for (var i = index; i < this.creates.length; i++)
        this.creates[i] -= 1
    }
  },
  mounted: function() {
    this.brands = this.$store.getters.SELECTED_BRANDS
  },
  components: {
    TheAdd,
    TheService,
  }
}
</script>

<style lang="css" scoped>
</style>
