BASE_URL="https://guachita-analytics.herokuapp.com/";
var f = new Date();
fecha=f.getDate() + "/" + (f.getMonth() +1) + "/" + f.getFullYear()
hora=f.getHours()+":"+f.getMinutes()+":"+f.getSeconds();

tiempoactual=hora +" "fecha


function enviar_evento() {
accion= document.["GuardarEvento"].value;
  data={
  	'Tipo ': accion,
  	'URL_Actual ': document.referrer,
  	'URL_Destino ': document.URL,
    'Tipo Brower':navigator.appCodeName,
    'Producto':navigator.product,
    'Browser' : navigator.appName,
    'Modo Online':navigator.onLine,
  	'Plataforma': navigator.platform,
  	'Language': navigator.language,
    'Fecha':fecha,
    'Hora':hora
  }

  $.ajax({
    alert("entró al ajax");
    type: "POST",
    url: BASE_URL + "sendEvent/",
    data: "data=" + JSON.stringify(data),
    async: false,
    success: function (data) {
      alert("TODO OK :P");
      }
  });
};
