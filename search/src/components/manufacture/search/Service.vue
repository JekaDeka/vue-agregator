<template lang="html">
  <div class="container" >

    <div class="row" v-for="(item,index) in listsSP">
      <div class="col col-sm col-lg">
        <div class="">
          {{item.brand.name}}
        </div>
      </div>
      <div class="col col-sm col-lg">
        <div class="">
          {{item.mark.name}}
        </div>

      </div>
      <div class="col col-sm col-lg">
        <div class="">
          <input v-model="checks[index]" type="checkbox" name="" value="">
          <label for="checkbox">{{item.breakage_action.name}}</label>
          <input v-if="checks[index]" v-model="item.manufacture_service.price" type="text" name="" value="">
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col col-sm col-lg">
        <button  v-on:click="Save"type="button" name="button">Save</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data: function() {
    return {
      list: [],
      checks: [],
    }
  },
  mounted: function() {
    this.$store.dispatch('GET_MANUFACTURE_SERVICE_BY_MANUFACTURE', this.$store.getters.MANUFACTURE)
    this.list = this.$store.getters.SPECIAL_MANUFACTURE_SERVICES
    for (var i = 0; i < this.list.length; i++) {
      this.checks.push(true)
    }
  },
  methods: {
    Save: function() {
      for (var i = 0; i < this.list.length; i++) {
        if (this.checks[i] == true) {
          this.$store.dispatch('PUT_MANUFACTURE_SERVICE', this.list[i].manufacture_service)
        } else {
          this.$store.dispatch('DELETE_MANUFACTURE_SERVICE', this.list[i].manufacture_service)
        }
      }
    }

  },
  computed: {
    listsSP() {
      this.list = this.$store.getters.SPECIAL_MANUFACTURE_SERVICES
      for (var i = 0; i < this.list.length; i++) {
        if (i < this.checks.length)
          continue;
        else
          this.checks.push(true)
      }
      return this.list
    }

  }
}
</script>

<style lang="css" scoped>
</style>
