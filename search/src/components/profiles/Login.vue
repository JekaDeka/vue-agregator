<template>
<v-content>
  <v-container fluid fill-height class="login-wrapper">
    <v-layout align-center justify-center>
      <v-flex xs12 sm8 md4>
        <v-card class="elevation-2 wrap-login100" v-if="!token">
          <!-- <v-toolbar dark color="primary">
            <v-toolbar-title>Добро пожаловать</v-toolbar-title>
            <v-spacer></v-spacer>
            <v-tooltip bottom>
              <v-btn icon large :href="source" target="_blank" slot="activator">
              </v-btn>
              <span>Source</span>
            </v-tooltip>
          </v-toolbar> -->
          <v-card-title primary-title>
            <h3 class="headline">Добро пожаловать</h3>
          </v-card-title>
          <v-card-text>
            <v-form @keyup.native.enter="submit">
              <v-text-field prepend-icon="fas fa-user-circle" name="username" label="Логин" type="text" :error-messages="usernameErrors" v-model.trim="$v.username.$model" required></v-text-field>
              <v-text-field prepend-icon="fas fa-lock" name="pass" label="Пароль" id="pass" type="password" :error-messages="passwordErrors" v-model.trim.lazy="$v.pass.$model" required></v-text-field>
            </v-form>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn flat color="primary" @click="submit" type="submit">Войти</v-btn>
          </v-card-actions>
        </v-card>
        <v-card class="elevation-2 wrap-login100" v-else>
          <v-card-title primary-title>
            <p>Вы уже вошли в аккаунт</p>
            <p>Перейти в <router-link :to="{ name: '', params: {} }">Панель управления</router-link> или <router-link :to="{ name: 'logout', params: {} }">выйти</router-link>
            </p>
          </v-card-title>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</v-content>
</template>

<script>
import * as types from '@/store/mutation-types'
import { required, minLength, between } from 'vuelidate/lib/validators'
export default {
  data() {
    return {
      username: '',
      pass: '',
      message: '',
      submitStatus: null,
      drawer: null
    }
  },
  props: {
    source: String
  },
  validations: {
    username: {
      required,
      minLength: minLength(3)
    },
    pass: {
      required,
      minLength: minLength(3)
    }
  },
  computed: {
    token() {
      return this.$store.state.token
    },
    status() {
      return this.$store.getters.status
    },
    usernameErrors() {
      var errors = [];
      if(!this.$v.username.$dirty) return errors;
      !this.$v.username.minLength && errors.push('Логин должен быть не менее 6 символов');
      !this.$v.username.required && errors.push('Обязательное поле');
      return errors;
    },
    passwordErrors() {
      var errors = [];
      if(!this.$v.pass.$dirty) return errors;
      !this.$v.pass.minLength && errors.push('Пароль должен быть не менее 6 символов');
      !this.$v.pass.required && errors.push('Обязательное поле');
      return errors;
    }
  },
  methods: {
    submit() {
      this.$v.$touch()
      if(this.$v.$invalid) {
        this.submitStatus = 'ERROR'
      } else {
        this.$Progress.start()
        this.submitStatus = 'PENDING'
        var credential = {
          username: this.username,
          password: this.pass
        }
        let redirect = decodeURIComponent(this.$route.query.redirect || '/')
        this.$store.dispatch(types.LOGIN, {
          credential: credential,
          redirect: redirect
        })
        this.$Progress.finish()
      }
    }
  }
}
</script>

<style lang="scss" scopped>
.login-wrapper {
    height: 100vh;
}
.v-card {
    padding: 10px 40px;
}
.theme--light.application {
    background: #f2f2f2;
}
.wrap-login100 {
    border-radius: 6px;
}
</style>
