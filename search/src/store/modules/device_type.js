import Axios from 'axios'

var HTTP_PATH = 'http://127.0.0.1:8000/';
const state = {
  device_types_by_affilation: [],
  filter_device_type: {},
  selected_device_type: {},
  bool_device_type: false,
};
const getters = {
  DEVICE_TYPES_BY_AFFILATION: state => {
    return state.device_types_by_affilation
  },
  SELECTED_DEVICE_TYPE: state => {
    return state.selected_device_type
  },
  BOOL_DEVICE_TYPE: state => {
    return state.bool_device_type
  },
  FILTER_DEVICE_TYPE: state => {
    return state.filter_device_type
  },
}
const mutations = {
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
  SET_FILTER_DEVICE_TYPE: (state, data) => {
    state.filter_device_type = data
  },
}
const actions = {

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
  GET_FILTER_DEVICE_TYPE: async (context, name) => {
    let {
      data
    } = await Axios(HTTP_PATH + 'api/device/filter/device_type/' + name)
    context.commit('SET_FILTER_DEVICE_TYPE', data)
  },

}

export default {
  state,
  getters,
  mutations,
  actions,
}