$(function(){
     $(".button-collapse").sideNav();

     var slctCine= $("#slc-cine"),
         slcDia= $("#slc-dia"),
         txtHorario= $("#txt-horario"),
         ctnHorario= $("#ctn-horario");

     if(slctCine && slcDia){
          slctCine.on("change", function(){
             var $this= $(this),
                 idCine= $this.val(),
                 idPelicula= $this.data("id");

             if(idCine != ''){
                  ctnHorario.html("");
                  $.ajax({
                      "url": "/api/cartelera/" + idCine + "/" + idPelicula,
                      "success": function(json){
                         slcDia.html("");
                         if(json.data.length > 0){
                              for (i = 0; i < json.data.length; i++) {
                                   var el= json.data[i];
                                   slcDia.append("<option value='" + el.fecha + "'>" + el.fecha + "</option>")
                              }
                              slcDia.trigger("change");
                         }else{
                              slcDia.append("<option value=''>Seleccione el día</option>");
                              txtHorario.html("No hay horarios disponibles");
                         }
                      }
                  });
             }
          });
          slctCine.trigger("change");

          slcDia.on("change", function () {
               var $this= $(this),
                   idCine= slctCine.val(),
                   idPelicula= slctCine.data("id"),
                   dia= $this.val();

               if(dia != ''){
                    $.ajax({
                      "url": "/api/cartelera/" + idCine + "/" + idPelicula + "/" + dia,
                      "success": function(json){
                         if(json.data.length > 0){
                              txtHorario.html("Horarios");
                              ctnHorario.html("");
                              for (i = 0; i < json.data.length; i++) {
                                   var el= json.data[i],
                                       hora= el.hora.substr(0,5);
                                   ctnHorario.append("<span class='horario-dis'>" + hora + "</span>")
                              }
                         }
                      }
                  });
               }
          });
     }
});