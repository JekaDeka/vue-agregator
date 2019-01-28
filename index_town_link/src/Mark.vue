<template lang="html">
<div class="" id="marks">
  <div class="container">
    <div class="row">
      <div class="col-1 col-sm-1 col-lg-1" v-on:click="setBefore">
        <img src="@/assets/img/arrow_before.png" alt="">
      </div>

      <div class="col col-sm col-lg">
        <div class="row">
          <div class="col col-sm col-lg" v-for="item in ListData">
            <a v-bind:href="getUrl(item)"> {{item.name}} </a>
          </div>
        </div>
        <div class="row">
          <div class="col col-sm col-lg">
            <div class="all-list" v-on:click="showAll">
              Смотерть весь список
              <img src="@/assets/img/arrow_down.png" alt="">
            </div>
            <div class="all" v-if="seen">
              <div class="" v-for="item in List">
                <a v-bind:href="getUrl(item)">{{item.name}}</a>
              </div>
            </div>
          </div>

        </div>
      </div>
      <div class="col-1 col-sm-1 col-lg-1" v-on:click="setNext">
        <img src="@/assets/img/arrow_next.png" alt="">
      </div>
    </div>
  </div>
</div>
</template>

<script>
export default {
  name: 'brand',
  data: function() {
    return {
      data: [],
      seen: false,
      start: 0,
      end: 3,
    }
  },
  mounted: function() {
    this.$store.dispatch('GET_MARKS')

  },
  computed: {
    List: function() {
      this.data = this.$store.getters.MARKS
      return this.data
    },
    ListData: function() {
      var list_result = [];
      var list = this.$store.getters.MARKS

      for (var i = this.start; i < this.end % (this.$store.getters.MARKS.length + 1); i++) {
        list_result.push(list[i])
      }
      return list_result
    },
  },
  methods: {
    getUrl: function(item) {

      return item.brand + '/' + item.id + '/'
    },
    setBefore: function() {

      if (this.start - 3 <= -3) {
        this.start = this.$store.getters.MARKS.length - 3
        this.end = this.$store.getters.MARKS.length
        return
      } else if (this.start - 3 < 0) {
        this.start = 0
        this.end = 3
        return
      } else {
        this.start -= 3
        this.end = this.start + 3
      }
    },
    showAll: function() {
      this.seen = !this.seen
    },
    setNext: function() {
      if (this.end + 3 >= this.$store.getters.MARKS.length + 3) {
        this.end = 3
        this.start = 0
      } else if (this.end + 3 >= this.$store.getters.MARKS.length) {
        this.end = this.$store.getters.MARKS.length
        this.start = this.end - 3
      } else {
        this.end += 3
        this.start = this.end - 3
      }
    },
  },
}
</script>

<style lang="scss" scoped>
@import '@/assets/scss/marks.scss'
</style>
