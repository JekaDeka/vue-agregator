<template lang="html">
<div class="main" v-if="BoolFault">
  <div class="container">
    <div class="row">
      <div class="col-8 col-sm-8 col-lg-8">
        <div class="step-text">
          ШАГ 5
        </div>
        <div class="main-text">
          {{getTitle}}
        </div>
        <div class="select">
          <a href="#MetroModal" v-on:clik="showSelect">выберите</a>
        </div>
      </div>
    </div>
  </div>
  <div id="MetroModal" class="MetroDialog">
    <div>
      <div class="container" >
        <div class="row">
          <div class="col col-lg col-sm">
            <div class="step-text">
              ШАГ 4
            </div>
            <div class="main-text">
              Выберите Метро
            </div>
          </div>
          <div class="col-1 col-sm-1 col-lg-1">
            <a href="#close" class="close" style="text-decoration:none;">X</a>
          </div>
        </div>
        <div class="row" >

             <div class="col col-sm col-lg">
               <div class="select-scroll">
                 <div class="select-type" v-for="item in metroList">

                     <a href="#close" v-on:click ="selectMetro(item)">
                       {{item.name}}
                   </a>

                 </div>
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
      town: '',
      title: 'Выберите метро',
      seen: false,
    }
  },
  mounted: function() {

    var url_list = window.location.pathname.split('/')
    var town = url_list[2]
    if (town != 'register' && town != '') {

      this.town = town.replace(town[0], town[0].toUpperCase())
      this.$store.dispatch('GET_METRO_LIST', this.town)
    }
  },
  computed: {
    metroList: function() {
      return this.$store.getters.METRO_LIST
    },
    BoolFault: function() {
      return this.$store.getters.BOOL_FAULT
    },
    getTitle() {
      if (this.$store.getters.BOOL_METRO)
        return this.$store.getters.SELECTED_METRO.name
      else
        return 'Выберите метро'
    }
  },
  methods: {
    showSelect: function() {
      this.seen = !this.seen
    },
    selectMetro: function(item) {
      this.$store.dispatch('SELECT_METRO', item)
      this.title = item.name
    }
  }
}
</script>

<style lang="scss" scoped>
@import '@/assets/scss/step.scss';
@import '@/assets/scss/metro_model.scss';
</style>
