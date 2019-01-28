import Vue from 'vue'
import Register from './Register.vue'
import {
  store
} from './store'
import * as backendAPI from './common/backendAPI'
import Register from './Register.vue'


Vue.prototype.$api = backendAPI
Vue.config.productionTip = false

new Vue({

  store,
  render: h => h(Register),

}).$mount('#register')