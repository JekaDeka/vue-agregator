import Vue from 'vue';
import Vuex from 'vuex';
import Axios from 'axios';

var HTTP_PATH = 'http://127.0.0.1:8000/';

Vue.use(Vuex)


export const store = new Vuex.Store({
  state: {
    countryes: [],
    selected_country: {},
    bool_country: false,

    manufacture: {},
    master: {},

    bool_login: true,
  },
  getters: {
    BOOL_LOGIN: state => {
      return state.bool_login
    },
    COUNTRYES: state => {
      return state.countryes
    },
    SELECTED_COUNTRY: state => {
      return state.selected_country
    },
    BOOL_COUNTRY: state => {
      return state.bool_country
    },
    MANUFACTURE: state => {
      return state.manufacture
    },
    MASTER: state => {
      return state.master
    },
  },
  mutations: {
    SET_BOOL_LOGIN: (state, data) => {
      if (data.length == 0) {
        state.bool_login = true
      } else {
        state.bool_login = false
      }
    },
    SET_COUNTRYES: (state, data) => {
      state.countryes = data
    },
    SELECT_COUNTRY: (state, data) => {
      state.bool_country = false
      state.selected_country = data
    },
    SET_MANUFACTURE: (state, data) => {
      state.manufacture = data
    },
    SET_MASTER: (state, data) => {
      state.master = data
    },

  },

  actions: {
    GET_FILTER_MANUFACTURE_BY_LOGIN: async (context, login) => {
      let {
        data
      } = await Axios(HTTP_PATH + 'api/manufacture/filter/manufacture_by_login/' + login)
      context.commit('SET_BOOL_LOGIN', data)
    },
    GET_FILTER_MASTER_BY_LOGIN: async (context, login) => {
      let {
        data
      } = await Axios(HTTP_PATH + 'api/manufacture/filter/master_by_login/' + login)
      context.commit('SET_BOOL_LOGIN', data)
    },
    POST_MANUFACTURE: async (context, obj) => {
      let {
        data
      } = await Axios.post(HTTP_PATH + 'api/manufacture/manufacture/', obj)
      context.commit('SET_MANUFACTURE', data)
    },
    POST_MASTER: async (context, obj) => {
      let {
        data
      } = await Axios.post(HTTP_PATH + 'api/manufacture/master/', obj)

      context.commit('SET_MASTER', data)
    },
    GET_COUNTRYES: async (context) => {
      let {
        data
      } = await Axios(HTTP_PATH + 'api/metro/country/')

      context.commit('SET_COUNTRYES', data)
    },
    SELECT_COUNTRY: async (context, obj) => {
      context.commit('SELECT_COUNTRY', obj)
    },
  },
})