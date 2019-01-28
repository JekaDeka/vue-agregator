import Vue from 'vue';
import Vuex from 'vuex';
import Axios from 'axios';

var HTTP_PATH = 'http://127.0.0.1:8000/';

Vue.use(Vuex)


export const store = new Vuex.Store({
  state: {
    brands: [],
    marks: [],
    device_models: [],
  },
  getters: {
    BRANDS: state => {
      return state.brands
    },
    MARKS: state => {
      return state.marks
    },
    DEVICE_MODELS: state => {
      return state.device_models
    },
  },
  mutations: {
    SET_BRANDS: (state, data) => {

      state.brands = data

    },
    SET_MARKS: (state, data) => {
      state.marks = data
    },
    SET_DEVICE_MODELS: (state, data) => {
      state.device_models = data
    }
  },

  actions: {
    GET_BREAKAGE_ACTIONS_BY_FAULTS: async (context, obj) => {
      let {
        data
      } = await Axios(HTTP_PATH + 'api/manufacture_service/search/breakage_action/fault/' + obj.id)
      context.commit('SET_BREAKAGE_ACTIONS', data)
    },
    GET_BRANDS: async (context) => {
      let {
        data
      } = await Axios(HTTP_PATH + 'api/device/brand/')
      context.commit('SET_BRANDS', data)
    },
    GET_MARKS: async (context) => {
      let {
        data
      } = await Axios(HTTP_PATH + 'api/device/mark/')
      context.commit('SET_MARKS', data)
    },
    GET_DEVICE_MODELS: async (context) => {
      let {
        data
      } = await Axios(HTTP_PATH + 'api/device/device_model/')
      context.commit('SET_DEVICE_MODELS', data)
    },
  },

})