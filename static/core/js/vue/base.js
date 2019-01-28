app = new Vue({
  el: "#go_register",

  methods: {
    goLogin: function() {
      var url = window.location.pathname
      var list = url.slice('/')
      window.location.pathname = list[1] + '/' + 'register/login/'
    }
  }
})