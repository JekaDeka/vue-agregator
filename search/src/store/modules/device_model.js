import Axios from 'axios'

var HTTP_PATH = 'http://127.0.0.1:8000/';
const state = {
  device_models: [],
  selected_device_model: {},
  filter_device_model: [],
  bool_device_model: false,
}
const getters = {
  DEVICE_MODELS: state => {
    return state.device_models
  },
  SELECTED_DEVICE_MODEL: state => {
    return state.selected_device_model
  },
  BOOL_DEVICE_MODEL: state => {

    return state.bool_device_model
  },
  FILTER_DEVICE_MODEL: state => {
    return state.filter_device_model
  },
}
const mutations = {
  SET_DEVICE_MODELS: (state, data) => {

    state.device_models = data
  },

  SELECT_DEVICE_MODEL: (state, data) => {
    state.bool_device_model = true
    state.bool_fault = false
    state.selected_device_model = data
  },
  SET_FILTER_DEVICE_MODEL: (state, data) => {
    state.filter_device_model = data
  },

}
const actions = {
  SELECT_DEVICE_MODEL: async (context, obj) => {
    context.commit('SELECT_DEVICE_MODEL', obj)
  },
  GET_DEVICE_MODEL_BY_BRAND: async (context, list) => {

    let {
      data
    } = await Axios(HTTP_PATH + 'api/device/search/device_model/device_type/brand/' + list[0] + '/' + list[1])
    context.commit('SET_DEVICE_MODELS', data)
  },
  GET_FILTER_DEVICE_MODEL: async (context, name) => {
    let {
      data
    } = await Axios(HTTP_PATH + 'api/device/filter/device_model/' + name)
    context.commit('SET_FILTER_DEVICE_MODEL', data)
  },
}

export default {
  state,
  getters,
  mutations,
  actions,
}