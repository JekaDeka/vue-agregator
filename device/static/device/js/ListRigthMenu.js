var appBrand = new Vue({
delimiters: ['${','}'],
el: '#ListRigthMenu',
data: {
      // for list brand
      show_list_brand:false,
      selected_brand:{},
      // for list device_model
      show_list_device_model:false,
      selected_device_model:{},
      // for list fault
      show_list_fault:false,
      selected_fault:{},
      // for list device_type
      show_list_device_type:false,
      selected_device_type:{},
      loading: false,
      // brad

      brands: [],

      title_brand:'Производитель',
      // device_model
      title_device_model:"Модель",

      devices: [],


      // device_type
      title_device_type:"Устройство",

      device_types:[],
      // fault
      title_fault:"Неисправность",

      faults:[],
      // proposa

      newPropsal:{},
   },
mounted: function() {
    this.getBrands();
    this.getDevices();
    this.getDeviceTypes();
    this.getFaults();
},
methods: {
showListDeviceType:function(){
  if(this.show_list_device_type==false)
    this.show_list_device_type=true
  else
    this.show_list_device_type=false
},
setDeviceType:function(data){
  this.show_list_device_type=false
  this.title_device_type=data.name
  this.selected_device_type=data
},
showListBrand:function(){
  if(this.show_list_brand==false)
    this.show_list_brand=true
  else
    this.show_list_brand=false
},
setBrand:function(data){
  this.show_list_brand=false
  this.title_brand=data.name
  this.selected_brand=data
},
showListDeviceModel:function(){
  if(this.show_list_device_model==false)
    this.show_list_device_model=true
  else
    this.show_list_device_model=false
},
setDeviceModel:function(data){
  this.show_list_device_model=false
  this.title_device_model=data.name
  this.selected_device_model=data
},
showListFault:function(){
  if(this.show_list_fault==false)
    this.show_list_fault=true
  else
    this.show_list_fault=false
},
setFault:function(data){
  this.show_list_fault=false
  this.title_fault=data.name
  this.selected_fault=data
},
makeProposal:function(event){
  this.loading = true;
  this.$http.post('/api/proposal/',this.newPropsal)
      .then((response) => {
        this.loading = false;
        this.getDevices();
      })
      .catch((err) => {
        this.loading = false;
        console.log(err);
      })

},
getBrands: function() {
this.loading_brands = true;
this.$http.get('/api/brand/')
    .then((response) => {
      this.brands = response.data;
      this.loading_brands = false;
    })
    .catch((err) => {
     this.loading_brands = false;
     console.log(err);
    })
},
getDevices: function() {
this.loading = true;
this.$http.get('/api/device_model/')
    .then((response) => {
      this.devices = response.data;
      this.loading = false;
    })
    .catch((err) => {
     this.loading = false;
     console.log(err);
    })
},
getDeviceTypes: function() {
this.loading = true;
this.$http.get('/api/device_type/')
    .then((response) => {
      this.device_types = response.data;
      this.loading = false;
    })
    .catch((err) => {
     this.loading = false;
     console.log(err);
    })
},
getFaults: function() {
this.loading = true;
this.$http.get('/api/fault/')
    .then((response) => {
      this.faults = response.data;
      this.loading = false;
    })
    .catch((err) => {
     this.loading = false;
     console.log(err);
    })
},

}})
