import Axios from 'axios'

const state = {

  marks_by_brand: []

}
const getters = {
  MARKS_BY_BRAND: state => {
    return state.marks_by_brand
  }
}
const mutations = {
  SET_MARKS_BY_BRAND: (state, data) => {
    state.marks_by_brand = data
  }
}
const actions = {
  GET_MARKS_BY_BRAND: ()
}

export default {
  state,
  getters,
  mutations,
  actions,
}