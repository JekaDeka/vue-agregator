<template lang="html">
<div class="main">
  <div class="">
    <div class="step-text">
      ШАГ 4
    </div>
    <div class="main-text">
      {{title}}
    </div>
    <div class="select">
      <a href="#FaultModal">выберите</a>
      <div id="FaultModal" class="FaultDialog">
        <div>
          <div class="container" v-if = "faults.length!=0">
            <div class="row">
              <div class="col col-lg col-sm">
                <div class="step-text">
                  ШАГ 4
                </div>
                <div class="main-text">
                  Выберите Неисправность
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
              <div class="col col-sm col-lg"  v-for=" item in faultsBySparePart">

                  <div class="text-aff">
                  <img src="" alt="">  {{item.spare_part.name}}
                  </div>
                  <div class="select-scroll">
                    <div class="select-type" v-for="fault in item.faults">

                        <a href="#close" v-on:click ="selectFault(type)">
                          {{fault.name}}
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
          <div class="container" v-else>
            <div class="row">
              <div class="col col-sm col-lg">
                  <div class="">
                    По данной модели ничего не найдено
                  </div>
              </div>
              <div class="col-1 col-sm-1 col-lg-1">
                <a href="#close" class="close" style="text-decoration:none;">X</a>
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
      seen: false,
      title: "Выберите Неисправность",
      faults: [],
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
        this.start = this.$store.getters.FAULTS_BY_SPARE_PART.length - 3
      else
        this.start -= 3
      if (this.end - 3 <= 0)
        this.end = this.$store.getters.FAULTS_BY_SPARE_PART.length
      else
        this.end -= 3
    },
    setNext: function() {
      if (this.start + 3 >= this.$store.getters.FAULTS_BY_SPARE_PART.length)
        this.start = 0
      else
        this.start += 3
      if (this.end + 3 > this.$store.getters.FAULTS_BY_SPARE_PART.length)
        this.end = 3
      else
        this.end += 3

    },
    selectDeviceType: function(fault) {
      this.seen = !this.seen
      this.$store.dispatch('SELECT_FAULT', fault)
      this.$store.dispatch('GET_BREAKAGE_ACTION_BY_FAULT', this.$store.getters.SELECTED_FAULT)
      this.title = this.$store.getters.SELECTED_FAULT.name
    }
  },
  computed: {
    deviceModelByAffilationList() {
      this.faults = this.$store.getters.FAULTS_BY_SPARE_PART
      var list_start = this.$store.getters.FAULTS_BY_SPARE_PART
      var list_result = []
      for (var i = this.start; i < this.end % (list_start.length + 1); i++) {
        list_result.push(list_start[i])
      }
      return list_result
    },
  },
}
</script>

<style lang="scss" scoped>
@import '@/assets/scss/search_one.scss';
@import '@/assets/scss/fault_model.scss';
</style>
