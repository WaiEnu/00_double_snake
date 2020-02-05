const vm = new Vue({
    el: '#app',
    delimiters: ["[[", "]]"],
    data: {
      activePageName: 'read',
      icons: [
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