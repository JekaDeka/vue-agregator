<template lang="html">
<div class="main">
<div class="container">
  <div class="row">
    <div class="col-9 col-sm-9 col-lg-9">
      <div class="step-text">
        ШАГ 1
      </div>
      <div class="main-text">
        {{getTitle}}
      </div>
      <div class="select">
        <a href="#AffModal">выберите</a>
    </div>
  </div>
  <div class="">
    <img src="@/assets/img/arrow_step.png" class="step-img" alt="">
  </div>
</div>
</div>
<div id="AffModal" class="AffDialog">
  <div>
    <div class="container">
      <div class="row">
        <div class="col col-lg col-sm">
          <div class="step-text">
            ШАГ 1
          </div>
          <div class="main-text">
            Выберите Устройтсво
          </div>
        </div>
        <div class="col-1 col-sm-1 col-lg-1">
          <a href="#close" class="close" style="text-decoration:none;">X</a>
        </div>
      </div>
      <div class="row">
        <div class="col-1 col-lg-1 col-sm-1" v-on:click="setBefore">
          <div class="button">
              <img src="@/assets/img/arrow_before.png" alt="">
          </div>

        </div>
        <div class="col col-sm col-lg"  v-for=" item in deviceModelByAffilationList">

            <div class="text-aff">
            <img src="" alt="">  {{item.aff.name}}
            </div>
            <div class="select-scroll">
              <div class="select-type" v-for="type in item.device_types">

                  <a href="#close" v-on:click ="selectDeviceType(type)">
                    {{type.name}}
                </a>

              </div>
            </div>
        </div>
        <div class="col-1 col-lg-1 col-sm-1" v-on:click="setNext">
          <div class="button">
              <img src="@/assets/img/arrow_next.png" alt="">
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
  data: function() {
    return {
      seen: false,
      title: "Выберите Устройство",
      start: 0,
      end: 3,
    }
  },
  methods: {
    showSelect: function() {
      this.seen = !this.seen
      return this.seen
    },
    setBefore: function() {
      if (this.start - 3 < 0)
        this.start = this.$store.getters.DEVICE_TYPES_BY_AFFILATION.length - 3
      else
        this.start -= 3
      if (this.end - 3 <= 0)
        this.end = this.$store.getters.DEVICE_TYPES_BY_AFFILATION.length
      else
        this.end -= 3
    },
    setNext: function() {
      if (this.start + 3 >= this.$store.getters.DEVICE_TYPES_BY_AFFILATION.length)
        this.start = 0
      else
        this.start += 3
      if (this.end + 3 > this.$store.getters.DEVICE_TYPES_BY_AFFILATION.length)
        this.end = 3
      else
        this.end += 3

    },
    selectDeviceType: function(device_model) {

      this.seen = !this.seen
      this.$store.dispatch('SELECT_DEVICE_TYPE', device_model)
      this.$store.dispatch('GET_BRANDS', this.$store.getters.SELECTED_DEVICE_TYPE)
      this.title = this.$store.getters.SELECTED_DEVICE_TYPE.name
    }
  },
  mounted() {
    this.$store.dispatch('GET_DEVICE_TYPES_BY_AFFILATION')
    if (this.$store.BOOL_DEVICE_TYPE)
      this.title = this.$store.SELECT_DEVICE_TYPE.name
  },
  computed: {
    deviceModelByAffilationList() {
      var list_start = this.$store.getters.DEVICE_TYPES_BY_AFFILATION
      var list_result = []
      for (var i = this.start; i < this.end % (list_start.length + 1); i++) {
        list_result.push(list_start[i])
      }
      return list_result
    },
    getTitle() {
      if (this.$store.getters.BOOL_DEVICE_TYPE)
        return this.$store.getters.SELECTED_DEVICE_TYPE.name
      else
        return 'Выберите устройство'
    }
  },
}
</script>

<style lang="scss" scoped>
@import '@/assets/scss/step.scss';
</style>
