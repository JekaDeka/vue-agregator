<template lang="html">
<div class="main">
<div class="">
  <div class="select" v-on:click = "showSelect">
    <div>
      
      {{title}}
    </div>
  </div>
  <div class="select-scroll" v-if="seen==1">
    <div class="select" v-bind:key="brand.id" v-for="brand in brands" >
      <div v-on:click = "selectBrand(brand)">
        {{brand.name}}
      </div>
    </div>
  </div>
  <div class="select" v-if="seen==2">
    <div class="">
      {{error_msg}}
    </div>
  </div>
</div>
</div>
</template>

<script>
export default {
  data: function() {
    return {
      seen: 0,
      title: "Производитель",
      error_msg: "Заполните сначала поле устройтсва",
      brands: [],
    }
  },
  methods: {
    showSelect: function() {
      if (this.seen != 0) {
        this.seen = 0
        return
      }
      if (this.$store.getters.BRANDS.length != 0) {
        this.seen = 1;
        this.brands = this.$store.getters.BRANDS
        return
      }

      this.seen = 2;
      return
    },
    selectBrand: function(brand) {
      this.title = brand.name
      this.seen = 0

      this.$store.dispatch('SELECT_BRAND', brand)
      this.$store.dispatch('GET_DEVICE_MODEL_BY_BRAND', [this.$store.getters.SELECTED_DEVICE_TYPE.id, brand.id])
    },
  }

}
</script>

<style lang="scss" scoped>
@import '@/assets/scss/rigth_select.scss';
</style>
