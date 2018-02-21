BASE_URL="https://guachita-analytics.herokuapp.com/";

var app = angular.module('analiticas', []);
app.controller('reporte1', function($scope, $http) {
  $http({
        method : "POST",
        url : BASE_URL + "getReport/",
    }).then(function mySuccess(response) {
        var even = []
        for (var i = 0; i < response.data.collection.length; i++) {
          console.log(response.data.collection[i])
          even.append(response.data.collection[i])
        }
        $scope.eventos = even
    }, function myError(response) {
        alert("TODO NO OK :(");
    });
});
