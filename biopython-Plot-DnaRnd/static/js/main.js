function drawGraph(disp) {
  var path = "/get/" + disp;
  var id = "#graph_" + disp;
  var img = "#plot_" + disp;
  $(id).append("<h4>" + disp + "</h4>");
  var plotdata = document.getElementById(img); 
  $.get(path, function(data) { 
    plotdata.src = data; 
  }); 
};

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