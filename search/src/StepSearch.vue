<template>
<div class="container" id="step_search">
  <div class="row">
    <div class="col col-sm col-lg">
      <TheAffilationSearch></TheAffilationSearch>
    </div>
    <div class="col col-sm col-lg">
      <TheBrandSearch></TheBrandSearch>
    </div>
    <div class="col col-smcol-lg">
      <TheDeviceModelsSearch></TheDeviceModelsSearch>
    </div>
    <div class="col col-sm col-lg">
      <TheFaultSearch></TheFaultSearch>
    </div>
    <div class="col col-sm col-lg">
      <TheMetroSearch></TheMetroSearch>
    </div>
  </div>
  <div class="row">
    <div class="col col-sm col-lg">
      <ThePrice></ThePrice>
    </div>
  </div>
</div>
</template>

<script>
import TheAffilationSearch from '@/components/step/AffilationSearch';
import TheBrandSearch from '@/components/step/BrandSearch'
import TheDeviceModelsSearch from '@/components/step/DeviceModelSearch'
import TheFaultSearch from '@/components/step/FaultsSearch'
import TheMetroSearch from '@/components/step/MetroSearch'
import ThePrice from '@/components/Price'
export default {
  name: 'selection_one',
  components: {
    TheAffilationSearch,
    TheBrandSearch,
    TheDeviceModelsSearch,
    TheFaultSearch,
    TheMetroSearch,
    ThePrice,
  },
}
</script>

<style lang="scss" scoped>
@import '@/assets/scss/step.scss';
</style>
