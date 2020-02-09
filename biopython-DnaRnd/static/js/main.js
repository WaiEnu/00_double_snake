const vm = new Vue({
    el: '#app',
    delimiters: ["[[", "]]"],
    data: {
      activePageName: 'origin',
      icons: [
        {
          id: 'origin',
          text: 'origin'
        },
        {
          id: 'mutate',
          text: 'mutate'
        },
      ],
    },
    methods: {
      navClick(e) {
        this.activePageName = e.currentTarget.getAttribute('data-icon-text')
      },
    }
  })