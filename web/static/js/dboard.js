document.addEventListener('DOMContentLoaded', function() {
  $(document).ready(function(){
     curChartSampleLoad();
     curChartMinMaxLoad();
     //curCharAvgLoad();
  });

 setInterval(curChartSampleLoad(),5000);

    document.getElementById("tbutton").onclick = function() {curChartSampleLoad()};
    document.getElementById("hbutton").onclick = function() {curChartMinMaxLoad()};
    //document.getElementById("pbutton").onclick = function() {pChartLoad()};

    function curChartSampleLoad() {
      var getData = $.get('/sample/current');
      getData.done(function(sample_recs){
        console.log(sample_recs);
        var curArr = sample_recs.sample_recs.map(element => element.current);
        console.log(curArr);
        var tsArr = sample_recs.sample_recs.map(element => element.ts.$date);
        console.log(tsArr);
        var cnvTsArr = tsArr.map(function(element){
        var temp = new Date(parseInt(element))
        element = temp.toISOString().substring(11,19)
        return element;
        });
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
                  text: "Current time series"
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

    function curChartMinMaxLoad(){
      var maxCurrArr;
      var avgCurrArr;

      var getMaxData = $.get('/maxData/max_current');
      getMaxData.done(function(maxData_recs){
        console.log(maxData_recs);
        maxCurrArr = maxData_recs.maxData_recs.map(element => element.max_current);
        console.log(maxCurrArr);
      });

      var getAvgData = $.get('/avgData/avg_current');
      getAvgData.done(function(avgData_recs){
        console.log(avgData_recs);
        avgCurrArr = avgData_recs.avgData_recs.map(element => element.avg_current);
        console.log(avgCurrArr);
      });

      var getData = $.get('/minData/min_current');
      getData.done(function(minData_recs){
        console.log(minData_recs);

        var minCurrArr = minData_recs.minData_recs.map(element => element.min_current);
        console.log(minCurrArr);
        var endtsArr = minData_recs.minData_recs.map(element => element.end_time.$date);
        console.log(endtsArr);

        var cnvEndTsArr = endtsArr.map(function(element){
          var temp = new Date(parseInt(element))
          element = temp.toISOString().substring(11,19)
          return element;
        });
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
                  text: "Aggregation Current Min/Max/Avg time series"
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

/*
    function pChartLoad(){
      var getData = $.get('/pdata');
      getData.done(function(presrecs){
        //console.log(presrecs);

        var presArr = presrecs.presrecs.map(element => element.pressure);
        console.log(presArr);
        var tsArr = presrecs.presrecs.map(element => element.ts.$date);
        //console.log(tsArr);

        var cnvTsArr = tsArr.map(function(element){
        var temp = new Date(parseInt(element))
        element = temp.toISOString().substring(11,19)
        return element;
        });
        console.log(cnvTsArr);

        var ctx = document.getElementById('pChart').getContext('2d');
        var myChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: cnvTsArr,
                datasets: [{
                    label: 'Pressure',
                    data: presArr,
                    borderWidth: 2,
                    borderColor: 'green',
                    backgroundColor: 'rgba(255, 0, 0, 0.1)',
                    fillOpacity: 0.3
                }]
            },
            options: {
                responsive: false,
                title:{
                  display: true,
                  text: "Pressure time series(Last 1 hr)"
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
});
