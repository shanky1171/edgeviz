document.addEventListener('DOMContentLoaded', function() {
  $(document).ready(function(){
     //curChartSampleLoad(devSelected);
     c_agg_Load(devSelected);
     c_smpl_Load(devSelected);
  });
    
  window.devSelected = 'Pump1';

  document.querySelector('#dev1').addEventListener('click',function() {
    window.devSelected = document.getElementById("dev1").getAttribute("value");
    console.log(devSelected);
  });

  document.querySelector('#dev3').addEventListener('click',function() {
    window.devSelected = document.getElementById("dev3").getAttribute("value");
    console.log(devSelected);
  });


  //var refc=setInterval(curChartSampleLoad,5000, window.devSelected);
  //var refagg=setInterval(curChartMinMaxLoad,5000);
  var p_ref_c_smpl=setInterval(c_smpl_Load,5000, window.devSelected);
  var p_ref_c_agg =setInterval(c_agg_Load, 5000, window.devSelected);


  function c_smpl_Load(devname){
      if(devname === undefined){
           devname = 'Pump1';
      };
      devname = window.devSelected;
      console.log(devname);

      var getData = $.get('/sample/current?devname='+ devname);

      getData.done(function(sample_recs){
        console.log(sample_recs);
        var rcurArr = sample_recs.sample_recs.map(element => element.current);
        curArr = rcurArr.reverse();
        console.log(curArr);
        var tsArr = sample_recs.sample_recs.map(element => element.ts.$date);
        console.log(tsArr);
        var rcnvTsArr = tsArr.map(function(element){
            var temp = new Date(parseInt(element))
            element = temp.toISOString().substring(11,19)
            return element;
        });
        cnvTsArr = rcnvTsArr.reverse();
        console.log(cnvTsArr);

	SAMPLE = document.getElementById('curSampl');
        var trace1 = {
            y: curArr,
            x: cnvTsArr,
            mode: 'lines+markers',
            name: 'Sampled',
            marker: {
              color: 'rgb(128, 0, 128)',
              size: 4
            },
            line: {
              color: 'white',
              width: 1
            }
        };
        var data = [trace1];
        var layout = {
          width: 700,
          height: 450,
          title:'Time Series-Current(' + devname +')',
          xaxis: {
            showgrid: true,
            automargin: true,
            title: 'Time'
          },
          yaxis: {
            zeroline: false,
            showgrid: true,
            automargin: true,
            title: 'Current(Amps)'
          },
          plot_bgcolor:"black",
          //paper_bgcolor:"#FFF3"
        };
	Plotly.newPlot( SAMPLE, data, layout);
     });
  }; //End of PlotlyLoad


  function c_agg_Load(devname){
    var maxCurrArr;
    var avgCurrArr;

    if(devname === undefined){
         devname = 'Pump1';
    };
    devname = window.devSelected;
    console.log(devname);

    var getMaxData = $.get('/maxData/max_current?devname='+ devname);
    getMaxData.done(function(maxData_recs){
      console.log(maxData_recs);
      rmaxCurrArr = maxData_recs.maxData_recs.map(element => element.max_current);
      maxCurrArr = rmaxCurrArr.reverse();
      console.log(maxCurrArr);
    });

    var getAvgData = $.get('/avgData/avg_current?devname='+ devname);
    getAvgData.done(function(avgData_recs){
      console.log(avgData_recs);
      ravgCurrArr = avgData_recs.avgData_recs.map(element => element.avg_current);
      avgCurrArr = ravgCurrArr.reverse()
      console.log(avgCurrArr);
    });

    var getData = $.get('/minData/min_current?devname='+ devname);
    getData.done(function(minData_recs){
      console.log(minData_recs);

      var rminCurrArr = minData_recs.minData_recs.map(element => element.min_current);
      minCurrArr = rminCurrArr.reverse();
      console.log(minCurrArr);
      var endtsArr = minData_recs.minData_recs.map(element => element.end_time.$date);
      console.log(endtsArr);

      var rcnvEndTsArr = endtsArr.map(function(element){
        var temp = new Date(parseInt(element))
        element = temp.toISOString().substring(11,19)
        return element;
      });
      cnvEndTsArr = rcnvEndTsArr.reverse()
      console.log(cnvEndTsArr);

      AGGR = document.getElementById('curAgg');
      var trace1 = {
        y: minCurrArr,
        x: cnvEndTsArr,
        mode: 'lines+markers',
        name: 'Minimum',
        marker: {
          color: 'lightgrey',
          size: 4
        },
        line: {
          color: 'lightblue',
          width: 1
        }
      };
      var trace2 = {
        y: maxCurrArr,
        x: cnvEndTsArr,
        mode: 'lines+markers',
        name: 'Maximum',
        marker: {
          color: 'lightgrey',
          size: 4
        },
        line: {
          color: 'yellow',
          width: 1
        }
      };
      var trace3 = {
        y: avgCurrArr,
        x: cnvEndTsArr,
        mode: 'lines+markers',
        name: 'Average',
        marker: {
          color: 'lightgrey',
          size: 4
        },
        line: {
          color: 'lightgreen',
          width: 1
        }
      };
      var data = [trace1,trace2,trace3];
      var layout = {
        width: 700,
        height: 450,
        title:'Tumbling Window Agg-Current(' + devname +')',
        xaxis: {
          showgrid: true,
          automargin: true,
          title: 'Time'
        },
        yaxis: {
          rangemode: 'normal',
          zeroline: false,
          showgrid: true,
          automargin: true,
          title: 'Current(Amps)'
        },
        plot_bgcolor:"black",
        //paper_bgcolor:"#FFF3"
      };
      Plotly.newPlot( AGGR, data, layout);
     });

  }; //End of PlotlyLoad

// End of Main Function 
});

