BASE_URL="https://guachita-analytics.herokuapp.com/";
var f = new Date();
fecha=f.getDate() + "/" + (f.getMonth() +1) + "/" + f.getFullYear();
hora=f.getHours()+":"+f.getMinutes()+":"+f.getSeconds();
var version=navigator.appVersion;

var division=split(",");
var browser=split[2];



function enviar_evento() {
//var accion=document["GuardarEvento"].value;
  data={
  	//'Tipo ': accion,
    'Tipo ': 'Click',
  	'URL_Actual ': document.URL,
  	'URL_Destino ': document.referrer,
    'Browser': browser,
    'Modo Online':navigator.onLine,
  	'Plataforma': navigator.platform,
  	'Language': navigator.language,
    'Fecha':fecha,
    'Hora':hora
  }


console.log(data);

  $.ajax({
    type: "POST",
    url: BASE_URL + "sendEvent/",
    data: "data=" + JSON.stringify(data),
    async: false,
    success: function (data) {
      alert("TODO OK :P");
      }
  });
};
