<template>
<div class="">
  <div class="container" id="register">
    <div class="row">
      <div class="col col-sm col-lg">
        <div class="">
          Войдите
        </div>
      </div>
      <div class="col col-sm col-lg">
        <div class="">
          <button v-on:click="GoRegister" type="button" name="button">Регистрация</button>
        </div>
      </div>
    </div>
    <div class="row" v-if="seen==0">
      <div class="col col-sm col-lg">
        <div class="">
          <button v-on:click="selectRegister(1)" type="button" name="button">Я сервис</button>
        </div>
      </div>
      <div class="col col-sm col-lg">
        <div class="">
          <button v-on:click="selectRegister(2)" type="button" name="button">Я мастер</button>
        </div>
      </div>
    </div>
    <div class="row" v-if="seen==1">
      <div class="col col-sm col-lg">
        <TheRegisterManufacture></TheRegisterManufacture>
      </div>
    </div>
    <div class="row" v-if="seen==2">
      <div class="col col-sm col-lg">
        <TheRegisterMaster></TheRegisterMaster>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import TheRegisterManufacture from '@/components/login/Manufacture';
import TheRegisterMaster from '@/components/login/Master'

export default {
  components: {
    TheRegisterManufacture,
    TheRegisterMaster,
  },
  data: function() {
    return {
      seen: 0,
    }
  },
  methods: {
    selectRegister: function(number) {
      this.seen = number
    },
    GoRegister: function() {
      var url = window.location.pathname
      var list = url.split('/')
      window.location.pathname = list[1] + '/' + 'register/new_login/'
    }
  },
}
</script>

<style lang="css" scoped>
</style>
