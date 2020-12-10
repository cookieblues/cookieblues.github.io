// Set the dimensions and margins of the graph
var margin = {top: 15, right: 25, bottom: 25, left: 25},
    width = 250,
    height = 140 - margin.top - margin.bottom;

// Parse dates
var parseTime = d3.timeParse("%Y-%m-%d");

// append the svg object to the body of the page
// appends a 'group' element to 'svg'
// moves the 'group' element to the top left margin
var svg = d3.select(".polls").append("svg")
    .attr("width", width)
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
  .call(d3.axisLeft(y))
  .style('opacity', 0.15);

// Process CSVs
Promise.all([
  d3.csv("/polling/mean_polls.csv"),
  d3.csv("/polling/fixed_polls.csv")
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
    .call(d3.axisBottom(x))
    .style('opacity', 0.15);

  // Create a rect on top of the svg area: this rectangle recovers mouse position
  svg
    .append('rect')
    .style("fill", "none")
    .style("pointer-events", "all")
    .attr('width', width)
    .attr('height', height);

  // Add the lines
  var line = d3.line()
    .x(function(d) { return x(d.date) })
    .y(function(d) { return y(+d.value) })

  var partyLines = svg.selectAll("myLines")
    .data(pollingMean)
    .enter()
    .append("path")
      .attr("class", function(d){ return "partyLine " + d.values[0].party })
      .attr("d", function(d){ return line(d.values) } )
      .attr("stroke", function(d){ return partyColors[d.name] })
      .style("stroke-width", 2.5)
      .style("fill", "none")
      .style('opacity', 0.15)

  var svgagain = d3.select(".polls").select("svg")
    .on("mousemove", function() {
      // recover coordinate we need
      var mouse = d3.mouse(this)[0];
      var x0 = x.invert(mouse);
      redrawPartyLines(x0);
    });

  function redrawPartyLines(pt) {
    // push a new data point onto the back
    ptdata.push(pt);
    // Redraw the path:
    path.attr("d", function(d) { return line(d);})
    // If more than 100 points, drop the old data pt off the front
    if (ptdata.length > npoints) {
      ptdata.shift();
    }
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
      .style('opacity', 0.15)
})