/***************************************************************************************************/
/*
    function curChartSampleLoad(devname) {
      if(devname === undefined){
           devname = 'Pump1';
      };
      devname = window.devSelected;
      console.log(devname);
      var getData = $.get('/sample/current?devname='+ devname);
      getData.done(function(sample_recs){
        console.log(sample_recs);
        var rcurArr = sample_recs.sample_recs.map(element => element.current);
        curArr = rcurArr.reverse();
        console.log(curArr);
        var tsArr = sample_recs.sample_recs.map(element => element.ts.$date);
        console.log(tsArr);
        var rcnvTsArr = tsArr.map(function(element){
        var temp = new Date(parseInt(element))
        element = temp.toISOString().substring(11,19)
        return element;
        });
        cnvTsArr = rcnvTsArr.reverse();
        console.log(cnvTsArr);

        var ctx = document.getElementById('curChartSample').getContext('2d');
        var myChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: cnvTsArr,
                datasets: [{
                    label: 'Current',
                    data: curArr,
                    borderWidth: 2,
                    borderColor: 'brown',
                    backgroundColor: 'rgba(0, 0, 255, 0.1)',
                    fillOpacity: 0.3
                }]
            },
            options: {
                responsive: false,
                title:{
                  display: true,
                  text: "Current time series(" + window.devSelected + ")"
                },
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero: false
                        }
                    }]
                }
            }
        });
      });
    };

    function curChartMinMaxLoad(devname){
      var maxCurrArr;
      var avgCurrArr;

      if(devname === undefined){
           devname = 'Pump1';
      };
      devname = window.devSelected;
      console.log(devname);

      var getMaxData = $.get('/maxData/max_current?devname='+ devname);
      getMaxData.done(function(maxData_recs){
        console.log(maxData_recs);
        rmaxCurrArr = maxData_recs.maxData_recs.map(element => element.max_current);
        maxCurrArr = rmaxCurrArr.reverse();
        console.log(maxCurrArr);
      });

      var getAvgData = $.get('/avgData/avg_current?devname='+ devname);
      getAvgData.done(function(avgData_recs){
        console.log(avgData_recs);
        ravgCurrArr = avgData_recs.avgData_recs.map(element => element.avg_current);
        avgCurrArr = ravgCurrArr.reverse()
        console.log(avgCurrArr);
      });

      var getData = $.get('/minData/min_current?devname='+ devname);
      getData.done(function(minData_recs){
        console.log(minData_recs);

        var rminCurrArr = minData_recs.minData_recs.map(element => element.min_current);
        minCurrArr = rminCurrArr.reverse();
        console.log(minCurrArr);
        var endtsArr = minData_recs.minData_recs.map(element => element.end_time.$date);
        console.log(endtsArr);

        var rcnvEndTsArr = endtsArr.map(function(element){
          var temp = new Date(parseInt(element))
          element = temp.toISOString().substring(11,19)
          return element;
        });
        cnvEndTsArr = rcnvEndTsArr.reverse()
        console.log(cnvEndTsArr);

        var ctx = document.getElementById('curChartMinMax').getContext('2d');
        var myChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: cnvEndTsArr,
                datasets: [
                  {
                    label: 'MinCurrent',
                    data: minCurrArr,
                    borderWidth: 2,
                    borderColor: 'blue',
                    backgroundColor: 'rgba(0,255, 0, 0.1)',
                    fillOpacity: 0.3
                  },
                  {
                    label: 'AvgCurrent',
                    data: avgCurrArr,
                    borderWidth: 2,
                    borderColor: 'green',
                    backgroundColor: 'rgba(150,255, 0, 0.1)',
                    fillOpacity: 0.3
                  },
                  {
                    label: 'MaxCurrent',
                    data: maxCurrArr,
                    borderWidth: 2,
                    borderColor: 'red',
                    backgroundColor: 'rgba(0,255, 150, 0.1)',
                    fillOpacity: 0.3
                  }
               ]
            },
            options: {
                responsive: false,
                title:{
                  display: true,
                  text: "Aggregation Current Min/Max/Avg time series(" + window.devSelected + ")"
                },
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero: false
                        }
                    }]
                }
            }
        });
      });
    };
*/
