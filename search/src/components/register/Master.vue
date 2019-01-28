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
          {{errorMessage}}
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
          <div class="">
              <button  v-on:click = "register" type="button" name="button">Регистрация</button>
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
      name: "",
      link: '',
      email: '',
      number: '',
      login: "",
      password: '',
      error: false,

      new_master: {
        login: "",
        passsword: "",
        name: "",
        content: "",
        adress: "",
        how_search: "",
        how_get: "",
        work_clock_weekdays_start: null,
        work_clock_weekdays_end: null,
        work_clock_saturday_start: null,
        work_clock_saturday_end: null,
        work_clock_suday_start: null,
        work_clock_sunday_end: null,
        pay_card: false,
        courier: false,
        comment_courier: "",
        diagnostic: false,
        comment_diagnostic: "",
        master_home: false,
        master_home_comment: "",
        urgent_repairs: false,
        is_private: false,
        country: null,
        town: null,
        number: null,
        manufacture: null,
        metro: []
      }
    }
  },
  methods: {
    register: function() {
      if (this.name != "" && this.login != "" && this.password != '' && this.$store.getters.BOOL_LOGIN) {
        this.new_master.name = this.name
        this.new_master.login = this.login
        this.new_master.password = this.password
        this.$store.dispatch('POST_MASTER', this.new_master)
        var url = window.location.pathname
        var list = url.split('/')
        window.location.pathname = list[1] + '/' + 'register/master/' + this.$store.getters.MASTER.id + '/'
      }
    },
  },
  computed: {
    boolRegister() {
      if (this.name != '' && this.login != "" && this.password != '' && this.$store.getters.BOOL_LOGIN) {
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
