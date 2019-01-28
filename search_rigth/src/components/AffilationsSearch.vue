<template lang="html">
  <div  class ="main">
    <div class="select" v-on:click="showSelect">
      <div>

        {{title}}
      </div>
    </div>
    <div class="select-scroll" v-if="seen">
      <div class="" v-bind:key="item.id"  v-for ="item in deviceModelByAffilationList">

          <div class="text-aff">
            {{item.aff.name}}
          </div>


        <div class="">
            <div class="" v-bind:key="device_type.id" v-for="device_type in item.device_types">
              <div class="select" v-on:click="selectDeviceType(device_type)">
                <div>
                    {{device_type.name}}
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
      title: "Устройства",
    }
  },
  methods: {
    showSelect: function() {
      this.seen = !this.seen
      return this.seen
    },
    selectDeviceType: function(device_model) {

      this.seen = !this.seen
      this.$store.dispatch('SELECT_DEVICE_TYPE', device_model)
      this.$store.dispatch('GET_BRAND_BY_DEVICE_TYPE', this.$store.getters.SELECTED_DEVICE_TYPE)
      this.title = this.$store.getters.SELECTED_DEVICE_TYPE.name
    }
  },
  mounted() {
    this.$store.dispatch('GET_DEVICE_TYPES_BY_AFFILATION')
  },
  computed: {
    deviceModelByAffilationList() {
      return this.$store.getters.DEVICE_TYPES_BY_AFFILATION
    },
  },
}
</script>

<style lang="scss" scoped>
@import '@/assets/scss/rigth_select.scss';
</style>
