const vm = new Vue({
    el: '#app',
    delimiters: ["[[", "]]"],
    data: {
      align:'100',
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