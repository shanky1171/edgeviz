document.addEventListener('DOMContentLoaded', function() {
  $(document).ready(function(){
     tChartLoad();
     hChartLoad();
     pChartLoad();
  });

 setInterval(tChartLoad(),5000);

    document.getElementById("tbutton").onclick = function() {tChartLoad()};
    document.getElementById("hbutton").onclick = function() {hChartLoad()};
    document.getElementById("pbutton").onclick = function() {pChartLoad()};

    function tChartLoad() {
      var getData = $.get('/tdata');
      getData.done(function(temprecs){
        //console.log(temprecs);
        var tempArr = temprecs.temprecs.map(element => element.temp);
        console.log(tempArr);
        var tsArr = temprecs.temprecs.map(element => element.ts.$date);
        //console.log(tsArr);
        var cnvTsArr = tsArr.map(function(element){
        var temp = new Date(parseInt(element))
        element = temp.toISOString().substring(11,19)
        return element;
        });
        console.log(cnvTsArr);

        var ctx = document.getElementById('tChart').getContext('2d');
        var myChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: cnvTsArr,
                datasets: [{
                    label: 'Temperature',
                    data: tempArr,
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
                  text: "Temparature time series(Last 1 hr)"
                },
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero: true
                        }
                    }]
                }
            }
        });
      });
    };

    function hChartLoad(){
      var getData = $.get('/hdata');
      getData.done(function(humrecs){
        //console.log(humrecs);

        var humArr = humrecs.humrecs.map(element => element.humidity);
        console.log(humArr);
        var tsArr = humrecs.humrecs.map(element => element.ts.$date);
        //console.log(tsArr);

        var cnvTsArr = tsArr.map(function(element){
          var temp = new Date(parseInt(element))
          element = temp.toISOString().substring(11,19)
          return element;
        });
        console.log(cnvTsArr);

        var ctx = document.getElementById('hChart').getContext('2d');
        var myChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: cnvTsArr,
                datasets: [{
                    label: 'Humidity',
                    data: humArr,
                    borderWidth: 2,
                    borderColor: 'blue',
                    backgroundColor: 'rgba(0,255, 0, 0.1)',
                    fillOpacity: 0.3
                }]
            },
            options: {
                responsive: false,
                title:{
                  display: true,
                  text: "Humidity time series(Last 1 hr)"
                },
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero: true
                        }
                    }]
                }
            }
        });
      });
    };

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
                            beginAtZero: true
                        }
                    }]
                }
            }
        });
      });
    };
});
