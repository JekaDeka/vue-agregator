import Axios from 'axios'
var HTTP_PATH = 'http://127.0.0.1:8000/';
const state = {
  manufacture_service: {},
  special_manufacture_services: [],
}
const getters = {
  MANUFACTURE_SERVICE: state => {
    return state.manufacture_service
  },
  SPECIAL_MANUFACTURE_SERVICES: state => {
    return state.special_manufacture_services
  }
}
const mutations = {
  SET_MANUFACTURE_SERVICE: (state, data) => {
    state.manufacture_service = data
  },
  SET_SPECIAL_MANUFACTURE_SERVICE: (state, data) => {
    state.special_manufacture_services = data
  }
}
const actions = {
  POST_MANUFACTURE_SERVICE: async (context, obj) => {
    let {
      data
    } = await Axios.post(HTTP_PATH + 'api/manufacture_service/manufacture_service/', obj)
    context.commit("SET_MANUFACTURE_SERVICE", data)
  },
  GET_MANUFACTURE_SERVICE_BY_MANUFACTURE: async (context, obj) => {
    var data = []
    var manufacture_services = await Axios.get(HTTP_PATH + 'api/manufacture_service/filter/manufacture_services_by_manufacture/' + obj.id)
    for (var i = 0; i < manufacture_services.data.length; i++) {

      var mark = await Axios.get(HTTP_PATH + 'api/device/mark/' + manufacture_services.data[i].mark + '/')
      var brand = await Axios.get(HTTP_PATH + 'api/device/brand/' + mark.data.brand + '/')
      var breakage_action = await Axios.get(HTTP_PATH + 'api/manufacture_service/breakage_action/' + manufacture_services.data[i].breaking_action + '/')
      var ms = {}
      ms.manufacture_service = manufacture_services.data[i]
      ms.breakage_action = breakage_action.data
      ms.brand = brand.data
      ms.mark = mark.data
      data.push(ms)
    }
    context.commit('SET_SPECIAL_MANUFACTURE_SERVICE', data)
  },
  PUT_MANUFACTURE_SERVICE: async (context, obj) => {
    let {
      data
    } = await Axios.put(HTTP_PATH + 'api/manufacture_service/manufacture_service/' + obj.id + '/', obj)
    context.commit('SET_MANUFACTURE_SERVICE', data)
  },
  DELETE_MANUFACTURE_SERVICE: async (context, obj) => {
    let {
      data
    } = await Axios.delete(HTTP_PATH + 'api/manufacture_service/manufacture_service/' + obj.id + '/', obj)
    context.commit('SET_MANUFACTURE_SERVICE', data)
  }
}

export default {
  state,
  getters,
  mutations,
  actions,
}