BASE_URL="https://guachita-analytics.herokuapp.com/";

var app = angular.module('analiticas', []);
app.controller('reporte1', function($scope,$http) {

  $http({
        method : "POST",
        url : BASE_URL + "getReport/",
    }).then(function mySuccess(response) {
      console.log(response.data)
      $scope.eventos = response.data.collection;
      chromes=0
      firefox=0
      safari=0
      for (var i = 0; i < response.data.collection.length; i++) {
        evento = $scope.eventos[i]
        if (evento.Browser=='Chrome') {
          chromes=chromes+1
        } else if (evento.Browser=='Firefox') {
          firefox=firefox+1
        } else {
          safari=safari+1
        }
      }
      total = chromes + firefox + safari
      chr = chromes/total
      fire = firefox/total
      safa = safari/total
      var data = [{
        values: [chr, fire, safa],
        labels: ['Chrome', 'Firefox', 'Otros'],
        type: 'pie'
      }];

      Plotly.newPlot('browsers', data);


    }, function myError(response) {
        alert("TODO NO OK :(");
    });
});
