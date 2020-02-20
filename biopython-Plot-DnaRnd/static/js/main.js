$('#length').on('blur', function(){
  $('#locate').attr({'max': $('#length').val()});
})
$('#locate').attr({'max': $('#length').val()});

const vm = new Vue({
  el: '#app',
  delimiters: ["[[", "]]"],
  data: {
    activePageName: 'graph',
    icons: [
      {
        id: 'graph',
        text: 'graph'
      },
      {
        id: 'align',
        text: 'align'
      },
      {
        id: 'read',
        text: 'read'
      },
    ],
  },
  computed: {
  },
  methods: {
    navClick(e) {
      this.activePageName = e.currentTarget.getAttribute('data-icon-text')
    },
    fillMax: function() {
    },
  }
  
})