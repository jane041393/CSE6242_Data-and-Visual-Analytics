function plot_1(data, x, y, title){
	var height = 600;
	var width = 800;
	var padding = 50;

	var xScale = d3.scale.linear()
		.domain([0, d3.max(data, (d) => d[x] )])
		.range([padding, width - 2*padding]);


	var yScale = d3.scale.linear()
		.domain([0, d3.max(data, (d) => d[y] )])
		.range([height - padding, padding]);

	var svg = d3.select("body")
				.append("svg")
				.attr("width", width)
				.attr("height", height);
	var arc = d3.svg.symbol()
				.type(function(d, i){if (d['IsGoodRating'] == 1 ){
					return d3.svg.symbolTypes[1];}
					else{
						return d3.svg.symbolTypes[0];
					}
				});
	var color = ["red","blue"];
	var legend = svg.selectAll(".legend")
		.data(color)
		.enter().append("g")
		.attr("class","legend");

	legend.filter(function(d){return d === "blue";})
		.append("path")
		.attr("class","cross")
		.attr("d", d3.svg.symbol().type("cross").size(50))
		.style("stroke","blue")
        .style("fill","none")
        .attr("transform", function() { return "translate(" + (width-60)  + "," + 10 + ")"; });

    legend.filter(function(d){ return d === "red"; })
            .append("circle")
            .attr("r", 5)
            .style("stroke","red")
            .style("fill","none")
            .attr("cx", width -60)
            .attr("cy", 30);

    legend.append("text")
            .attr("x",width-40)
            .attr("y",function(d){
                return d == "blue" ? 10 : 30;
            })
            .text(function(d){
                return d == "blue" ? "Good" : "Bad";
            })
            .attr("dy",".35em");

    svg.selectAll(".point")
           .data(data)
           .enter()
           .append("path")
           .attr("stroke", function(d) {if (d['IsGoodRating'] ==1 ){
					return "blue";}
					else{
						return "red";
					}})
           .attr("d", arc)
           .attr("fill-opacity", 0)
           .attr("transform",
            function(d) {return "translate(" + xScale(d[x]) + "," + yScale(d[y]) + ")";});


	//X-axis
	var xAxis = d3.svg.axis()
					.scale(xScale)
					.orient("bottom")
					.ticks(10);
	svg.append("g")
		.attr("class", "axis")
		.attr("transform", "translate(30, " + (height - padding) + ")")
		.call(xAxis);

	//Y-axis
	var yAxis = d3.svg.axis()
					.scale(yScale)
					.orient("left")
					.ticks(10);
	svg.append("g")
		.attr("class", "axis")
		.attr("transform", "translate(" + (padding+30) + ",0)")
		.call(yAxis);


	svg.append("text")
      .attr("x", 300)
      .attr("y", 15)
      .attr("font-size","20px")
      .text(title);

    // Axis Label
    svg.append("text")
       .attr("x", 700)
       .attr("y", 600)
       .text(x);

    svg.append("text")
       .attr("x", 15)
       .attr("y", 20)
       .text(y);

}

//---------------------------------------------------------------------------------
function plot_2(data, x, y,z, title){
	var height = 600;
	var width = 800;
	var padding = 50;

	var xScale = d3.scale.linear()
		.domain([0, d3.max(data, (d) => d[x] )])
		.range([padding, width - 2*padding]);

	var yScale = d3.scale.linear()
		.domain([0, d3.max(data, (d) => d[y] )])
		.range([height - padding, padding]);

	//console.log(d3.max(data, (d) => 1.0 / (d[x] * d[y])))
	var rScale = d3.scale.linear()
		//.domain([  d3.min(data, (d) => d[z]) , d3.max(data, (d) => d[z])])
		.domain([  0 , d3.max(data, (d) => d[z])])
		.range([20,1500]);

	var svg = d3.select("body")
				.append("svg")
				.attr("width", width)
				.attr("height", height);

	var arc = d3.svg.symbol()
				.size(function(d){return rScale(d[z]); })
				.type(function(d, i){if (d['IsGoodRating'] == 1 ){
					return d3.svg.symbolTypes[1];}
					else{
						return d3.svg.symbolTypes[0];
					}
				});
	var color = ["red","blue"];
	var legend = svg.selectAll(".legend")
		.data(color)
		.enter().append("g")
		.attr("class","legend");

	legend.filter(function(d){return d === "blue";})
		.append("path")
		.attr("class","cross")
		.attr("d", d3.svg.symbol().type("cross").size(50))
		.style("stroke","blue")
        .style("fill","none")
        .attr("transform", function() { return "translate(" + (width-60)  + "," + 10 + ")"; });

    legend.filter(function(d){ return d === "red"; })
            .append("circle")
            .attr("r", 5)
            .style("stroke","red")
            .style("fill","none")
            .attr("cx", width -60)
            .attr("cy", 30);

    legend.append("text")
            .attr("x",width-40)
            .attr("y",function(d){
                return d == "blue" ? 10 : 30;
            })
            .text(function(d){
                return d == "blue" ? "Good" : "Bad";
            })
            .attr("dy",".35em");

    svg.selectAll(".point")
           .data(data)
           .enter()
           .append("path")
           .attr("stroke", function(d) {if (d['IsGoodRating'] ==1 ){
					return "blue";}
					else{
						return "red";
					}})
           .attr("d", arc)
           .attr("fill-opacity", 0)
           .attr("transform",
            function(d) {return "translate(" + xScale(d[x]) + "," + yScale(d[y]) + ")";});


	//X-axis
	var xAxis = d3.svg.axis()
					.scale(xScale)
					.orient("bottom")
					.ticks(10);
	svg.append("g")
		.attr("class", "axis")
		.attr("transform", "translate(30, " + (height - padding) + ")")
		.call(xAxis);

	//Y-axis
	var yAxis = d3.svg.axis()
					.scale(yScale)
					.orient("left")
					.ticks(10);
	svg.append("g")
		.attr("class", "axis")
		.attr("transform", "translate(" + (padding+30) + ",0)")
		.call(yAxis);


	svg.append("text")
      .attr("x", 250)
      .attr("y", 15)
      .attr("font-size","20px")
      .text(title);

    // Axis Label
    svg.append("text")
       .attr("x", 700)
       .attr("y", 600)
       .text(x);

    svg.append("text")
       .attr("x", 15)
       .attr("y", 20)
       .text(y);

}


