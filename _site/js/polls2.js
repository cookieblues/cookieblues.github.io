// Set the dimensions and margins of the graph
var margin = {top: 50, right: 250, bottom: 20, left: 25},
    width = 1100 - margin.left - margin.right,
    height = 700 - margin.top - margin.bottom;

var parseTime = d3.timeParse("%Y-%m-%d");

var x = d3.scaleTime()
    .range([0, width]);

const yMax = 40;
var y = d3.scaleLinear()
    .domain([0, yMax])
    .range([ height-50, 0 ]);

var xAxis = d3.axisBottom(x)
var yAxis = d3.axisLeft(y);

// Define function to plot lines
var line = d3.line()
    .defined(function (d) { return d.value != ""; })
    .x(function(d) { return x(d.date) })
    .y(function(d) { return y(+d.value) });

var svg = d3.select(".content").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

// List of groups (here I have one group per column)
var partyNames = [
    "Socialdemokratiet",
    "Radikale_Venstre",
    "Det_Konservative_Folkeparti",
    "Nye_Borgerlige",
    "Klaus_Riskær_Pedersen",
    "Socialistisk_Folkeparti",
    "Veganerpartiet",
    "Liberal_Alliance",
    "Kristendemokraterne",
    "Dansk_Folkeparti",
    "Stram_Kurs",
    "Venstre",
    "Enhedslisten",
    "Alternativet"
];

var partyColors = {
    "Socialdemokratiet":"#C10B20",
    "Radikale_Venstre":"#D50080",
    "Det_Konservative_Folkeparti":"#034536",
    "Nye_Borgerlige":"#024450",
    "Klaus_Riskær_Pedersen":"#1F9FAC",
    "Socialistisk_Folkeparti":"#A40000",
    "Veganerpartiet":"#80A51A",
    "Liberal_Alliance":"#0A1B3E",
    "Kristendemokraterne":"#F5820B",
    "Dansk_Folkeparti":"#FFFF00",
    "Stram_Kurs":"#000000",
    "Venstre":"#003460",
    "Enhedslisten":"#D0004D",
    "Alternativet":"#00FF00"
};

