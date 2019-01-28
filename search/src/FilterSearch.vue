<template lang="html">
  <div class="" id ="filter_search">
  <div class="container">
    <div class="row">
      <div class="col col-sm-5 col-lg-3">
        <TheAffilationSearch></TheAffilationSearch>
      </div>
      <div class="col col-sm-5 col-lg-3">
        <TheBrandSearch></TheBrandSearch>
      </div>
      <div class="col col-sm-5 col-lg-3">
        <TheDeviceModelsSearch></TheDeviceModelsSearch>
      </div>
      <div class="col col-sm-5 col-lg-3">
        <TheFaultSearch></TheFaultSearch>
      </div>
      <div class="col col-sm-5 col-lg-3">
        <TheMetroSearch></TheMetroSearch>
      </div>
      <div class="col col-sm-5 col-lg-4">
        <ThePrice></ThePrice>
      </div>

    </div>
  </div>
  </div>
</template>

<script>
import TheAffilationSearch from '@/components/filter/AffilationSearch.vue'
import TheBrandSearch from '@/components/filter/BrandSearch.vue'
import TheDeviceModelsSearch from '@/components/filter/DeviceModelSearch.vue'
import TheFaultSearch from '@/components/filter/FaultSearch.vue'
import TheMetroSearch from '@/components/filter/MetroSearch.vue'
import ThePrice from '@/components/Price.vue'
export default {
  components: {
    TheAffilationSearch,
    TheBrandSearch,
    TheDeviceModelsSearch,
    TheFaultSearch,
    TheMetroSearch,
    ThePrice,
  }
}
</script>

<style lang="scss" scoped>
@import '@/assets/scss/filter/filter.scss';
</style>