//---------------------------------------------------------------------------------
function plot_3(data, x, y, method, title){
	var height = 600;
	var width = 800;
	var padding = 50;

	var xScale = d3.scale.linear()
		.domain([0, d3.max(data, (d) => d[x] )])
		.range([padding, width - 2*padding]);

	var yScale = d3.scale.linear()
		.domain([0, d3.max(data, (d) => d[y] )])
		.range([height - padding, padding]);

	if(method == "square"){
		var yScale = d3.scale.sqrt()
			.domain([0, d3.max(data, (d) => d[y] )])
			.range([height - padding, padding]);
	}
	if (method == "log"){
		var yScale = d3.scale.log()
			.domain([0.1, d3.max(data, (d) => d[y] )])
			.range([height - padding, padding]);
	}



	var svg = d3.select("body")
				.append("svg")
				.attr("width", width)
				.attr("height", height);

	var arc = d3.svg.symbol()
				.type(function(d, i){if (d['IsGoodRating'] == 1 ){
					return d3.svg.symbolTypes[1];}
					else{
						return d3.svg.symbolTypes[0];
					}
				});
	var color = ["red","blue"];
	var legend = svg.selectAll(".legend")
		.data(color)
		.enter().append("g")
		.attr("class","legend");

	legend.filter(function(d){return d === "blue";})
		.append("path")
		.attr("class","cross")
		.attr("d", d3.svg.symbol().type("cross").size(50))
		.style("stroke","blue")
        .style("fill","none")
        .attr("transform", function() { return "translate(" + (width-60)  + "," + 10 + ")"; });

    legend.filter(function(d){ return d === "red"; })
            .append("circle")
            .attr("r", 5)
            .style("stroke","red")
            .style("fill","none")
            .attr("cx", width -60)
            .attr("cy", 30);

    legend.append("text")
            .attr("x",width-40)
            .attr("y",function(d){
                return d == "blue" ? 10 : 30;
            })
            .text(function(d){
                return d == "blue" ? "Good" : "Bad";
            })
            .attr("dy",".35em");

    svg.selectAll(".point")
           .data(data)
           .enter()
           .append("path")
           .attr("stroke", function(d) {if (d['IsGoodRating'] ==1 ){
					return "blue";}
					else{
						return "red";
					}})
           .attr("d", arc)
           .attr("fill-opacity", 0)
           .attr("transform",
            function(d) {return "translate(" + xScale(d[x]) + "," + yScale(d[y]) + ")";});


	//X-axis
	var xAxis = d3.svg.axis()
					.scale(xScale)
					.orient("bottom")
					.ticks(10);
	svg.append("g")
		.attr("class", "axis")
		.attr("transform", "translate(30, " + (height - padding) + ")")
		.call(xAxis);

	//Y-axis
	var yAxis = d3.svg.axis()
					.scale(yScale)
					.orient("left")
					.ticks(10);
	svg.append("g")
		.attr("class", "axis")
		.attr("transform", "translate(" + (padding+30) + ",0)")
		.call(yAxis);


	svg.append("text")
      .attr("x", 250)
      .attr("y", 15)
      .attr("font-size","20px")
      .text(title);

    // Axis Label
    svg.append("text")
       .attr("x", 700)
       .attr("y", 600)
       .text(x);

    svg.append("text")
       .attr("x", 15)
       .attr("y", 20)
       .text(y);

}


