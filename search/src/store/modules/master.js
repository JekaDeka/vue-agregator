import Axios from 'axios';

var HTTP_PATH = 'http://127.0.0.1:8000/';

const state = {
  master: {},
};

const getters = {
  MASTER: state => {
    return state.master
  },

};

const mutations = {
  SET_MASTER: (state, data) => {
    state.master = data
  },
  SET_MASTER_BY_LOGIN_PASSWORD: (state, data) => {
    state.master = data
  }
};
const actions = {
  PUT_MASTER: async (context, obj) => {
    let {
      data
    } = await Axios.put(HTTP_PATH + 'api/manufacture/master/' + obj.id + '/', obj)
    context.commit('SET_MASTER', data)
  },
  GET_MASTER_BY_LOGIN_PASSWORD: async (context, list) => {
    let {
      data
    } = await Axios.get(HTTP_PATH + 'api/manufacture/filter/master_by_login_password/' + list[0] + '/' + list[1])
    context.commit('SET_MASTER_BY_LOGIN_PASSWORD', data)
  },
  GET_MASTER: async (context, id) => {
    let {
      data
    } = await Axios.get(HTTP_PATH + 'api/manufacture/master/' + id + '/')
    context.commit('SET_MASTER', data)
  },
  POST_MASTER: async (context, obj) => {
    let {
      data
    } = await Axios.post(HTTP_PATH + 'api/manufacture/master/', obj)

    context.commit('SET_MASTER', data)
  },
  DELETE_MASTER: async (context, obj) => {
    let {
      data
    } = await Axios.delete(HTTP_PATH + 'api/manufacture/master/' + obj.id + '/', obj)

    context.commit('SET_MASTER', data)
  },

}
export default {
  state,
  getters,
  mutations,
  actions,
}