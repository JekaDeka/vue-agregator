import Axios from 'axios'

var HTTP_PATH = 'http://127.0.0.1:8000/';

const state = {
  proposal: {},
  proposal_metro_list: [],
}
const getters = {
  PROPOSAL_METRO_LIST: state => {
    return state.proposal_metro_list
  },
}
const mutations = {
  SET_PROPOSAL: (state, data) => {
    state.proposal = data
  },
  SET_PROPOSAL_METRO_LIST: (state, data) => {
    state.proposal_metro_list = data
  }
}
const actions = {
  POST_PROPOSAL: async (context, obj) => {
    let {
      data
    } = await Axios.post(HTTP_PATH + 'api/proposal/proposal/', obj)
    context.commit('SET_PROPOSAL', data)
  },
  GET_PROPOSAL_BY_METRO: async (context, obj) => {
    var data = []

    for (var i = 0; i < obj.metro.length; i++) {

      var metro = await Axios.get(HTTP_PATH + 'api/metro/metro/' + obj.metro[i] + '/')
      var proposals = await Axios.get(HTTP_PATH + 'api/proposal/filter/proposals_by_metro/' + metro.data.id)
      var t = {}
      t.metro = metro.data
      t.proposals = proposals.data
      data.push(t)

    }

    context.commit('SET_PROPOSAL_METRO_LIST', data)
  }
}

export default {
  state,
  getters,
  mutations,
  actions,
}