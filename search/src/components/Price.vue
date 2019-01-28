<template lang="html">
  <div class="container">
    <div class="row">
      <div class="col-10 col-sm-12 col-lg-11">
        <div class="result" style="text-aling:center">
            <a v-bind:href="getUrl">Расчитать результат</a>
        </div>
      </div>
    </div>
  </div>


</template>

<script>
export default {
  data: function() {
    return {
      metro: "",
    }
  },
  computed: {
    getUrl: function() {
      if (this.$store.getters.BOOL_METRO) {
        var path = window.location.pathname
        path = path.split('/')
        var url = ''
        var town = path[2]
        town = town.replace(town[0], town[0].toUpperCase())
        var device_model = this.$store.getters.SELECTED_DEVICE_MODEL
        url = window.location.origin + '/' + path[1] + '/' + town + '/' + device_model.brand + '/' + device_model.mark + '/' + device_model.id + '/' + this.$store.getters.SELETED_FAULT.id + '/' + this.$store.getters.SELECTED_METRO.id + '/'
        return url
      }
    },
  },
}
</script>

<style lang="scss" scoped>
@import '@/assets/scss/step.scss';
</style>
