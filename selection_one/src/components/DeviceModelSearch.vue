<template lang="html">
<div class="main">
  <div class="">
    <div class="step-text">
      ШАГ 3
    </div>
    <div class="main-text">
      {{title}}
    </div>
    <div class="select">
      <a href="#DeviceModal" v-on:clik="showSelect">выберите</a>
      <div id="DeviceModal" class="DeviceModelDialog">
        <div>
          <div class="container">
            <div class="row">
              <div class="col col-lg col-sm">
                <div class="step-text">
                  ШАГ 3
                </div>
                <div class="main-text">
                  Выберите Модель
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


              <div class="col col-sm col-lg" v-for="item in ListDeviceModel">
                  <div class="select-type">
                    <div>
                      <a href="#close" v-on:click ="selectDeviceModel(item)">{{item.name}}</a>
                    </div>
                  </div>
              </div>
              <div class="col-1 col-lg-1 col-sm-1" v-on:click="setNext">
                <div class="button">
                    <img src="@/assets/img/arrow_next.png" alt="">
                </div>

              </div>
            </div>
            <div class="row justify-content-md-center">
              <div class="col-10 col-lg-10 col-sm-10">
                <div class="select-type" v-on:click="showSelect">
                <div class="all-list">
                  Смотреть полный список
                  <img src="@/assets/img/arrow_down.png" alt="hey">
                </div>
                </div>
                <div class="select-scroll" v-if="seen">
                  <div class="select-type" v-for ="item in device_models">
                    <div>
                      <a href="#close" v-on:click="selectDeviceModel(item)">{{item.name}}</a>
                    </div>
                  </div>
                </div>
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
      title: "Выберите Модель",
      error_msg: "Заполните сначала поле устройтсва",
      start: 0,
      end: 3,
      device_models: [],
    }
  },
  methods: {
    showSelect: function() {
      this.seen = !this.seen
    },

    setBefore: function() {
      if (this.start - 3 <= -3) {
        this.start = this.$store.getters.DEVICE_MODELS.length - 3
        this.end = this.$store.getters.DEVICE_MODELS.length
      } else if (this.start - 3 < 0) {
        this.start = 0
        this.end = 3
      } else {
        this.start -= 3
        this.end -= 3
      }
    },
    setNext: function() {
      if (this.end + 3 >= this.$store.getters.DEVICE_MODELS.length + 3) {
        this.end = 3
        this.start = 0
      } else if (this.end + 3 >= this.$store.getters.DEVICE_MODELS.length) {
        this.end = this.$store.getters.DEVICE_MODELS.length
        this.start = this.end - 3
      } else {
        this.end += 3
        this.start = this.end - 3
      }

    },

    selectDeviceModel: function(item) {
      this.title = item.name
      this.seen = 0

      this.$store.dispatch('SELECT_DEVICE_MODEL', item)
      this.$store.dispatch('GET_FAULTS_BY_SPARE_PART', item)

    },
  },
  computed: {
    ListDeviceModel: function() {
      this.device_models = this.$store.getters.DEVICE_MODELS
      var list_result = []
      for (var i = this.start; i < this.end; i++) {
        list_result.push(this.device_models[i])
      }
      return list_result
    },
  }

}
</script>

<style lang="scss" scoped>
@import '@/assets/scss/search_one.scss';
@import '@/assets/scss/device_model_dialog.scss';
</style>
