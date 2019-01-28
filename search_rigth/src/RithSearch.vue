<template>
<div id="search_rigth" class="search_rigth">
  <div class="container">
    <div class="row">
      <div class="col col-lg col-sm">
        <TheAffilationsSearch></TheAffilationsSearch>
      </div>

      <div class="col col-lg col-sm">
        <TheBrandSearch></TheBrandSearch>
      </div>



      <div class="col col-lg col-sm">
        <TheDeviceModelSearch></TheDeviceModelSearch>
      </div>


      <div class="col col-sm col-lg">
        <TheBreakageActionSearch></TheBreakageActionSearch>
      </div>


      <div class="col col-lg col-sm">
        <div class="button">
          <button type="button" name="button" v-on:click="breakageActionList"> Расчитать стоимость</button>
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col col-sm col-lg">
        <div class="result" v-if="seen==1">

          Стоимость: {{breakage_action.price}}
        </div>
        <div class="result" v-if="seen==2">
          Что-то пошло не так
        </div>
      </div>
    </div>

  </div>
</div>
</template>

<script>
import TheAffilationsSearch from '@/components/AffilationsSearch';
import TheBrandSearch from '@/components/BrandSearch';
import TheDeviceModelSearch from '@/components/DeviceModelSearch';
import TheBreakageActionSearch from '@/components/BreakageActionSearch';

export default {
  components: {
    TheAffilationsSearch,
    TheBrandSearch,
    TheDeviceModelSearch,
    TheBreakageActionSearch,

  },
  data: function() {
    return {
      seen: 0,
      breakage_actions: {}
    }
  },
  methods: {
    breakageActionList: function() {
      this.breakage_actions = this.$store.getters.SELECTED_BREAKAGE_ACTION
      if (this.$store.getters.BOOL_BREAKAGE_ACTION) {
        this.seen = 1
      } else {
        this.seen = 2
      }
    }
  }
}
</script>

<style lang="scss" scoped>
@import '@/assets/scss/rigth_select.scss';
</style>
