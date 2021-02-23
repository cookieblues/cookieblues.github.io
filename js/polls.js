// Set the dimensions and margins of the graph
var margin = {top: 50, right: 250, bottom: 20, left: 25},
    width = 1100 - margin.left - margin.right,
    height = 500 - margin.top - margin.bottom;

// Parse dates
var parseTime = d3.timeParse("%Y-%m-%d");

// append the svg object to the body of the page
// appends a 'group' element to 'svg'
// moves the 'group' element to the top left margin
var svg = d3.select(".content").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform",
          "translate(" + margin.left + "," + margin.top + ")");


// List of groups (here I have one group per column)
var partyNames = [
  'Socialdemokratiet',
  'Radikale_Venstre',
  'Det_Konservative_Folkeparti',
  'Nye_Borgerlige',
  'Klaus_Riskær_Pedersen',
  'Socialistisk_Folkeparti',
  'Veganerpartiet',
  'Liberal_Alliance',
  'Kristendemokraterne',
  'Dansk_Folkeparti',
  'Stram_Kurs',
  'Venstre',
  'Enhedslisten',
  'Alternativet'
]

var partyColors = {
  'Socialdemokratiet':"#C10B20",
  'Radikale_Venstre':"#D50080",
  'Det_Konservative_Folkeparti':"#034536",
  'Nye_Borgerlige':"#024450",
  'Klaus_Riskær_Pedersen':"#1F9FAC",
  'Socialistisk_Folkeparti':"#A40000",
  'Veganerpartiet':"#80A51A",
  'Liberal_Alliance':"#0A1B3E",
  'Kristendemokraterne':"#F5820B",
  'Dansk_Folkeparti':"#FFFF00",
  'Stram_Kurs':"#000000",
  'Venstre':"#003460",
  'Enhedslisten':"#D0004D",
  'Alternativet':"#00FF00"
};

// Add X axis --> it is a date format
var x = d3.scaleTime()
  .range([0, width]);

// Add Y axis
const yMax = 40;
var y = d3.scaleLinear()
  .domain([0, yMax])
  .range([ height, 0 ]);
svg.append("g")
  .call(d3.axisLeft(y));

// Highlight the party that is hovered
var partyHighlight = function(d){
  if ('values' in d) {
    selected_party = d.values[0].party
  }
  else if ('name' in d) {
    selected_party = d.name
  }
  else {
    selected_party = d.party
  }
  d3.selectAll(".dot")
    .transition()
    .duration(200)
    .style("opacity", 0.1)
  d3.selectAll(".partyLine")
    .transition()
    .duration(200)
    .style("opacity", 0.1)
  d3.selectAll(".partyText")
    .transition()
    .duration(200)
    .style("opacity", 0.1)
  d3.selectAll("." + selected_party)
    .transition()
    .duration(200)
    .style("opacity", 1.0)
}

// Un-highlight parties
var partyNotHighlight = function(){
  d3.selectAll(".dot")
    .transition()
    .duration(200)
    .style("opacity", 0.375)
  d3.selectAll(".partyLine")
    .transition()
    .duration(200)
    .style("opacity", 1.0)
  d3.selectAll(".partyText")
    .transition()
    .duration(200)
    .style("opacity", 1.0)
}

// TBA
var showLinesUpToMouse = function(){
  // recover date coordinate we need
  var mouse = d3.mouse(this)[0];
  var x0 = x.invert(mouse);
}

