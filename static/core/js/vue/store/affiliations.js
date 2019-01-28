import {
  HTTP_AGREGATOR
} from './http.js'

Vue.use(Vuex)

export const affiliations = new Vuex.Store({
  state: {
    objects: [],
    object: {},
  },
  getters: {
    OBJECTS: state => {
      return state.objects
    }
    OBJECT: state => {
      return state.object
    }
  },
  mutations: {
    SET_OBJECT: (state, object) => {
      state.object = object
    },
    SET_OBJECTS: (state, objects) => {
      state.objects = objects
    },
  },
  actions: {
    getObjects: async (context) => {
      let {
        objects
      } = await Axios.get(HTTP_AGREGATOR + 'vice_affiliation/')
      context.commit('SET_OBJECTS')

    },
    getObject: async ({
      context
    }, id) => {
      let {
        object
      } = await Axios.get(HTTP_AGREGATOR + 'api/device/device_affiliation/' + id)

      context.commit('SET_OBJECT', object)
    },
  },


});