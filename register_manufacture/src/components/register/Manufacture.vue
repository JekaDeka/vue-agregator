<template lang="html">
  <div class="">
    <div class="container">
      <div class="row">
        <div class="col col-sm col-lg">
          <div class="">
            Название
          </div>
        </div>
        <div class ="col col-sm col-lg">
          <div class="">
            <input  v-model="name" type="text" name="" value="">
          </div>
        </div>
      </div>

      <div class="row">
        <div class="col col-sm col-lg">
          <div class="">
            Логин
          </div>
        </div>
        <div class="col col-sm col-lg">
          <input v-model="login" type="text" name="" value="">
        </div>
      </div>
      <div class="row">
        <div class="col col-sm col-lg">
          Пароль
        </div>
        <div class="col col-sm col-lg">
          <div class="">
            <input v-model = "password" type="password" name="" value="">
          </div>
        </div>
      </div>
      <div class="row" v-if = "boolRegister">
        <div class="col col-sm col-lg">
          <a href="#" v-on:click = "register">Регистрация</a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data: function() {
    return {
      name: "",
      link: '',
      email: '',
      number: '',
      login: "",
      password: '',
      error: false,

      new_manufacture: {
        "login": "",
        "passsword": "",
        "name": "",
        "content": "",
        "adress": "",
        "how_search": "",
        "how_get": "",
        "work_clock_weekdays_start": null,
        "work_clock_weekdays_end": null,
        "work_clock_saturday_start": null,
        "work_clock_saturday_end": null,
        "work_clock_suday_start": null,
        "work_clock_sunday_end": null,
        "pay_card": false,
        "courier": false,
        "comment_courier": "",
        "diagnostic": false,
        "comment_diagnostic": "",
        "master_home": false,
        "master_home_comment": "",
        "urgent_repairs": false,
        "link": "",
        "country": null,
        "town": null,
        "number": null,
        "metro": []
      },
    }
  },
  methods: {
    register: function() {
      if (this.name != "" && this.login != "" && this.password != '' && this.$store.getters.BOOL_LOGIN) {
        this.new_manufacture.name = this.name
        this.new_manufacture.login = this.login
        this.new_manufacture.password = this.password
        this.$store.dispatch('POST_MANUFACTURE', this.new_manufacture)
      }
    },
  },
  computed: {
    boolRegister() {
      if (this.name != "" && this.link != '' && this.email != '' && this.number != '' && this.login != "" && this.password != '' && this.$store.getters.BOOL_LOGIN) {
        return true
      } else
        return false
    },
    errorMessage() {
      if (this.login != '')
        this.$store.dispatch("GET_FILTER_MANUFACTURE_BY_LOGIN", this.login)

      if (this.$store.getters.BOOL_LOGIN) {
        return ''
      } else return 'Вы ввели уже существующий логин'

    }
  }
}
</script>

<style lang="css" scoped>
</style>
