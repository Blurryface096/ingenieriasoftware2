BASE_URL="https://guachita-analytics.herokuapp.com/";



function enviar_evento() {
alert("DETECTÓ EL CLICK");
  data={
  	'Tipo ': 'click',
  	'URL_Actual ': 'www.guachita.com',
  	'URL_Destino ': 'www.guachita.com/home',
  	'Browser' : 'Mozilla',
  	'Plataforma': 'Win32',
  	'Language': 'en-US',
  }

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
