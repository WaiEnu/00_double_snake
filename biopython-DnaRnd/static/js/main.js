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
    methods: {
      navClick(e) {
        this.activePageName = e.currentTarget.getAttribute('data-icon-text')
      },
    }
  })