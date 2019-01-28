import Axios from 'axios';

var HTTP_PATH = 'http://127.0.0.1:8000/';

const state = {
  manufacture: {},
};

const getters = {
  MANUFACTURE: state => {
    return state.manufacture
  },

};

const mutations = {
  SET_MANUFACTURE: (state, data) => {
    state.manufacture = data
  },
  SET_MANUFACTURE_BY_LOGIN_PASSWORD: (state, data) => {

    state.manufacture = data

  }
};
const actions = {
  GET_MANUFACTURE_BY_LOGIN_PASSWORD: async (context, list) => {
    let {
      data
    } = await Axios.get(HTTP_PATH + 'api/manufacture/filter/manufacture_by_login_password/' + list[0] + '/' + list[1])
    context.commit('SET_MANUFACTURE_BY_LOGIN_PASSWORD', data)
  },
  GET_MANUFACTURE: async (context, id) => {
    let {
      data
    } = await Axios.get(HTTP_PATH + 'api/manufacture/manufacture/' + id)

    context.commit('SET_MANUFACTURE', data)
  },
  POST_MANUFACTURE: async (context, obj) => {
    console.log(obj)
    let {
      data
    } = await Axios.post(HTTP_PATH + 'api/manufacture/manufacture/', obj)
    context.commit('SET_MANUFACTURE', data)
  },
  PUT_MANUFACTURE: async (context, obj) => {

    let {
      data
    } = Axios.put(HTTP_PATH + 'api/manufacture/manufacture/' + obj.id + '/', obj)
    context.commit('SET_MANUFACTURE', data)
  },
  DELETE_MANUFACTURE: async (context, obj) => {
    let {
      data
    } = Axios.delete(HTTP_PATH + 'api/manufacture/manufacture/' + obj.id + '/', obj)
    context.commit("SET_MANUFACTURE", data)
  }

}
export default {
  state,
  getters,
  mutations,
  actions,
}