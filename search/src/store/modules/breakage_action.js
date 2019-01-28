import Axios from 'axios';
var HTTP_PATH = 'http://127.0.0.1:8000/';

const state = {
  breakage_actions: [],
  breakage_actions_with_mark: [],
};
const getters = {
  BREAKAGE_ACTIONS: state => {
    return state.breakage_actions
  },
  BREAKAGE_ACTIONS_WITH_MARK: state => {
    return state.breakage_actions_with_mark
  },
};

const mutations = {
  SET_BREAKAGE_ACTIONS: (state, data) => {
    state.breakage_actions = data
  },
  SET_BREAKAGE_ACTIONS_WITH_MARK: (state, data) => {
    state.breakage_actions_with_mark = data
  },
  SET_EMPTY_BREAKAGE_ACTIONS_WITH_MARK: state => {
    state.breakage_actions_with_mark = []
  }
};
const actions = {
  GET_BREAKAGE_ACTIONS_BY_FAULT: async (context, obj) => {
    let {
      data
    } = await Axios(HTTP_PATH + 'api/manufacture_service/search/breakage_action/fault/' + obj.id)
    context.commit('SET_BREAKAGE_ACTIONS', data)
  },
  GET_BRAKAGE_ACTIONS_BY_BRAND: async (context, brand) => {

    var data = []

    var mark = await Axios.get(HTTP_PATH + 'api/device/filter/marks_by_brand/' + brand.id)


    for (var i = 0; i < mark.data.length; i++) {
      var breakage_action = {}
      var br = await Axios.get(HTTP_PATH + 'api/manufacture_service/filter/breakage_actions_by_mark/' + mark.data[i].id)
      breakage_action.mark = mark.data[i]
      breakage_action.breakage_actions = br.data
      data.push(breakage_action)
    }
    context.commit('SET_BREAKAGE_ACTIONS_WITH_MARK', data)
  },
  SET_EMPTY_BREAKAGE_ACTIONS_WITH_MARK: async (context) => {
    context.commit("SET_EMPTY_BREAKAGE_ACTIONS_WITH_MARK")
  }
};

export default {
  state,
  getters,
  mutations,
  actions,
}