// Process CSVs
Promise.all([
  d3.csv("../polling/mean_polls.csv"),
  d3.csv("../polling/fixed_polls.csv")
]).then(function(files) {
  var pollingMean = partyNames.map( function(partyName) { // .map allows to do something for each element of the list
    return {
      name: partyName,
      values: files[0].map(function(d) {
          return {date: parseTime(d.date), value: +d[partyName], party: partyName};
      })
    };
  });

  // Add X axis --> it is a date format
  x.domain(d3.extent(files[0], function(d) { return parseTime(d.date); }));
  svg.append("g")
    .attr("transform", "translate(0," + height + ")")
    .call(d3.axisBottom(x));

  // Create a rect on top of the svg area: this rectangle recovers mouse position
  svg
    .append('rect')
    .style("fill", "none")
    .style("pointer-events", "all")
    .attr('width', width)
    .attr('height', height)
    .on('mouseover', mouseover)
    .on('mousemove', mousemove)
    .on('mouseout', mouseout);
    
  // Add the lines
  var line = d3.line()
    .x(function(d) { return x(d.date) })
    .y(function(d) { return y(+d.value) })

  var mouseG = svg.append("g")
    .attr("class", "mouse-over-effects");

  mouseG.append("path") // this is the black vertical line to follow mouse
    .attr("class", "mouse-line")
    .attr("d", function() {
      var d = "M" + 0 + "," + y(yMax);
      d += " " + 0 + "," + y(0);
      return d;
    })
    .style("stroke-dasharray", ("3, 3"))  // <== This line here!!
    .style("stroke", "black")
    .style("stroke-width", 1)
    .style("opacity", 1);
    

  var partyLines = svg.selectAll("myLines")
    .data(pollingMean)
    .enter()
    .append("path")
      .attr("class", function(d){ return "partyLine " + d.values[0].party })
      .attr("d", function(d){ return line(d.values) } )
      .attr("stroke", function(d){ return partyColors[d.name] })
      .style("stroke-width", 2.5)
      .style("fill", "none")
      .on("mouseover", partyHighlight)
      .on("mouseleave", partyNotHighlight)
  console.log(partyLines)

  // var svgagain = d3.select(".content").select("svg")
  //   .on("mousemove", function() {
  //     // recover coordinate we need
  //     var mouse = d3.mouse(this)[0];
  //     var x0 = x.invert(mouse);
  //     redrawPartyLines(x0);
  //   });

  // function redrawPartyLines(pt) {
  //   // push a new data point onto the back
  //   ptdata.push(pt);
  //   // Redraw the path:
  //   path.attr("d", function(d) { return line(d);})
  //   // If more than 100 points, drop the old data pt off the front
  //   if (ptdata.length > npoints) {
  //     ptdata.shift();
  //   }
  // }

  var lastVals = pollingMean.forEach(element => element.values[element.values.length-1]);
  
  // 1.8 from each other, 1 below its real value
  function labelSpacing() {

  };
  
  // Add a legend at the end of each line
  var labels = svg
    .selectAll("myLabels")
    .data(pollingMean)
    .enter()
      .append('g')
      .append("text")
        .datum(function(d) { return {name: d.name, value: d.values[d.values.length - 1]}; }) // keep only the last value of each time series
        .attr("transform", function(d) { return "translate(" + x(d.value.date) + "," + y(d.value.value) + ")"; }) // Put the text at the position of the last point
        .attr("x", 12)
        .attr("class", function(d){ return "partyText " + d.name })
        .text(function(d) { return d.name.replaceAll("_", " ") + " " + d.value.value + "%"; })
        .style("fill", function(d){ return partyColors[d.name] })
        .style("font-size", 15)
      .on("mouseover", partyHighlight)
      .on("mouseleave", partyNotHighlight)

  // This allows to find the closest X index of the mouse:
  var bisect = d3.bisector(function(d) { return parseTime(d.date); }).left;

  // What happens when the mouse move -> show the annotations at the right positions.
  function mouseover() {
    labels.style("opacity", 1)
    d3.select(this).lower();
    d3.select(".mouse-line")
      .style("opacity", 1);
  }
  
  // What happens when the mouse 
  function mousemove() {
    // recover coordinate we need
    var mouse = d3.mouse(this)[0];
    var x0 = x.invert(mouse);
    // find idx in data
    var i = bisect(files[0], x0);
    selectedData = files[0][i];
    //var asd = function(d) { return selectedData[d.name]};
    var ypos = [];
    var ys = Object.values(selectedData).slice(1).map(parseFloat).sort();
    console.log(ys);
    labels
      .attr("transform", function(d) { return "translate(" + x(parseTime(selectedData.date)) + "," + y(selectedData[d.name]) + ")"; }) // Put the text at the position of the mouse
      .attr("x", -5)
      .text(function(d) { return "\xa0\xa0" + d.name.replaceAll("_", " ") + " " + selectedData[d.name] + "%"; })

    // Vertical dotted date line
    var vertPos = mouse-1
    d3.select(".mouse-line")
      .attr("d", function() {
        var d = "M" + vertPos + "," + y(yMax);
        d += " " + vertPos + "," + y(0);
        return d;
      })
    
    var ypos = [];
    d3.selectAll("myLines")
    .attr("transform", function(d, i) {
      console.log(width/mouse)
      var xDate = x.invert(mouse),
          bisect = d3.bisector(function(d) { return d.date; }).right;
          idx = bisect(d.value, xDate);
      
      var beginning = 0,
          end = lines[i].getTotalLength(),
          target = null;

      while (true){
        target = Math.floor((beginning + end) / 2);
        pos = lines[i].getPointAtLength(target);
        if ((target === end || target === beginning) && pos.x !== mouse) {
            break;
        }
        if (pos.x > mouse)      end = target;
        else if (pos.x < mouse) beginning = target;
        else break; //position found
      }
      
      d3.select(this).select('text')
        .text(y.invert(pos.y).toFixed(2));
        
        ypos.push ({ind: i, y: pos.y, off: 0});
        
      return "translate(" + mouse + "," + pos.y +")";
    })
    .call(function(sel) {
      ypos.sort (function(a,b) { return a.y - b.y; });
      ypos.forEach (function(p,i) {
        if (i > 0) {
          var last = ypos[i-1].y;
          ypos[i].off = Math.max (0, (last + 15) - ypos[i].y);
          ypos[i].y += ypos[i].off;
        }
      })
      ypos.sort (function(a,b) { return a.ind - b.ind; });
    })
    .select("text")
    
    .attr("transform", function(d,i) {
      return "translate (10,"+(3+ypos[i].off)+")";
    });
  }

  function mouseout() {
    labels.style("opacity", 0)
    d3.select(".mouse-line")
      .style("opacity", 1);
  }



  // Reformat the data: we need an array of arrays of {x, y} tuples
  var pollingData = partyNames.map( function(partyName) { // .map allows to do something for each element of the list
    return {
      name: partyName,
      values: files[1].map(function(d) {
          return {date: parseTime(d.date), value: +d[partyName], party: partyName};
        })
      };
  });
  // I strongly advise to have a look to dataReady with
  // console.log(dataReady)

  // Add the points
  svg
    // First we need to enter in a group
    .selectAll("dot")
    .data(pollingData)
    .enter()
      .append('g')
      .style("fill", function(d){ return partyColors[d.name] })
    // Second we need to enter in the 'values' part of this group
    .selectAll("myPoints")
    .data(function(d){ return d.values })
    .enter()
    .append("circle")
      .attr("class", function (d) { return "dot " + d.party } )
      .attr("cx", function(d) { return x(d.date) } )
      .attr("cy", function(d) { return y(d.value) } )
      .attr("r", 4)
      .style('opacity', 0.375)
      .on("mouseover", partyHighlight)
      .on("mouseleave", partyNotHighlight)
})
