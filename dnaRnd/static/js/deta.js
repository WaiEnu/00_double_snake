
const STT = 'STT';
const STP = 'STP';
const LEN = 'LEN';
const color = ["SkyBlue","Coral"];

var margin = {top: 30, right: 20, bottom: 30, left: 40},
width = 300 - margin.left - margin.right,
height = 300 - margin.top - margin.bottom;

function svg(disp) {
  var path = "/get-" + disp;
  var id = "#graph_" + disp;
  var lb1 = disp+"_STT";
  var lb2 = disp+"_LEN";

  $(id).append("<h4>" + disp + "</h4>");

  d3.json(path)
    .then(function(data){
      // 通常処理（グラフの描画など）
      setGraph(id,lb1,data,STT,STP,color[0]);
      setGraph(id,lb2,data,LEN,STP,color[1]);
    })
    .catch(function(error){
    // エラー処理
    });
}

function setGraph(id,disp,dataset,x,y,color){
    var svg = d3.select(id).append("svg")
      .attr('class', "svg_" + disp)
      .attr("width", width + margin.left + margin.right)
      .attr("height", height + margin.top + margin.bottom)
      .append("g")
      .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    var xScale = d3.scaleLinear()
      .domain([0,d3.max(dataset, function(d) { return d[x]; })])
      .range([0,width]);
  
    var yScale = d3.scaleLinear()
      .domain([0,d3.max(dataset, function(d) { return d[y]; })])
      .range([height,0]);
    
    svg.append("g")
      .attr('class', "x axis")
      .attr("transform", "translate(" + 0 + "," + height + ")")
      .call(d3.axisBottom(xScale));
  
    svg.append("g")
      .attr('class', "y axis")
      .attr("transform", "translate(" + 0 + "," + 0 + ")")
      .call(d3.axisLeft(yScale));
    
    svg.append("g")
      .selectAll("circle")
      .data(dataset)
      .enter()
      .append("circle")
      .attr("cx", function(d) {
        return xScale(d[x]);
      })
      .attr("cy", function(d) {
        return yScale(d[y]);
      })
      .attr("fill", color)
      .attr("r", 1);
}