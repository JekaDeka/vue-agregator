import Axios from 'axios'
var HTTP_PATH = 'http://127.0.0.1:8000/';

const state = {
  bool_login: false,
}
const getters = {
  BOOL_LOGIN: state => {
    return state.bool_login
  },
}
const mutations = {
  SET_BOOL_LOGIN: (state, data) => {
    if (data.length == 0) {
      state.bool_login = true
    } else {
      state.bool_login = false
    }
  },
}
const actions = {


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
}

export default {
  state,
  getters,
  mutations,
  actions,
}

// const state = {
//
// }
// const getters = {
//
// }
// const mutations = {
//
// }
// const actions = {
//
// }
//
// export default {
//   state,
//   getters,
//   mutations,
//   actions,
// }