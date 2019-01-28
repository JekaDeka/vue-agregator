<template lang="html">
  <div class="container" id ="proposal">
    <div class="row">
      <div class="col col-sm col-lg">
        <div class="link">
        <a href="#ProposalModal">Оставить заявку</a>
        </div>

      </div>
    </div>
    <div class="ProposalDialog" id="ProposalModal">
      <div >
        <div class="container">
          <div class="row">
            <div class="col col-sm col-lg">
              <div class="main-text">
                Заполните поля
              </div>
            </div>
            <div class="col-1 col-sm-1 col-lg-1">
                    <a href="#close" class="close" style="text-decoration:none;">X</a>
            </div>
          </div>
          <div class="row justify-content-md-center">
            <div class="col-5 col-sm-5 col-lg-5">
            <div class="input">
              <input class="select-text" type="text" v-model = "name" name="" value="" placeholder="Ваше имя">

            </div>
              </div>
          </div>
          <div class="row row justify-content-md-center">
            <div class="col-5 col-sm-5 col-lg-5">
              <div class="input">
                <input class="select-text" v-model="number" type="text" name="" value="" placeholder="Телефон">

              </div>
              </div>
          </div>
          <div class="row row justify-content-md-center">
            <div class="col-5 col-sm-5 col-lg-5">
              <TheAffilationSearch></TheAffilationSearch>
            </div>
          </div>
          <div class="row row justify-content-md-center">
            <div class="col-5 col-sm-5 col-lg-5">
              <TheBrandSearch></TheBrandSearch>
            </div>
          </div>
          <div class="row row justify-content-md-center">
            <div class="col-5 col-sm-5 col-lg-5">
              <TheDeviceModelsSearch></TheDeviceModelsSearch>
            </div>
          </div>
          <div class="row row justify-content-md-center">
            <div class="col-5 col-sm-5 col-lg-5">
              <TheFaultSearch></TheFaultSearch>
            </div>
          </div>
          <div class="row row justify-content-md-center">
            <div class="col-5 col-sm-5 col-lg-5">
              <TheMetroSearch></TheMetroSearch>
            </div>
          </div>
          <div class="row row justify-content-md-center">
            <div class="col-5 col-sm-5 col-lg-5">
              <div class="link">
                <a href="#close"  v-on:click="postProposl">Оправить</a>
              </div>
            </div>
          </div>
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
  },
  data: function() {
    return {
      name: '',
      number: '',
      new_proposal: {
        "name": "",
        "number": "",
        "status": null,
        "device_type": null,
        "brand": null,
        "device_model": null,
        "fault": null,

        "metro": null
      },
    }
  },
  methods: {
    postProposl: function() {
      if (this.name != '' && this.number != '' && this.$store.getters.BOOL_METRO && this.$store.getters.BOOL_FAULT) {
        this.new_proposal.name = this.name
        this.new_proposal.number = this.number
        this.new_proposal.status = 1
        this.new_proposal.device_type = this.$store.getters.SELECTED_DEVICE_TYPE.id
        this.new_proposal.brand = this.$store.getters.SELECTED_BRAND.id
        this.new_proposal.device_model = this.$store.getters.SELECTED_DEVICE_MODEL.id
        this.new_proposal.fault = this.$store.getters.SELETED_FAULT.id
        this.new_proposal.metro = this.$store.getters.SELECTED_METRO.id
        this.$store.dispatch('POST_PROPOSAL', this.new_proposal)
      }
    }
  }

}
</script>

<style lang="scss" scoped>
@import '@/assets/scss/proposal.scss';
@import '@/assets/scss/step.scss';
</style>
