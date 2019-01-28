DEVICE_TYPE = 'Устроства'
BRAND = 'Производитель'
DEVICE_MODEL = 'Модель'
FAULT = 'Неисправности'
var app = new Vue({
  delimiters: ['${', '}'],
  el: '#LeftMenu',
  data: {
    message: 'Выбирайте пункты последовательно',
    // для страницы
    titles: [DEVICE_TYPE, BRAND, DEVICE_MODEL, FAULT],
    device_title: DEVICE_TYPE,
    seens: [{
      'object': DEVICE_TYPE,
      'open': false
    }, {
      'object': BRAND,
      'open': false
    }, {
      'object': DEVICE_MODEL,
      'open': false
    }, {
      'object': FAULT,
      'open': false
    }],
    // загрузчики
    loading: false,
    loading_type_devices: false,

    // АПИ данные
    types_by_affiliation: [],

    divece_types: [],
    brands: [],
    device_models: [],
    faults: [],
    // выбранные

    bool_brand: false,
    bool_device_type: false,
    bool_fault: false,
    bool_device_model: false,

    selected_device_type: {},
    selected_brand: {},
    selected_device_model: {},
    selected_fault: {},
    selected_device_type: {},


    selected_brand: {},
    selected_device_model: {},
    selected_fault: {},

    brands: [],
    device_models: [],
    faults: [],

  },
  mounted: function() {

  },
  methods: {
    getErorMessage: function(seen) {
      if (seen.object == DEVICE_TYPE) {
        return "Что-то пошло не так"
      }
      if (seen.object == BRAND) {
        return "Сначала нужно заполнить поле " + DEVICE_TYPE
      }

      if (seen.object == DEVICE_MODEL) {
        return "Сначала нужно заполнить поля " + DEVICE_TYPE + " " + BRAND
      }
      if (seen.object == FAULT) {
        return "Сначала нужно заполнить поля " + DEVICE_TYPE + " " + BRAND + " " + DEVICE_MODEL
      }
    },
    getName: function(seen) {

      if (seen.object == DEVICE_TYPE) {
        if (this.bool_device_type)
          return this.selected_device_type.name
        else
          return seen.object
      }
      if (seen.object == BRAND) {
        if (this.bool_brand)
          return this.selected_brand.name
        else
          return seen.object
      }

      if (seen.object == DEVICE_MODEL) {

        if (this.bool_device_model)
          return this.selected_device_model.name
        else
          return seen.object
      }
      if (seen.object == FAULT) {
        if (this.bool_fault)
          return this.selected_fault.name
        else
          return seen.object
      }
    },
    getObjects: function(seen) {

      if (seen.object == BRAND)
        return this.brands

      if (seen.object == DEVICE_MODEL)
        return this.device_models
      if (seen.object == BRAND)
        return this.faults

    },

    setSelect: function(seen, obj) {
      if (seen.object == DEVICE_TYPE) {
        this.seens[0].open = 0
        this.selected_device_type = obj
        this.bool_device_type = true
        this.bool_brand = false
        this.bool_device_model = false
        this.bool_fault = false

      }
      if (seen.object == BRAND) {

        this.seens[1].open = 0

        this.selected_brand = obj
        this.bool_brand = true

        this.bool_device_model = false
        this.bool_fault = false
      }
      if (seen.object == DEVICE_MODEL) {

        this.seens[2].open = 0
        this.selected_device_model = obj

        this.bool_device_model = true
        this.bool_fault = false
      }
      if (seen.object == FAULT) {

        this.seens[3].open = 0
        this.selected_fault = obj
        this.bool_fault = true
      }
    },
    showList: function(seen) {

      if (seen.object == DEVICE_TYPE) {
        if (seen.open != 0) {
          this.seens[0].open = 0
          return false
        }

        this.getDeviceAffiliaton()
        this.seens[0].open = true
        return
      }
      if (seen.object == BRAND) {
        if (seen.open != 0) {
          this.seens[1].open = 0
          return false
        }
        if (this.bool_device_type) {

          this.getBrands()
          this.seens[1].open = true
          return
        } else {
          this.seens[1].open = 2
          return
        }
      }
      if (seen.object == DEVICE_MODEL) {
        if (this.seens[2].open != false) {
          this.seens[2].open = 0
          return false
        }
        if (this.bool_brand) {


          this.getDeviceModels()
          this.seens[2].open = true
          return
        } else {
          this.seens[2].open = 2
          return
        }
      }
      if (seen.object == FAULT) {
        if (seen.open != 0) {
          this.seens[3].open = 0
          return false
        }

        if (this.bool_device_model) {
          this.getFaults()
          this.seens[3].open = true
          return
        } else {
          this.seens[3].open = 2
          return
        }
      }
      return true
    },
    getDeviceAffiliaton: function() {
      this.types_by_affiliation = []
      this.device_affiliations = []
      this.loading = true
      if (true) {
        this.$http.get('api/device/device_affiliation/')
          .then((response) => {
            this.loading_type_devices = true
            this.device_affiliations = []
            this.device_affiliations = response.data
            this.loading = false
            this.setTypesByAffiliation()

          })
          .catch((err) => {
            this.loading = false
            console.log(err)
          })


      }

    },
    getDeviceTypes: function(aff) {

      this.loading = true;
      var data;
      this.$http.get('/api/device/search/device_type/device_affiliation/' + aff.id)
        .then((response) => {

          data = response.data;
          dict = {}
          dict.types = []
          for (var i = 0; i < data.length; i++)
            dict.types.push(data[i])
          dict.affliation = aff
          this.types_by_affiliation.push(dict)
          this.loading = false;

        })
        .catch((err) => {
          data = false
          this.loading = false;
          console.log(err);
        })


    },
    setTypesByAffiliation: function() {
      for (var i = 0; i < this.device_affiliations.length; i++) {


        this.getDeviceTypes(this.device_affiliations[i])

      }
    },
    getBrands: function() {
      if (this.bool_device_type) {
        this.loading = true
        this.loading_brands = true;
        this.$http.get('api/device/search/brand/device_type/' + this.selected_device_type.id)
          .then((response) => {
            this.brands = response.data;
            this.loading_brands = false;
          })
          .catch((err) => {
            this.loading_brands = false;
            console.log(err);
          })
      }
    },
    getDeviceModels: function() {
      if (this.bool_brand && this.bool_device_type) {
        this.loading = true;
        this.$http.get('api/device/search/device_model/device_type/brand/' + this.selected_device_type.id + '/' + this.selected_brand.id)
          .then((response) => {
            this.device_models = response.data;
            this.loading = false;
          })
          .catch((err) => {
            this.loading = false;
            console.log(err);
          })
      }
    },

    getFaults: function() {
      if (this.bool_device_model) {

        this.loading = true;
        this.$http.get('api/manufacture_service/search/fault/device_model/' + this.selected_device_model.id)
          .then((response) => {
            this.faults = response.data;
            this.loading = false;

          })
          .catch((err) => {
            this.loading = false;
            console.log(err);
          })
      }
    },
  }
})