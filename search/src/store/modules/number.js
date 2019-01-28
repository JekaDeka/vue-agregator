import Axios from 'axios';
var HTTP_PATH = 'http://127.0.0.1:8000/';

const state = {
  numbers: [],
  number: {},
  numbers_by_manufacture: [],
  numbers_by_master: [],
};

const getters = {
  NUMBERS: state => {
    return state.numbers
  },
  NUMBER: state => {
    return state.number
  },
  NUMBERS_BY_MANUFACTURE: state => {
    return state.numbers_by_manufacture
  },
  NUMBERS_BY_MASTER: state => {
    return state.numbers_by_master
  }
};

const mutations = {
  SET_NUMBER: (state, data) => {
    state.number
  },
  SET_NUMBERS: (state, data) => {
    state.numbers = data
  },
  SET_NUMBERS_BY_MANUFACTURE: (state, data) => {
    state.numbers_by_manufacture = data
  },
  SET_NUMBERS_BY_MASTER: (state, data) => {
    state.numbers_by_master = data
  },

};
const actions = {
  GET_NUMBERS: async (context) => {
    let {
      data
    } = await Axios.get(HTTP_PATH + 'api/manufacture/numbers/')
  },
  PUT_NUMBER: async (context, obj) => {
    let {
      data
    } = await Axios.put(HTTP_PATH + 'api/manufacture/numbers/' + obj.id + '/', obj)
    context.commit("SET_NUMBER", data)
  },
  GET_NUMBERS_BY_MANUFACTURE: async (context, id) => {
    let {
      data
    } = await Axios.get(HTTP_PATH + 'api/manufacture/filter/numbers_by_manufacture/' + id)
    context.commit('SET_NUMBERS_BY_MANUFACTURE', data)
  },
  GET_NUMBERS_BY_MASTER: async (context, id) => {
    let {
      data
    } = await Axios.get(HTTP_PATH + 'api/manufacture/filter/numbers_by_master/' + id)
    context.commit('SET_NUMBERS_BY_MASTER', data)
  },
  POST_NUMBER: async (context, obj) => {
    let {
      data
    } = await Axios.post(HTTP_PATH + 'api/manufacture/numbers/', obj)
    context.commit('SET_NUMBER', obj)
  },
  DELETE_NUMBER: async (context, obj) => {
    let {
      data
    } = await Axios.delete(HTTP_PATH + 'api/manufacture/numbers/' + obj.id + '/', obj)
  },

}
export default {
  state,
  getters,
  mutations,
  actions,
}