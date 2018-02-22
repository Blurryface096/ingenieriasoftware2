BASE_URL="https://guachita-analytics.herokuapp.com/";

var app = angular.module('analiticas', []);
app.controller('reporte1', function($scope,$http) {

  var data = [{
    values: [19, 26, 55],
    labels: ['Residential', 'Non-Residential', 'Utility'],
    type: 'pie'
  }];

  Plotly.newPlot('browsers', data);

  $http({
        method : "POST",
        url : BASE_URL + "getReport/",
    }).then(function mySuccess(response) {
      console.log(response.data)
      $scope.eventos = response.data.collection;
    }, function myError(response) {
        alert("TODO NO OK :(");
    });
});
