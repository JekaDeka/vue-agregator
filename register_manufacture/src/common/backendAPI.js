/* eslint-disable */
// import * as types from '../store/mutation-types'
import axios from 'axios'
import {
  store
} from '../store'
// import router from '../router'
import AWN from "awesome-notifications"
var options = {
  duration: 4000,
  maxNotifications: 3,
  position: 'top-right',
  labels: {
    tip: 'Подсказка',
    info: 'Увдомление',
    warning: 'Внимание',
    success: 'Сохранено',
    async: 'Загрузка...',
  }
}
let notifier = new AWN(options)

axios.interceptors.request.use(
  config => {
    if (store.state.token) {
      config.headers.Authorization = `JWT ${store.state.token}`
    }
    return config
  },
  err => {
    return Promise.reject(err)
  })


export function base() {
  return 'http://127.0.0.1:8000/api/'
}

/* --------- USER API ----------------  */
// export function UserList() {
//   return axios.get(base() + 'users/')
// }
// export function UserDetail(pk) {
//   return axios.get(base() + `users/${pk}`)
// }
/* --------- PAGE API ----------------  */
// export function PageList() {
//   return axios.get(base() + 'pages/')
// }
// export function PageDetail(slug) {
//   return axios.get(base() + `pages/${slug}/`)
// }
export function CategoryList() {
  return axios.get(base() + 'pages/')
}
export function CategoryDetail(slug) {
  return axios.get(base() + `pages/${slug}/`)
}

export function Notify() {
  return notifier
}