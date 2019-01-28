import Vue from 'vue';
import Vuex from 'vuex';
import Axios from 'axios';

var HTTP_PATH = 'http://127.0.0.1:8000/';

Vue.use(Vuex)


export const store = new Vuex.Store({
  state: {
    device_types_by_affilation: [],
    selected_device_type: {},
    bool_device_type: false,

    brands: [],
    selected_brand: {},
    bool_brand: false,

    device_models: [],
    selected_device_model: {},
    bool_device_model: false,
    faults_by_spare_part: [],
    selected_fault: {},
    bool_fault: false,

    breakage_actions: [],

  },
  getters: {
    DEVICE_TYPES_BY_AFFILATION: state => {
      return state.device_types_by_affilation
    },
    SELECTED_DEVICE_TYPE: state => {
      return state.selected_device_type
    },
    BOOL_DEVICE_TYPE: state => {
      return state.bool_device_type
    },
    BRANDS: state => {
      return state.brands
    },
    SELECTED_BRAND: state => {
      return state.selected_brand
    },
    BOOL_BRAND: state => {
      return state.bool_brand
    },
    DEVICE_MODELS: state => {
      return state.device_models
    },
    SELECTED_DEVICE_MODEL: state => {
      return state.selected_device_model
    },
    BOOL_DEVICE_MODEL: state => {
      console.log(state.bool_device_model)
      return state.bool_device_model
    },
    FAULTS_BY_SPARE_PART: state => {
      return state.faults_by_spare_part
    },
    SELETED_FAULT: state => {
      return state.selected_fault
    },
    BOOL_FAULT: state => {
      return state.bool_fault
    },
    BREAKAGE_ACTIONS: state => {
      return state.breakage_actions
    }


  },
  mutations: {
    SET_DEVICE_TYPES_BY_AFFILATION: (state, data) => {

      state.device_types_by_affilation = data
    },
    SELECT_DEVICE_TYPE: (state, data) => {
      state.bool_brand = false
      state.bool_device_model = false
      state.bool_fault = false
      state.bool_device_type = true
      state.selected_device_type = data
    },
    SET_BRANDS: (state, data) => {
      state.brands = data
    },
    SELECT_BRAND: (state, data) => {
      state.bool_device_model = false
      state.bool_fault = false
      state.bool_brand = true
      state.selected_brand = data
    },
    SET_DEVICE_MODELS: (state, data) => {
      state.device_models = data
    },
    SELECT_DEVICE_MODEL: (state, data) => {
      state.bool_device_model = true
      state.bool_fault = false
      state.selected_device_model = data
    },
    SET_FAULTS_BY_SPARE_PART: (state, data) => {
      state.faults_by_spare_part = data
    },
    SELECT_FAULT: (state, data) => {
      state.bool_fault = true
      state.selected_fault = data
    },
    SET_BREAKAGE_ACTIONS: (state, data) => {
      state.breakage_actions = data
    }
  },

  actions: {
    GET_DEVICE_TYPES_BY_AFFILATION: async (context) => {
      let {
        data
      } = await Axios.get(HTTP_PATH + 'api/device/device_affiliation/')

      var result = []
      for (var i = 0; i < data.length; i++) {
        var device_types = await Axios.get(HTTP_PATH + 'api/device/search/device_type/device_affiliation/' + data[i].id)

        var affilation = {}
        affilation.aff = data[i]
        affilation.device_types = device_types.data
        result.push(affilation)
      }
      context.commit('SET_DEVICE_TYPES_BY_AFFILATION', result)
    },
    SELECT_DEVICE_TYPE: async (context, obj) => {
      context.commit('SELECT_DEVICE_TYPE', obj)
    },
    GET_BRAND_BY_DEVICE_TYPE: async (context, device_type) => {
      let {
        data
      } = await Axios(HTTP_PATH + 'api/device/search/brand/device_type/' + device_type.id)
      context.commit('SET_BRANDS', data)
      return data
    },
    SELECT_BRAND: async (context, brand) => {
      context.commit('SELECT_BRAND', brand)
    },
    SELECT_DEVICE_MODEL: async (context, obj) => {
      context.commit('SELECT_DEVICE_MODEL', obj)
    },
    GET_DEVICE_MODEL_BY_BRAND: async (context, list) => {

      let {
        data
      } = await Axios(HTTP_PATH + 'api/device/search/device_model/device_type/brand/' + list[0] + '/' + list[1])
      context.commit('SET_DEVICE_MODELS', data)
    },
    GET_FAULTS_BY_SPARE_PART: async (context, obj) => {
      let {
        data
      } = await Axios.get(HTTP_PATH + 'api/device/search/spare_part/device_model/' + obj.id)

      var result = []
      for (var i = 0; i < data.length; i++) {
        var faults = await Axios.get(HTTP_PATH + 'api/manufacture_service/search/spare_part/device_model/' + data[i].id)

        var dict = {}
        dict.spare_part = data[i]
        dict.faults = faults.data
        result.push(dict)
      }
      context.commit('SET_FAULTS_BY_SPARE_PART', result)
    },
    GET_BREAKAGE_ACTIONS_BY_FAULTS: async (context, obj) => {
      let {
        data
      } = await Axios(HTTP_PATH + 'api/manufacture_service/search/breakage_action/fault/' + obj.id)
      context.commit('SET_BREAKAGE_ACTIONS', data)
    }
  },

})