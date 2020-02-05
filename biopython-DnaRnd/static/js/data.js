function drawGraph(value) {
    var id = "plt_" + value;
    var plotdata = document.getElementById(id);
    $.get("/plot/" + value, function(data) {
        plotdata.src = "data:image/png:base64," + data;
    });
};

$(document).ready(function() {
    //initialize components
    var target_o = "origin";
    var target_m = "mutate";
    drawGraph(target_o);
    drawGraph(target_m);
});