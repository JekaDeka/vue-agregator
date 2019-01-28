import Vue from 'vue'
import StepSearch from './StepSearch.vue'
import FilterSearch from './FilterSearch.vue'
import Proposal from './Proposal.vue'
import ChangesManufacture from './ChangesManufacture'
import Login from './Login.vue'
import ChangesMaster from './ChangesMaster'
// import router from './router'
import {
  store
} from './store/index.js'
import * as backendAPI from './common/backendAPI'

import Register from './Register.vue'

Vue.prototype.$api = backendAPI


Vue.config.productionTip = false

var app1 = new Vue({
  el: "#step_search",
  store,
  render: h => h(StepSearch),

})

var app2 = new Vue({
  el: '#filter_search',
  store,
  render: h => h(FilterSearch)
})

var app3 = new Vue({
  el: '#proposal',
  store,
  render: h => h(Proposal)
}).$mount('#proposal')

var app4 = new Vue({
  el: "#register",
  store,
  render: h => h(Register),

})

var app5 = new Vue({
  el: '#changes_manufacture',
  store,
  render: h => h(ChangesManufacture)
})

var app6 = new Vue({
  el: '#changes_master',
  store,
  render: h => h(ChangesMaster)
})

var app7 = new Vue({
  el: '#login',
  store,
  render: h => h(Login)

})