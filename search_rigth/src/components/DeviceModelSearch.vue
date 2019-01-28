<template lang="html">
<div class="main">
  <div class="select" v-on:click = "showSelect">
    <div>
      {{title}}
    </div>
  </div>
  <div class="select-scroll" v-if="seen==1">
    <div class="select" v-bind:key="item.id" v-for="item in device_models" >
      <div v-on:click = "select(item)">
        {{item.name}}
      </div>
    </div>
  </div>
  <div class="select" v-if="seen==2">
    <div class="">
      {{error_msg}}
    </div>
  </div>
</div>

</template>

<script>
export default {
  data: function() {
    return {
      seen: 0,
      title: "Модель",
      error_msg: "Заполните сначала поле производитель",
      device_models: [],
    }
  },
  methods: {
    showSelect: function() {
      if (this.seen != 0) {
        this.seen = 0
        return
      }
      if (this.$store.getters.DEVICE_MODELS.length != 0) {

        this.seen = 1;
        this.device_models = this.$store.getters.DEVICE_MODELS
        return
      }

      this.seen = 2;
      return
    },
    select: function(obj) {
      this.title = obj.name
      this.seen = 0

      this.$store.dispatch('SELECT_DEVICE_MODEL', obj)
      this.$store.dispatch('GET_BREAKAGE_ACTIONS_BY_DEVICE_MODEL', obj)
    },
  }

}
</script>

<style lang="scss" scoped>
@import '@/assets/scss/rigth_select.scss';
</style>
