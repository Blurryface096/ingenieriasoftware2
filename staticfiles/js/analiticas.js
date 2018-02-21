BASE_URL="https://guachita-analytics.herokuapp.com/";

var app = angular.module('analiticas', []);
app.controller('reporte1', function($scope,$http) {


  $http({
        method : "POST",
        url : BASE_URL + "getReport/",
    }).then(function mySuccess(response) {
        console.log(response.data);
        $scope.eventos = response.data.json_report;
    }, function myError(response) {
        alert("TODO NO OK :(");
    });
});
