new Vue({
  delimiters: ['${', '}'],
  el: '#LinkBrand',
  data: {
    data: [],
    loading: false,
    start: 0,
    end: 3,

  },
  mounted: function() {
    console.log('hello')
  },
  created: function() {
    console.log('hello')
    this.loading = true;
    this.$http.get('api/device/brand/')
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
    setBefore: function() {

      if (this.start - 3 <= -3) {
        this.start = this.$store.getters.BRANDS.length - 3
        this.end = this.$store.getters.BRANDS.length
      } else if (this.start - 3 < 0) {
        this.start = 0
        this.end = 3
      } else {
        this.start -= 3
        this.end -= 3
      }
    },
    setNext: function() {
      if (this.end + 3 >= this.$store.getters.BRANDS.length + 3) {
        this.end = 3
        this.start = 0
      } else if (this.end + 3 >= this.$store.getters.BRANDS.length) {
        this.end = this.$store.getters.BRANDS.length
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