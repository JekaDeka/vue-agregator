var app = new Vue({
  delimiters: ['${', '}'],
  el: '#LinkMark',
  data: {
    data: [],
    loading: false,
    start: 0,
    end: 3,
    seen: false

  },
  mounted: function() {
    console.log('hello')
  },
  created: function() {
    console.log('hello')
    this.loading = true;
    this.$http.get('api/device/mark/')
      .then((response) => {
        this.data = response.data
        this.loading = true
      })
      .catch((err) => {
        this.loading = false
        console.log(err)
      })
  },
  methods: {
    showAll: function() {
      this.seen = !this.seen
    },
    setBefore: function() {

      if (this.start - 3 <= -3) {
        this.start = this.data.length - 3
        this.end = this.data.length
        return
      } else if (this.start - 3 < 0) {
        this.start = 0
        this.end = 3
        return
      } else {
        this.start -= 3
        this.end = this.start + 3
      }
    },
    setNext: function() {
      if (this.end + 3 >= this.data.length + 3) {
        this.end = 3
        this.start = 0
      } else if (this.end + 3 >= this.data.length) {
        this.end = this.data.length
        this.start = this.end - 3
      } else {
        this.end += 3
        this.start = this.end - 3
      }
    },
  },
  computed: {
    ListData: function() {
      list_result = []
      for (var i = this.start; i < this.end; i++) {
        list_result.push(this.data[i])
      }
      console.log("hello")
      return list_result
    }
  }
})