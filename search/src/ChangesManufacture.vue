<template lang="html">
  <div class="" id ="changes">

    <div class="cotainer">
      <div class="row">
      <div class="col-3 col-sm-3 col-lg-3">

          <div class="row">
            <div class="col col-sm col-lg">
              <div class="" v-on:click = "selectChanges(1)">
                Адресс
              </div>
            </div>
          </div>
          <div class="row">
            <div class="col col-sm col-lg">
              <div class="" v-on:click="selectChanges(2)">
                Контактная информация
              </div>
            </div>
          </div>
          <div class="row">
            <div class="col col-sm col-lg">
              <div class="" v-on:click="selectChanges(3)">
                Услуги
              </div>
              </div>
            </div>
            <div class="row">
              <div class="col col-sm col-lg">
                <div class="" v-on:click="selectChanges(4)">
                  Заявки
                </div>
                </div>
            </div>
            <div class="row">
              <div class="col col-sm col-lg">
                <div class="" v-on:click="selectChanges(5)">
                  Удалить
                </div>
                </div>
              </div>

      </div>
      <div class="col col-sm col-lg">
          <div class="" v-if='changes_select ==1'>
            <TheAdress></TheAdress>
          </div>
          <div class="" v-if="changes_select ==2">
            <TheContactInformation></TheContactInformation>
          </div>
          <div class="" v-if="changes_select ==3">
            <TheManufactureService></TheManufactureService>
          </div>
          <div class="" v-if="changes_select ==4">
            <TheProposal></TheProposal>
          </div>
          <div class="" v-if = "changes_select==5">
            <TheDelete></TheDelete>
          </div>
      </div>
    </div>

    </div>
  </div>
</template>

<script>
import TheAdress from '@/components/manufacture/Adress.vue'
import TheContactInformation from '@/components/manufacture/ContactInformation'
import TheManufactureService from '@/components/manufacture/ManufactureService'
import TheProposal from '@/components/manufacture/Proposal'
import TheDelete from '@/components/manufacture/Delete.vue'
export default {
  data: function() {
    el: "#changes"
    return {
      changes_select: 1,
    }
  },
  methods: {
    selectChanges: function(index) {
      this.changes_select = index
    },
  },
  mounted: function() {
    var url = window.location.pathname
    var list = url.split('/')
    var id = list[list.length - 2]
    if (isFinite(id)) {
      this.$store.dispatch('GET_MANUFACTURE', id)
      this.$store.dispatch('GET_TONWS_BY_COUNTRY_NAME', list[1])
      this.$store.dispatch('GET_NUMBERS_BY_MANUFACTURE', id)
    }
  },
  components: {
    TheAdress,
    TheContactInformation,
    TheManufactureService,
    TheDelete,
    TheProposal,
  },
}
</script>

<style lang="css" scoped>
</style>
