import Axios from 'axios'

var HTTP_PATH = 'http://127.0.0.1:8000/';

const state = {
  faults_by_spare_part: [],
  filter_fault: [],
  selected_fault: {},
  bool_fault: false,
}
const getters = {
  FAULTS_BY_SPARE_PART: state => {
    return state.faults_by_spare_part
  },
  SELETED_FAULT: state => {
    return state.selected_fault
  },
  BOOL_FAULT: state => {
    return state.bool_fault
  },
  FILTER_FAULT: state => {
    return state.filter_fault
  },

}
const mutations = {
  SET_FAULTS_BY_SPARE_PART: (state, data) => {
    state.faults_by_spare_part = data
  },
  SELECT_FAULT: (state, data) => {

    state.bool_fault = true
    state.selected_fault = data

  },
  SET_FILTER_FAULT: (state, data) => {
    state.filter_fault = data
  },

}
const actions = {
  GET_FAULTS_BY_SPARE_PART: async (context, obj) => {
    let {
      data
    } = await Axios.get(HTTP_PATH + 'api/device/search/spare_part/device_model/' + obj.id)

    var result = []
    for (var i = 0; i < data.length; i++) {

      var faults = await Axios.get(HTTP_PATH + 'api/manufacture_service/search/fault/spare_part/' + data[i].id)

      var dict = {}
      dict.spare_part = data[i]
      dict.faults = faults.data
      result.push(dict)
    }
    context.commit('SET_FAULTS_BY_SPARE_PART', result)
  },
  SELECT_FAULT: async (context, obj) => {
    context.commit('SELECT_FAULT', obj)
  },
  GET_FILTER_FAULT: async (context, name) => {
    let {
      data
    } = await Axios(HTTP_PATH + 'api/manufacture_service/filter/fault/' + name)
    context.commit('SET_FILTER_FAULT', data)
  },
}

export default {
  state,
  getters,
  mutations,
  actions,
}