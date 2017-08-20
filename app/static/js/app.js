
Vue.component('one-list', {
    props: ['item'],
    template: '#template-one'
});


// register the grid component
Vue.component('demo-grid', {
  template: '#grid-template',
  props: {
    data: Array,
    columns: Array,
    filterKey: String
  },
  data: function () {
    var sortOrders = {}
    this.columns.forEach(function (key) {
      sortOrders[key] = 1
    })
    return {
      sortKey: '',
      sortOrders: sortOrders
    }
  },
  computed: {
    filteredData: function () {
      var sortKey = this.sortKey
      var filterKey = this.filterKey && this.filterKey.toLowerCase()
      var order = this.sortOrders[sortKey] || 1
      var data = this.data
      if (filterKey) {
        data = data.filter(function (row) {
          return Object.keys(row).some(function (key) {
            return String(row[key]).toLowerCase().indexOf(filterKey) > -1
          })
        })
      }
      if (sortKey) {
        data = data.slice().sort(function (a, b) {
          a = a[sortKey]
          b = b[sortKey]
          return (a === b ? 0 : a > b ? 1 : -1) * order
        })
      }
      return data
    }
  },
  filters: {
    capitalize: function (str) {
      return str.charAt(0).toUpperCase() + str.slice(1)
    }
  },
  methods: {
    sortBy: function (key) {
      this.sortKey = key
      this.sortOrders[key] = this.sortOrders[key] * -1
    }
  }
})

// bootstrap the demo
var demo = new Vue({
  el: '#demo',
  data: {
    searchQuery: '',
    gridColumns: ['name', 'power'],
    gridData: [
      { name: 'Chuck Norris', power: Infinity },
      { name: 'Bruce Lee', power: 9000 },
      { name: 'Jackie Chan', power: 7000 },
      { name: 'Jet Li', power: 8000 }
    ]
  }
});




var app_zero = new Vue({
    el: '#app-zero',
    data: {
        ts: {}
    },
    methods: {
        fetchData: function () {
            this.$http.get('/api/ts')
                .then(function (response) {
                    this.ts = response.data.now;
                }, function (err) {
                    console.log(err);
                });
        }
    },
    mounted: function () {
        setInterval(this.fetchData,
        1000);
    }
});

var app_one = new Vue({
    el: '#app-one',
    data: {
        one_list: []
    },
    methods: {
        fetchData: function () {
            this.$http.get('/api/one')
                .then(function (response) {
                    this.one_list = response.data.one;
                }, function (err) {
                    console.log(err);
                });
        }
    },
    mounted: function () {
        this.fetchData();
    }
});

var app_two = new Vue({
    el: '#app-two',
    data: {
        two_list: []
    },
    methods: {
        fetchData: function () {
            this.$http.get('/api/two')
                .then(function (response) {
                    this.two_list = response.data.two;
                }, function (err) {
                    console.log(err);
                });
        }
    },
    mounted: function () {
        this.fetchData();
    }
});

var app_four = new Vue({
    el: '#app-four',
    data: {
      message: 'Hello Vue.js!'
    },
    methods: {
      reverseMessage: function () {
        this.message = this.message.split('').reverse().join('')
      }
    }
  })


