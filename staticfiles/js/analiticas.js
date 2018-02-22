BASE_URL="https://guachita-analytics.herokuapp.com/";

var app = angular.module('analiticas', []);
app.controller('reporte1', function($scope,$http) {

  $http({
        method : "POST",
        url : BASE_URL + "getReport/",
    }).then(function mySuccess(response) {
      $scope.eventos = response.data.collection;
      chromes=0
      firefox=0
      safari=0

      win=0
      linux=0
      mac=0

      for (var i = 0; i < response.data.collection.length; i++) {
        evento = $scope.eventos[i]
        if (evento.Browser=='Chrome') {
          chromes=chromes+1
        } else if (evento.Browser=='Firefox') {
          firefox=firefox+1
        } else {
          safari=safari+1
        }

        if(evento.Plataforma=='Win32'){
          win=win+1
        } else if (evento.Plataforma=='Linux x86_64') {
          linux=linux+1
        } else {
          mac=mac+1
        }
      }
      total = chromes + firefox + safari
      chr = chromes/total
      fire = firefox/total
      safa = safari/total

      total2=win+linux+mac
      w=win/total2
      l=linux/total2
      m=mac/total2

      var data = [{
        values: [chr, fire, safa],
        labels: ['Chrome', 'Firefox', 'Otros'],
        type: 'pie'
      }];

      var data2 = [{
        values: [l, w, m],
        labels: ['Linux', 'Windows', 'Otros'],
        type: 'pie'
      }];

      var layout = {
        title: 'Navegadores que usan nuestros visitantes',
      };

      var layout2 = {
        title: 'Plataformas desde las que se conectan nuestros visitantes', 
      };
      Plotly.newPlot('browsers', data, layout);
      Plotly.newPlot('plataformas', data2, layout2);

    }, function myError(response) {
        alert("TODO NO OK :(");
    });

    $http({
        method : "POST",
        url : BASE_URL + "getVistasDiarias/",
    }).then(function mySuccess(response) {
      var raw = response.data.visitas
      var x  = []
      var y = []
      for (var i = 0; i < raw.length; i++) {
        r = raw[i]
        x.push(r._id)
        y.push(r.total)
      }
      var data3 = [{
          x: x,
          y: y,
          type: 'scatter'
        }
      ];
      var layout = {
        title: 'Cantidad de visitas por dia',
      };
      Plotly.newPlot('visitas', data3, layout);
    }, function myError(response) {
        alert("TODO NO OK :(");
    });
});
