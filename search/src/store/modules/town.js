import Axios from 'axios'

var HTTP_PATH = 'http://127.0.0.1:8000/';

const state = {
  towns: [],
  town: {},
}
const getters = {
  TOWNS: state => {
    return state.towns
  },
  TOWN: state => {
    return state.town
  }
}
const mutations = {
  SET_TOWNS: (state, data) => {
    state.towns = data
  },
  SET_TOWN: (state, data) => {
    state.town = data
  }
}
const actions = {
  GET_TONWS_BY_COUNTRY_NAME: async (context, name) => {
    let {
      data
    } = await Axios.get(HTTP_PATH + 'api/metro/filter/town_by_coutnry_name/' + name)
    context.commit('SET_TOWNS', data)
  },
  GET_TOWN: async (context, id) => {
    let {
      data
    } = await Axios.get(HTTP_PATH + 'api/metro/town/' + id + '/')

    context.commit("SET_TOWN", data)
  }
}

export default {
  state,
  getters,
  mutations,
  actions,
}