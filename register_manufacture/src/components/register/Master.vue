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
            email
          </div>
        </div>
        <div class="col col-sm col-lg">
          <div class="">
            <input v-model="email" type="text" name="" value="">
          </div>
        </div>
      </div>
      <div class="row">
        <div class="col col-sm col-lg">
          <div class="">
            Номер
          </div>
        </div>
        <div class="col col-sm col-lg">
          <div class="">
            <input v-model="number" type="text" name="" value="">
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
    </div>
  </div>
</template>

<script>
export default {
  data: function() {
    return {
      name: "",
      email: '',
      number: '',
      login: "",
      password: '',
    }
  }
}
</script>

<style lang="css" scoped>
</style>
