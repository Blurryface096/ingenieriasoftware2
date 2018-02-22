BASE_URL="https://guachita-analytics.herokuapp.com/";

var app = angular.module('analiticas', []);
app.controller('reporte1', function($scope,$http) {
  $http({
        method : "POST",
        url : BASE_URL + "getReport/",
    }).then(function mySuccess(response) {
        var eventos = []
        for (var i = 0; i < response.data.collection.length; i++) {
          raw = response.data.collection[i]
          var d = Date.parse(raw.Fecha);
          evento = {
            'Tipo' : raw.Tipo,
            'Browser' : raw.Browser,
            'URL_Actual' : raw.URL_Actual,
            'URL_Destino' : raw.URL_Destino,
            'Plataforma' : raw.Plataforma,
            'Fecha' : d,
          }
          eventos.push(evento)
        }
        $scope.eventos = eventos;
    }, function myError(response) {
        alert("TODO NO OK :(");
    });
});
