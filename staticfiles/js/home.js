BASE_URL="https://guachita-analytics.herokuapp.com/";
var f = new Date();
fecha=f.getDate() + "/" + (f.getMonth() +1) + "/" + f.getFullYear();
var version1=navigator.appVersion;

var division=version1.split(",");
var browser=division[1];
if(browser == undefined){
  var division=version1.split(";");
  browser=division[1];
    if(browser == undefined){
      browser='Firefox'
    }else{
        browser='Internet Explorer'
      }

}else{
browser='Chrome'
}
function enviar_evento() {
var accion=document.getElementById('GuardarEvento').getAttribute('name');

  data={
  	'Tipo': accion,
    //'Tipo ': 'Click',
  	'URL_Actual': document.URL,
  	'URL_Destino': document.referrer,
    'Browser': browser,
    'Modo Online':navigator.onLine,
  	'Plataforma': navigator.platform,
  	'Language': navigator.language,
    'Fecha':f,
    'Date': fecha
  }

  $.ajax({
    type: "POST",
    url: BASE_URL + "sendEvent/",
    data: "data=" + JSON.stringify(data),
    async: false,
    success: function (data) {
      //alert(" OK :P");
      }
  });
};