// Process CSVs
Promise.all([
    d3.csv("../polling/mean_polls.csv"),
    d3.csv("../polling/fixed_polls.csv")
]).then(function(files) {
    var data = partyNames.map( function(partyName) { // .map allows to do something for each element of the list
        return {
            name: partyName,
            values: files[0].map(function(d) {
                return {date: parseTime(d.date), value: d[partyName], party: partyName};
            })
        };
    });

    Object.keys(data).forEach(function(d) {
        d.date = parseTime(d.date);
    });


    var cities = data.map(function(partyObject) {
        return {
            name: partyObject.name,
            values: partyObject.values.filter(d => d.value != "")
        };
    });

// Set x lim
x.domain(d3.extent(files[0], function(d) { return parseTime(d.date); }));

// Create x axis
svg.append("g")
    .attr("class", "x axis")
    .attr("transform", "translate(0," + y(0) + ")")
    .call(xAxis);

// Create y axis
svg.append("g")
    .attr("class", "y axis")
    .call(yAxis)

svg.append("text")
    .attr("transform", "rotate(-90)")
    .attr("y", 0 + (margin.left/2))
    .attr("x", 0)
    //.attr("dy", ".71em")
    .style("text-anchor", "end")
    .style("font-size", "10px")
    .text("Stemmer (%)");

var mouseG = svg.append("g")
    .attr("class", "mouse-over-effects");

// Create grey vertical line to follow mouse
mouseG.append("path") 
    .attr("class", "mouse-line")
    .style("stroke-dasharray", ("5, 5"))
    .style("stroke", "grey")
    .style("stroke-width", "1px")
    .style("opacity", 1);
    
var lines = document.getElementsByClassName("line");


mouseG.append("svg:rect") // append a rect to catch mouse movements on canvas
    .attr("width", width) // can"t catch mouse events on a g element
    .attr("height", height)
    .attr("fill", "none")
    .attr("pointer-events", "all")
    // .on("mouseout", function() { // on mouse out hide line, circles and text
    //     var mouse = d3.mouse(this);
    //     d3.selectAll(".mouse-per-line")
    //         .filter(function(d, i) {
    //             var xDate = x.invert(mouse[0]),
    //             bisect = d3.bisector(function(d) { return d.date; }).right;
    //             idx = bisect(d.values, xDate);
    //             return idx > 0;
    //         })
    //         .style("opacity", 0)
    // })
    .on("mouseover", function() { // on mouse in show line, circles and text
        d3.select(".mouse-line")
            .style("opacity", 1);
        d3.selectAll(".mouse-per-line text")
            .style("opacity", 1);
    })
    .on("mousemove", function() { // mouse moving over canvas
        var mouse = d3.mouse(this);
        var xDate = x.invert(mouse[0]); // current mouseover date
        // Draw grey vertical line to follow mouse
        d3.select(".mouse-line")
            .attr("d", function() {
                var d = "M" + mouse[0] + "," + y(0);
                d += " " + mouse[0] + "," + 0;
                return d;
            })
            .select("text")
            .text("WEOW")
            .attr("translate(" + mouse[0] + "," + pos.y +")");

        // Make party tooltips invisible
        d3.selectAll(".mouse-per-line")
            .filter(function(d, i) {
                bisect = d3.bisector(function(d) { return d.date; }).right;
                idx = bisect(d.values, xDate);
                return idx == 0;
            })
            .style("opacity", 0)
        
        var ypos = [];
        d3.selectAll(".mouse-per-line")
            .filter(function(d, i) {
                bisect = d3.bisector(function(d) { return d.date; }).right;
                idx = bisect(d.values, xDate);
                return idx > 0;
            })
            .style("opacity", 1)
            .attr("transform", function(d, i) {
                // var xDate = x.invert(mouse[0]),
                // bisect = d3.bisector(function(d) { return d.date; }).right;
                // idx = bisect(d.values, xDate);
                
                //console.log(d.name, idx);

                //console.log(d)
                //var maxIdx = Object.keys(lines[i].animatedPathSegList).length;
                //console.log(idx)
                var currentLine = document.getElementsByClassName("line " + d.name)[0];
                //console.log(currentLine)

                
                var beginning = 0,
                    end = currentLine.getTotalLength(),
                    target = null;

                while (true){
                    target = Math.floor((beginning + end) / 2);
                    pos = currentLine.getPointAtLength(target);
                    if ((target === end || target === beginning) && pos.x !== mouse[0]) {
                        break;
                    }
                    if (pos.x > mouse[0])      end = target;
                    else if (pos.x < mouse[0]) beginning = target;
                    else break; //position found
                }
                
                // Tooltip text
                d3.select(this).select("text")
                    .text(d.name.replaceAll("_", " ") + " " + y.invert(pos.y).toFixed(1) + "%")
                    .attr("class", "party-tooltip " + d.name);
                
                ypos.push({ind: i, y: pos.y, off: 0});
                    
                return "translate(" + mouse[0] + "," + pos.y +")";
            })
            .call(function(sel) {
                ypos.sort(function(a, b) { return a.y - b.y; });
                ypos.forEach (function(p, i) {
                    if (i > 0) {
                        var last = ypos[i-1].y;
                        ypos[i].off = Math.max (0, (last + 15) - ypos[i].y);
                        ypos[i].y += ypos[i].off;
                    }
                })
                ypos.sort(function(a,b) { return a.ind - b.ind; });
            })
            .select("text")
            .attr("transform", function(d, i) {
                return "translate (7,"+(ypos[i].off-5)+")";
            });
    });

// Highlight the party that is hovered
var highlightParty = function(party){
    d3.selectAll(".dot")
        .transition()
        .duration(200)
        .style("opacity", 0.1);
    d3.select(".mouse-line")
        .transition()
        .duration(200)
        .style("opacity", 1);
    d3.selectAll(".line")
        .transition()
        .duration(200)
        .style("opacity", 0.1);
    d3.selectAll(".party-tooltip")
        .transition()
        .duration(200)
        .style("opacity", 0.1);
    d3.selectAll("." + party.name)
      .transition()
      .duration(200)
      .style("opacity", 1.0);
}
// Un-highlight parties
var unhighlightParties = function(){
    d3.selectAll(".dot")
        .transition()
        .duration(200)
        .style("opacity", 0.375);
    d3.selectAll(".mouse-per-line")
        .transition()
        .duration(200)
        .style("opacity", 1.0);
    d3.selectAll(".line")
        .transition()
        .duration(200)
        .style("opacity", 1.0);
}
var city = mouseG.selectAll(".city")
    .data(cities)
    .enter().append("g");

city.append("path")
    .attr("class", function(d){
        return "line " + d.name
    })
    .attr("d", function(d) {
        return line(d.values);
    })
    .style("stroke", function(d) {
        return partyColors[d.name];
    })
    .style("stroke-width", 2.5)
    .style("fill", "none")
    .on("mouseover", highlightParty)
    .on("mouseleave", unhighlightParties);    

// Load poll data
var pollingData = partyNames.map( function(partyName) {
    return {
        name: partyName,
        values: files[1]
            .filter((d)=>{return d[partyName] != "";})
            .map(function(d) {
                return {date: parseTime(d.date), value: +d[partyName], name: partyName}
            })
    };
});

// Add the points
mouseG
    // First we need to enter in a group
    .selectAll("dot")
    .data(pollingData)
    .enter()
        .append("g")
        .style("fill", function(d){ return partyColors[d.name] })
    // Second we need to enter in the "values" part of this group
    .selectAll("myPoints")
    .data(function(d){ return d.values })
    .enter()
    .append("circle")
        .attr("class", function (d) {
            return "dot " + d.name
        })
        .attr("cx", function(d) {
            return x(d.date)
        })
        .attr("cy", function(d) {
            return y(d.value)
        })
        .attr("r", 4)
        .style("opacity", 0.375)
        .on("mouseover", highlightParty)
        .on("mouseleave", unhighlightParties);


var mousePerLine = mouseG
    .selectAll(".mouse-per-line")
    .data(cities)
    .enter()
    .append("g")
    .attr("class", function(d){
        return "mouse-per-line " + d.name
    });
    //.attr("class", "mouse-per-line");

mousePerLine.append("text")
    .style("fill", function(d) {
        return partyColors[d.name];
    });

});
