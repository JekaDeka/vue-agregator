import Vue from 'vue';
import Vuex from 'vuex';
import Axios from 'axios';
import createPersistedState from 'vuex-persistedstate'

import Number from './modules/number'
import Manufacture from './modules/manufacture'
import Master from './modules/master'
import Login from './modules/login'
import DeviceType from './modules/device_type'
import Brand from './modules/brand'
import DeviceModel from './modules/device_model'
import Fault from './modules/fault'
import BreakageAction from './modules/breakage_action'
import Metro from './modules/metro'
import Proposal from './modules/proposal'
import Town from './modules/town'
import ManufactureService from './modules/manufacture_service'

var HTTP_PATH = 'http://127.0.0.1:8000/';

Vue.use(Vuex)


export const store = new Vuex.Store({
  state: {},
  getters: {},
  mutations: {},
  actions: {},
  plugins: [
    createPersistedState()
  ],
  modules: {
    ManufactureService,
    BreakageAction,
    Proposal,
    Town,
    Metro,
    Fault,
    Brand,
    DeviceModel,
    DeviceType,
    Login,
    Manufacture,
    Master,
    Number,
  }

})