import Axios from 'axios';

var HTTP_PATH = 'http://127.0.0.1:8000/';
const state = {
  metros: [],
  metro_list: [],
  filter_metro: [],
  selected_metro: {},
  bool_metro: false,
}
const getters = {
  METROS: state => {
    return state.metros
  },
  METRO_LIST: state => {
    return state.metro_list
  },
  SELECTED_METRO: state => {
    return state.selected_metro
  },
  BOOL_METRO: state => {
    return state.bool_metro
  },
  FILTER_METRO: state => {
    return state.filter_metro
  }
}
const mutations = {
  SET_EMPTY_METROS: (state) => {
    state.metros = []

  },
  SET_EMPTY_METRO_LIST: (state) => {
    state.metro_list = []
  },
  SET_METROS: (state, data) => {
    state.metros.push(data)
  },
  SET_METRO_LIST: (state, data) => {
    state.metro_list = data
  },
  SELECT_METRO: (state, data) => {
    state.bool_metro = true
    state.selected_metro = data
  },


  SET_FILTER_METRO: (state, data) => {
    state.filter_metro = data
  },
}
const actions = {
  SET_EMPTY_METROS: (context) => {
    context.commit('SET_EMPTY_METROS')
  },
  SET_EMPTY_METRO_LIST: (context) => {
    context.commit('SET_EMPTY_METRO_LIST')
  },
  GET_METRO: async (context, id) => {
    let {
      data
    } = await Axios.get(HTTP_PATH + 'api/metro/metro/' + id + '/')
    context.commit("SET_METROS", data)
  },
  GET_METRO_LIST: async (context, town) => {
    let {
      data
    } = await Axios(HTTP_PATH + 'api/metro/search/metro_by_town_name/' + town)
    context.commit('SET_METRO_LIST', data)
  },
  GET_LIST_METRO_BY_TOWN: async (context, obj) => {
    let {
      data
    } = await Axios.get(HTTP_PATH + 'api/metro/search/metro_by_town/' + obj.id)

    context.commit('SET_METRO_LIST', data)
  },

  SELECT_METRO: async (context, obj) => {
    context.commit('SELECT_METRO', obj)
  },
  GET_FILTER_METRO: async (context, name) => {
    let {
      data
    } = await Axios(HTTP_PATH + 'api/metro/filter/metro/' + name)
    context.commit('SET_FILTER_METRO', data)
  },
}

export default {
  state,
  getters,
  mutations,
  actions,
}