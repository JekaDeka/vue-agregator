import Vue from 'vue'
import Brand from './Brand.vue'
import Mark from './Mark.vue'
import DeviceModel from './DeviceModel.vue'
import {
  store
} from './store';


Vue.config.productionTip = false
new Vue({

  store,
  render: h => h(Brand),

}).$mount('#brands')

new Vue({
  store,
  render: f => f(Mark),
}).$mount('#marks')

new Vue({
  store,
  render: h => h(DeviceModel),
}).$mount('#device_models')