<template>
<div id="selection_one">
  <div class="container">
    <div class="row">
      <div class="col-3 col-sm-3 col-lg-3">
        <TheAffilationSearch></TheAffilationSearch>
      </div>
      <div class="col-1 col-sm-1 col-lg-1">
        <img src="@/assets/img/arrow_step.png" class="step-img" alt="">
      </div>
      <div class="col-3 col-sm-3 col-lg-3" v-if="BoolDeviceType">
        <div class="row">
          <div class="col-10 col-sm-10 col-lg-10">
            <TheBrandSearch> </TheBrandSearch>
          </div>
          <div class="col-1 col-sm-1 col-lg-1">
            <img src="@/assets/img/arrow_step.png" alt="" class="step-img">
          </div>
        </div>
      </div>

      <div class="col-3 col-sm-3 col-lg-3" v-if="BoolBrand">
        <div class="row">
          <div class="col col-sm col-lg">
            <TheDeviceModelsSearch></TheDeviceModelsSearch>
          </div>
          <div class="col-1 col-sm-1 col-lg-1">
            <img src="@/assets/img/arrow_step.png" alt="" class="step-img">
          </div>
        </div>
      </div>
      <div class="col-2 col-sm-2 col-lg-2" v-if="BoolDeviceModel">
        <div class="row">
          <div class="col col-sm col-g">
            <TheFaultSearch></TheFaultSearch>
          </div>
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col col-sm col-lg">
        <TheButtonPrice></TheButtonPrice>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import TheAffilationSearch from '@/components/AffilationsSearch';
import TheBrandSearch from '@/components/BrandSearch'
import TheDeviceModelsSearch from '@/components/DeviceModelSearch'
import TheFaultSearch from '@/components/FaultsSearch'
import TheButtonPrice from '@/components/ButtonPrice'
export default {
  name: 'selection_one',
  components: {
    TheAffilationSearch,
    TheBrandSearch,
    TheDeviceModelsSearch,
    TheFaultSearch,
    TheButtonPrice,
  },
  computed: {
    BoolDeviceType() {
      return this.$store.getters.BOOL_DEVICE_TYPE
    },
    BoolBrand() {
      return this.$store.getters.BOOL_BRAND
    },
    BoolDeviceModel() {
      return this.$store.getters.BOOL_DEVICE_MODEL
    },
  }
}
</script>

<style lang="scss" scoped>
@import '@/assets/scss/search_one.scss';
</style>
