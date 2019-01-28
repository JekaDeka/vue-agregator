var app = new Vue({
  delimiters: ['${','}'],
  el: '.ListBrand',
  data: {
    lol: 'Lol',
    brands: [],
   loading: false,
   currentBrand: {},
   message: null,
   newBrand: { 'id': null, 'name': null },
 },
 mounted: function() {
this.getBrands();
},
methods: {
getBrands: function() {
this.loading = true;
this.$http.get('/api/brand/')
    .then((response) => {
      this.brands = response.data;
      this.loading = false;
    })
    .catch((err) => {
     this.loading = false;
     console.log(err);
    })
},
getBrand: function(id) {
this.loading = true;
this.$http.get('/api/brand/${id}/')
    .then((response) => {
      this.currentBrand = response.data;
      this.loading = false;
    })
    .catch((err) => {
      this.loading = false;
      console.log(err);
    })
},
addBrand: function() {
this.loading = true;
this.$http.post('/api/brand/',this.newBrand)
    .then((response) => {
      this.loading = false;
      this.getBrands();
    })
    .catch((err) => {
      this.loading = false;
      console.log(err);
    })
},
updateBrand: function() {
this.loading = true;
this.$http.put('/api/brand/${this.currentBrand.brand_id}/',     this.currentBrand)
    .then((response) => {
      this.loading = false;
      this.currentBrand = response.data;
      this.getBrands();
    })
    .catch((err) => {
      this.loading = false;
      console.log(err);
    })
},
deleteBrand: function(id) {
this.loading = true;
this.$http.delete('/api/brand/${id}/' )
    .then((response) => {
      this.loading = false;
      this.getBrands();
    })
    .catch((err) => {
      this.loading = false;
      console.log(err);
    })
}
}  })
