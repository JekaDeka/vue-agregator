<template lang="html">
  <div class="">
    <div class="container">
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
      <div class="row" v-if="seen_empty">
        <div class="col col-sm col-lg">
          <div class="">
                Заполните все поля
          </div>

        </div>
      </div>
      <div class="row" v-if ="seen_error">
        <div class="col col-sm col-lg">
          <div class="">
            Вы ввели не правильный логин
          </div>
        </div>
      </div>
      <div class="row">
        <div class="col col-sm col-lg">
          <div class="">
              <button v-on:click = "register" type="button" name="button">Вход</button>
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
      login: "",
      password: '',
      seen_empty: false,
      seen_error: false,

    }
  },
  methods: {
    register: function() {
      if (this.login != "" && this.password != '') {
        this.$store.dispatch('GET_MASTER_BY_LOGIN_PASSWORD', [this.login, this.password])
        console.log('next')
        if (this.$store.getters.MASTER.length != 0) {
          var url = window.location.pathname
          var list = url.split('/')
          window.location.pathname = list[1] + '/' + 'register/master/' + this.$store.getters.MASTER[0].id + '/'
        } else {
          this.seen_error = true
        }
      } else
        this.seen_empty = true
    },
  },
}
</script>

<style lang="css" scoped>
</style>
