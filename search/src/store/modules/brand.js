import Axios from 'axios';
var HTTP_PATH = 'http://127.0.0.1:8000/';
const state = {
  brands: [],
  filter_brand: [],
  selected_brand: {},
  bool_brand: false,
}
const getters = {
  BRANDS: state => {
    return state.brands
  },
  SELECTED_BRAND: state => {
    return state.selected_brand
  },
  BOOL_BRAND: state => {
    return state.bool_brand
  },
  FILTER_BRAND: state => {
    return state.filter_brand
  },
}
const mutations = {
  SET_BRANDS: (state, data) => {
    state.brands = data
  },
  SELECT_BRAND: (state, data) => {
    state.bool_device_model = false
    state.bool_fault = false
    state.bool_brand = true
    state.selected_brand = data
  },
  SET_FILTER_BRAND: (state, data) => {
    state.filter_brand = data
  },
}
const actions = {
  GET_BRANDS: async (context) => {
    let {
      data
    } = await Axios(HTTP_PATH + 'api/device/brand/')
    context.commit('SET_BRANDS', data)
    return data
  },
  SELECT_BRAND: async (context, brand) => {
    context.commit('SELECT_BRAND', brand)
  },
  GET_BRAND_FILTER: async (context, name) => {
    let {
      data
    } = await Axios(HTTP_PATH + 'api/device/filter/brand/' + name)
    context.commit('SET_FILTER_BRAND', data)
  },
}

export default {
  state,
  getters,
  mutations,
  actions,
}