var app = new Vue({

  delimiters: ['${', '}'],
  el: '#SelectRegion',
  data: {
    loading: false,
    countrys: [],
    selected_country: {},
    title_country: "Выберите страну",
    seenCountry: false,
    seenTown: false,
    bool_country: false,
    url: "",
    towns: [],
    selected_town: {},
    title_town: "Выберите город",
    bool_town: false,

  },
  created: function() {
    this.loading = true
    this.$http.get('api/metro/country/')
      .then((response) => {
        this.countrys = response.data
        this.loading = false
      })
      .catch((err) => {
        this.loading = false
        console.log(err)
      })
  },


  computed: {},
  methods: {
    get_Town: function() {
      console.log(this.selected_country.id)
      if (this.bool_country) {
        this.loading = true
        this.$http.get('api/metro/search/town_by_coutnry/' + this.selected_country.id)
          .then((response) => {
            this.towns = response.data
            this.loading = true
          })
          .catch((err) => {
            this.loading = false
            console.log(err)
          })
      }


    },
    showCountrys: function() {
      this.seenCountry = !this.seenCountry
    },
    selectCountry: function(item) {

      this.bool_country = true
      this.selected_country = item
      this.seenCountry = false
      this.title_country = item.name
      this.get_Town()
    },
    showTowns: function() {
      this.seenTown = !this.seenTown
      console.log(this.towns)
    },
    selectTown: function(item) {
      this.title_town = item.name
      this.bool_town = true
      this.selected_town = item
      this.url = '' + this.selected_country.name + '/' + this.selected_town.name
      this.seenTown = false
    }
  },


});