<template lang="html">
  <div class="container">
<!-- adress -->
    <div class="row">
      <div class="col col-sm col-lg">
        <div class="row">
          <div class="col col-sm col-lg">
            Город
          </div>
        </div>
          <div class="row">
            <div class="col col-sm col-lg">
              <div class="" v-on:click = "showTowns">
                {{title}}
              </div>
            </div>
          </div>
          <div class="row">
            <div class="col col-sm col-lg">
              <div class="" v-if ="seen">

                <div class="" v-for="item in Towns">
                  <div class="" v-on:click="selectTown(item)">
                    {{item.name}}
                  </div>
                </div>
              </div>
            </div>
          </div>

      </div>
      <div class="col col-sm col-lg">
        <div class="row">
          <div class="col col-sm col-lg">
            Адресс
          </div>
        </div>
        <div class="row">
          <div class="col col-sm col-lg">
            <div class="">
              <input v-model="adress" type="text" name="" value="">
            </div>
          </div>
        </div>
      </div>
    </div>
<!-- map -->
    <div class="row">
      <div class="col col-sm col-lg">

      </div>
    </div>
<!-- searc -->
    <div class="row">
      <div class="col col-sm col-lg">
        <div class="">
          Как найти
        </div>
        <div class="">
          <input v-model="how_search" type="text" name="" value="">
        </div>
        <div class="">
          Как найти внутри здания
        </div>
      </div>
    </div>
    <!-- get -->
    <div class="row">
      <div class="col col-sm">
        <div class="">
          Как проехать
        </div>
        <div class="">
          <input v-model="how_get" type="text" name="" value="">
        </div>
        <div class="">
          Как проехать до нужного здания?
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col col-sm col-lg">
        <div class="">
          Ближайшее метро
        </div>
        <div class="">

          <select v-model="metros" class="" name="" multiple>
            <option v-bind:value="item" v-for="item in listMetro">{{item.name}}</option>
          </select>
        </div>
        <div class="" >
          <div class="">
            Вы выбрали:
          </div>
          <div class="" v-for="item in metros">
            <div class="">
              {{item.name}}
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col col-sm col-lg">
        <div class="">
          <button v-on:click="Save" type="button" name="button">Save</button>
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
      title: "Выберите",
      metros: [],
      town: {},
      adress: "",
      office: "",
      how_search: "",
      how_get: '',
    }
  },
  mounted() {
    this.$store.dispatch('SET_EMPTY_METRO_LIST')
    var master = this.$store.getters.MASTER
    if (master.adress != '')
      this.adress = master.adress
    if (master.office != '')
      this.office = master.office
    if (master.how_search != '')
      this.how_search = master.how_search
    if (master.how_get != '')
      this.how_get = master.how_get
    if (master.town != null) {
      this.$store.dispatch('GET_TOWN', master.town)
      this.title = this.$store.getters.TOWN.name
      this.$store.dispatch('GET_LIST_METRO_BY_TOWN', this.$store.getters.TOWN)
    }


    if (master.metro.length != 0) {
      this.$store.dispatch('SET_EMPTY_METROS')
      for (var i = 0; i < master.metro.length; i++) {
        this.$store.dispatch('GET_METRO', master.metro[i])
      }
      this.metros = this.$store.getters.METROS

    }
  },
  methods: {
    Save: function() {
      var master = this.$store.getters.MASTER
      // изменения
      master.adress = this.adress
      master.town = this.town.id
      master.office = this.office
      master.how_search = this.how_search
      master.how_get = this.how_get

      for (var i = 0; i < this.metros.length; i++) {
        master.metro.push(this.metros[i].id)
      }

      this.$store.dispatch('PUT_MASTER', master)

    },
    selectTown: function(item) {
      this.seen = false
      this.title = item.name
      this.town = item

      this.$store.dispatch('GET_LIST_METRO_BY_TOWN', item)
    },
    showTowns: function() {
      this.seen = !this.seen
    },
  },
  computed: {
    Towns: function() {

      return this.$store.getters.TOWNS
    },
    listMetro: function() {

      return this.$store.getters.METRO_LIST
    }
  }
}
</script>

<style lang="css" scoped>
</style>
