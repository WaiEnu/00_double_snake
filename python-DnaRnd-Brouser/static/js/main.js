const vm = new Vue({
    el: '#app',
    data: {
      isActive: '1'
    },
    methods: {
      change: function(num){
        this.isActive = num
      }
    }
  })