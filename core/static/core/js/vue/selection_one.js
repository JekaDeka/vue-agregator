DEVICE_TYPE = 'Устроства'
BRAND = 'Производитель'
DEVICE_MODEL = 'Модель'
FAULT = 'Неисправности'
var appSection = new Vue({

  delimiters: ['${', '}'],
  el: '#SelectionOne',
  affiliations,
  data: {
    titles = [DEVICE_TYPE, BRAND, DEVICE_MODEL, FAULT],
    affs: []
  },
  mounted() {
    this.$store.dispatch('GET_OBJCETS')
    this.affiliations = this.$affilations.getters.OBJECTS
  },
  methods: {
    SET_DATA: function() {}
  },
})