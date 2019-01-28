<template lang="html">
  <div class="container">
    <div class="row">
      <div class="col col-sm col-lg">
        <div class="butttom-schet">
            <button type="button" name="button">Расчитать стоимость</button>
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col col-sm col-lg">
        <div class="">
          <div class="" v-if="seen">
            <div class="" v-for="item in ListBreakageAction">
              <div class="">
                Рузультат и возможные действия:
              </div>
              <div class="">
                {{item.name}} {{item.price}}
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
  date: function() {
    return {
      seen: false
    }
  },
  computed: {
    ListBreakageAction() {
      this.seen = this.$store.getters.BOOL_FAULT
      return this.$store.getters.BREAKAGE_ACTIONS
    }
  }
}
</script>

<style lang="scss" scoped>
@import '@/assets/scss/search_one.scss';
</style>
