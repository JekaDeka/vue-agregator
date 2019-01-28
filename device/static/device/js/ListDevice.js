var appDevice = new Vue({
  delimiters: ['${', '}'],
  el: '#ListDevice',
  data: {
    selected_device: -1,
    devices: [],
    loading: false,
    currentDevice: {},
    message: null,
    newDevice: {
      'id': null,
      'name': null
    },
  },
  mounted: function() {
    this.getDevices();
  },
  methods: {
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
    getDevice: function(id) {
      this.loading = true;
      this.$http.get('/api/device_model/' + id + '/')
        .then((response) => {
          this.currentDevice = response.data;
          this.loading = false;
        })
        .catch((err) => {
          this.loading = false;
          console.log(err);
        })
    },
    addDevice: function() {
      this.loading = true;
      this.$http.post('/api/device_model/', this.newDevice)
        .then((response) => {
          this.loading = false;
          this.getDevices();
        })
        .catch((err) => {
          this.loading = false;
          console.log(err);
        })
    },
    updateDevice: function() {
      this.loading = true;
      this.$http.put('/api/device_model/${this.currentDevice.device_id}/', this.currentDevice)
        .then((response) => {
          this.loading = false;
          this.currentDevice = response.data;
          this.getDevices();
        })
        .catch((err) => {
          this.loading = false;
          console.log(err);
        })
    },
    deleteDevice: function(id) {
      this.loading = true;
      this.$http.delete('/api/device_model/${id}/')
        .then((response) => {
          this.loading = false;
          this.getDevices();
        })
        .catch((err) => {
          this.loading = false;
          console.log(err);
        })
    }
  }
})