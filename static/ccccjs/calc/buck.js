///////////////////////////////
// BUCK
///////////////////////////////

var carga_buck, carga_manual_buck, contas_buck, handle_check_buck, play_buck, carga_nova;

carga_buck = 0;

carga_manual_buck = "null";

handle_check_buck = function() {
    var estado;
    estado = $("#check_load_buck").is(':checked');
    if (!estado) {
    $("#carga_tag_buck").html("Load (&Omega;): " + carga_buck.toFixed(2) + " <input id='check_load_buck' type='checkbox' onclick='handle_check_buck()'>");
} else {
    $("#carga_tag_buck").html("Load (&Omega;): <input type='text' style='width: 50px;' value='" + carga_manual_buck + "' id='carga_manual_buck' onkeydown='if (event.keyCode == 13) play_buck()'> <input id='check_load_buck' type='checkbox' checked='true' onclick='handle_check_buck()'>");
}
};

contas_buck = function(entrada_buck, saida_buck, frequencia_buck, potencia_buck, delta_i, delta_v) {
    this.q = saida_buck / entrada_buck;
    this.D = this.q;
    this.T = 1 / (frequencia_buck * 1000);
    this.ton = this.T * this.q;
    this.Io = potencia_buck / saida_buck;
    this.Lo = (entrada_buck-saida_buck)*this.ton/((delta_i / 100) * this.Io);
    this.delta_i = delta_i;
    this.capacitancia = entrada_buck / (31 * this.Lo * frequencia_buck * 1000 * frequencia_buck * 1000 * delta_v / 100 * saida_buck);
    this.Lcri = (entrada_buck-saida_buck)*this.ton/(2*this.Io);
    this.Ilmed = ((entrada_buck - saida_buck) * this.q) / frequencia_buck * 1000 * 2 * this.Lo;
    this.critico = ((this.D * this.D) / 2) * ((1 / this.D) - 1);
    this.Iocrit = ((delta_i / 100) * this.Io)/2;
    carga_buck = saida_buck * saida_buck / potencia_buck;
};

play_buck = function() {
    var i3_plot, si, t, step_plot, j, Ggo, Gdo, wo, Q, funcao, D, buck, carga_ponto, cond, d1_plot, d2_plot, d3_plot, data, delta_i, delta_v, denominador, entrada_buck, f_plot, fase, frequencia_buck, g_plot, ganho_ponto, i1_plot, i2_plot, imaginaria, k, options, pico, plot, ponto, potencia_buck, real, saida, saida_buck, tcorte, tensao_saida_buck, v_carga;


///////////////////////////////
//passa var to django
//////////////////////////////
    
    kp = parseFloat($("#ganhokp").val());   
    kh = parseFloat($("#ganhoh").val());

   

    nc2 = parseFloat($("#numc2").val());
    nc1 = parseFloat($("#numc1").val());
    nc0 = parseFloat($("#numc0").val());

    dc2 = parseFloat($("#denc2").val());
    dc1 = parseFloat($("#denc1").val());
    dc0 = parseFloat($("#denc0").val());


    Phase_Mar = parseFloat($("#Phase_Mar").val());
    Freq_cruz = parseFloat($("#Freq_cruz").val());
    

    





    function getCookie(name) {
       var cookieValue = null;
       if (document.cookie && document.cookie != '') {
         var cookies = document.cookie.split(';');
         for (var i = 0; i < cookies.length; i++) {
         var cookie = jQuery.trim(cookies[i]);
         // Does this cookie string begin with the name we want?
         if (cookie.substring(0, name.length + 1) == (name + '=')) {
             cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
             break;
          }
     }
 }
 return cookieValue;
}


 var csrftoken = getCookie('csrftoken');
 var checkBox = document.getElementById("myCheck_PI");
 if (checkBox.checked == true){
    var PI_ON=1;
  } else {
   var PI_ON=0;
  }
 

///////////////////////////////
// CHAMA O TEMPO
///////////////////////////////

$("#teste").css('width', "0%");
setTimeout((function() {
    $("#teste1").css('display', "none");
}), 300);
setTimeout((function() {
    $("#teste").css('width', "100%");
}), 0);
$("#teste1").css('display', "block");
grava_cookies();

///////////////////////////////
// LÊ VARIÁVEIS
/////////////////////////////// 

entrada_buck = parseFloat($("#entrada_buck").val());
saida_buck = parseFloat($("#saida_buck").val());
frequencia_buck = parseFloat($("#frequencia_buck").val());
potencia_buck = parseFloat($("#potencia_buck").val());
delta_v = parseFloat($("#delta_v_buck").val());
delta_i = parseFloat($("#delta_i_buck").val());

if(saida_buck>entrada_buck) {
    alert('Output must be smaller than input!')
    return false;
}

///////////////////////////////
// MODO DE CONDUÇÃO
///////////////////////////////

buck = new contas_buck(entrada_buck, saida_buck, frequencia_buck, potencia_buck, delta_i, delta_v);
//  k = (buck.Io * buck.Lo) / (entrada_buck * buck.T);
if ($("#check_load_buck").is(':checked')) {
    carga_buck = parseFloat($("#carga_manual_buck").val());
    buck.Io = saida_buck / carga_buck;
    carga_manual_buck = carga_buck;
//    k = (buck.Io * buck.Lo) / (entrada_buck * buck.T);
}
k = (buck.Io * buck.Lo) / (entrada_buck * buck.T);
D = buck.q;


/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//This is the Ajax post.Observe carefully. It is nothing but details of where_to_post,what_to_post
 
 $.ajax({
         url : window.location.href, // the endpoint,commonly same url
         type : "POST", // http method
         data : { csrfmiddlewaretoken : csrftoken,
         Vi : entrada_buck, 
         Ro : carga_buck,
         C : buck.capacitancia,
         L : buck.Lo,  
         kp : kp,
         kh : kh,
         nc2 : nc2,
         nc1 : nc1,
         nc0 : nc0,
         dc2 : dc2,
         dc1 : dc1,
         dc0 : dc0,
         Phase_Mar : Phase_Mar,
         Freq_cruz : Freq_cruz,
         PI_ON : PI_ON
        
                 
 }, // data sent with the post request

 // handle a successful response
 success : function(dadinho) {
      
      //objectName["propertyName"]
      planta_magnitude = dadinho["planta_magnitude"];
      //controle_magnitude =  dadinho["controle_magnitude"];
      MF_magnitude = dadinho["MF_magnitude"];
      planta_fase = dadinho["planta_fase"];
      //controle_fase = dadinho["controle_fase"];
      MF_fase = dadinho["MF_fase"];

      Resistor = dadinho["Ro"]
      PI_liga = dadinho["PI_ON"]
      
      Step_dados = dadinho["Step"]
      Step = JSON.parse(Step_dados)

      Impulse_dados = dadinho["Impulse"]
      Impulse = JSON.parse(Impulse_dados)
      
      Polos_Zeros=dadinho["Polos"]
      Polos = JSON.parse(Polos_Zeros)

      Pontos_LGR_MF = dadinho["LGR_MF"]
      LGR_MF = JSON.parse(Pontos_LGR_MF)
      Pontos_LGR_MA = dadinho["LGR_MA"]
      LGR_MA = JSON.parse(Pontos_LGR_MA)

      console.log(Step[2]); // another sanity check

      var magnitude = document.getElementById("myMag_p");
      var magChart = new Chart(magnitude, {
            type: 'line',
            data: {
                datasets: [{
                    label: 'G(s) - Magnitude',
                    borderColor: "rgb(30,144,255)",
                    backgroundColor: "rgba(255,255,255,0.4)",
                    lineTension: 0.1,
                    data: JSON.parse(planta_magnitude)
                }
                ]
            },
            options: {
                scales: {
                    xAxes: [{
                        type: 'logarithmic',
                        position: 'bottom'
                    }],
                    yAxes: [{
                        type: 'logarithmic'
                    }]
                },
                showLines: true,
                responsive: false,
                maintainAspectRatio: false,
                tooltips: {
                    enabled: true,
                    mode: 'single',
                    callbacks: {
                        title: function (tooltipItem, data) { return  'Diagrama de Ganho' },
                        beforeLabel: function(tooltipItems, data) { return  'Magnitude: ' + tooltipItems.yLabel.toFixed(3) },
                        label: function(tooltipItems, data) { return  'Frequência: ' + tooltipItems.xLabel.toFixed(3) }
                    }
                },
            }
        });

        var fase = document.getElementById("myFase_p");
        var phaseChart = new Chart(fase, {
            type: 'line',
            data: {
                datasets: [{
                    label: 'G(s) - Fase',
                    borderColor: "red",
                    backgroundColor: "rgba(255,255,255,0.4)",
                    lineTension: 0.1,
                    data: JSON.parse(planta_fase)
                }
                
                ]
            },
            options: {
                scales: {
                    xAxes: [{
                        type: 'logarithmic',
                        position: 'bottom'
                    }],
                    yAxes: [{
                        type: 'linear'
                    }]
                },
                showLines: true,
                responsive: false,
                maintainAspectRatio: false,
                tooltips: {
                    enabled: true,
                    mode: 'single',
                    callbacks: {
                        title: function (tooltipItem, data) { return  'Diagrama de Fase' },
                        beforeLabel: function(tooltipItems, data) { return  'Fase: ' + tooltipItems.yLabel.toFixed(3) },
                        label: function(tooltipItems, data) { return  'Frequência: ' + tooltipItems.xLabel.toFixed(3) }
                    }
                },
            }
        });


      var magnitude = document.getElementById("myMag_c");
      var magChart = new Chart(magnitude, {
            type: 'line',
            data: {
                datasets: [{
                    label: 'G(s) - Magnitude',
                    borderColor: "rgb(30,144,255)",
                    backgroundColor: "rgba(255,255,255,0.4)",
                    lineTension: 0.1,
                    data: JSON.parse(MF_magnitude)
                }
                ]
            },
            options: {
                scales: {
                    xAxes: [{
                        type: 'logarithmic',
                        position: 'bottom'
                    }],
                    yAxes: [{
                        type: 'logarithmic'
                    }]
                },
                showLines: true,
                responsive: false,
                maintainAspectRatio: false,
                tooltips: {
                    enabled: true,
                    mode: 'single',
                    callbacks: {
                        title: function (tooltipItem, data) { return  'Diagrama de Ganho' },
                        beforeLabel: function(tooltipItems, data) { return  'Magnitude: ' + tooltipItems.yLabel.toFixed(3) },
                        label: function(tooltipItems, data) { return  'Frequência: ' + tooltipItems.xLabel.toFixed(3) }
                    }
                },
            }
        });

        var fase = document.getElementById("myFase_c");
        var phaseChart = new Chart(fase, {
            type: 'line',
            data: {
                datasets: [{
                    label: 'G(s) - Fase',
                    borderColor: "red",
                    backgroundColor: "rgba(255,255,255,0.4)",
                    lineTension: 0.1,
                    data: JSON.parse(MF_fase)
                }]
            },
            options: {
                scales: {
                    xAxes: [{
                        type: 'logarithmic',
                        position: 'bottom'
                    }],
                    yAxes: [{
                        type: 'linear'
                    }]
                },
                showLines: true,
                responsive: false,
                maintainAspectRatio: false,
                tooltips: {
                    enabled: true,
                    mode: 'single',
                    callbacks: {
                        title: function (tooltipItem, data) { return  'Diagrama de Fase' },
                        beforeLabel: function(tooltipItems, data) { return  'Fase: ' + tooltipItems.yLabel.toFixed(3) },
                        label: function(tooltipItems, data) { return  'Frequência: ' + tooltipItems.xLabel.toFixed(3) }
                    }
                },
            }
        });

        
    
        var pzmap = document.getElementById("myPZmap");
        var pzChat = new Chart(pzmap, {
            type: 'line',
            data: {
                datasets: [{
                    label: 'Polos',
                    pointStyle: "crossRot",
                    pointRadius: 7,
                    borderColor: "rgb(30,144,255)",
                    backgroundColor: "rgba(255,255,255,0.4)",
                    lineTension: 0.1,
                    data: Polos[0]
                },
                {
                    label: 'Eixo',
                    borderColor: "green",
                    pointRadius: 0,
                    backgroundColor: "rgba(255,255,255,0.4)",
                    lineTension: 0.1,
                    data: [{"y": 0, "x": 0}],
                    legend: {
                        display: false,
                    }
                },
                {
                    label: 'Zeros',
                    borderColor: "red",
                    pointRadius: 5,
                    backgroundColor: "rgba(255,255,255,0.4)",
                    lineTension: 0.1,
                    data: Polos[1]
                }

                ]
            },
            options: {
                scales: {
                    xAxes: [{
                        type: 'linear',
                        position: 'bottom'
                    }]
                },
                showLines: false,
                legend: {
                    display: false,
                },
                responsive: false,
                maintainAspectRatio: false,
                tooltips: {
                    enabled: true,
                    mode: 'single',
                    callbacks: {
                        title: function (tooltipItem, data) { return  'Localização' },
                        beforeLabel: function(tooltipItems, data) { return  'Im: ' + tooltipItems.yLabel.toFixed(3) },
                        label: function(tooltipItems, data) { return  'Re: ' + tooltipItems.xLabel.toFixed(3) }
                    }
                },
            }
        });

        var LGR_plot = document.getElementById("myLGR");   

        if (LGR_MF[1] == null) {
            LGR_MF[1] = [{"y": 0, "x": 0}];
        }
        if (LGR_MF[2] == null) {
            LGR_MF[2] = [{"y": 0, "x": 0}];
        }
        if (LGR_MF[3] == null) {
            LGR_MF[3] = [{"y": 0, "x": 0}];
        }
        if (LGR_MF[4] == null) {
            LGR_MF[4] = [{"y": 0, "x": 0}];
        }

        var LGRChart = new Chart(LGR_plot, {
            type: 'line',
            data: {
                datasets: [{
                    label: 'Polos',
                    borderColor: "rgb(30,144,255)",
                    backgroundColor: "rgba(255,255,255,0.4)",
                    lineTension: 0.1,
                    data: LGR_MF[0],
                    pointRadius: 0,
                },
                {
                    label: 'Eixo',
                    borderColor: "green",
                    pointRadius: 0,
                    backgroundColor: "rgba(255,255,255,0.4)",
                    lineTension: 0.1,
                    data: [{"y": 0, "x": 0}],
                },
                {
                    label: 'Polos',
                    borderColor: "red",
                    backgroundColor: "rgba(255,255,255,0.4)",
                    lineTension: 0.1,
                    data: LGR_MF[1],
                    pointRadius: 0,
                },
                {
                    label: 'Polos',
                    borderColor: "green",
                    backgroundColor: "rgba(255,255,255,0.4)",
                    lineTension: 0.1,
                    data: LGR_MF[2],
                    pointRadius: 0,
                },
                {
                    label: 'Polos',
                    borderColor: "purple",
                    backgroundColor: "rgba(255,255,255,0.4)",
                    lineTension: 0.1,
                    data: LGR_MF[3],
                    pointRadius: 0,
                },
                {
                    label: 'Polos',
                    borderColor: "yellow",
                    backgroundColor: "rgba(255,255,255,0.4)",
                    lineTension: 0.1,
                    data: LGR_MF[4],
                    pointRadius: 0,
                }
                ]
            },
            options: {
                scales: {
                    xAxes: [{
                        type: 'linear',
                        position: 'bottom'
                    }]
                },
                legend: {
                    display: false,
                },
                showLines: true,
                responsive: false,
                maintainAspectRatio: false,
                pointDotRadius  : 0,
                tooltips: {
                    enabled: false,
                    mode: 'single',
                    callbacks: {
                        title: function (tooltipItem, data) { return  'Resposta ao Degrau' },
                        beforeLabel: function(tooltipItems, data) { return  'Amplitude: ' + tooltipItems.yLabel.toFixed(3) },
                        label: function(tooltipItems, data) { return  'Tempo: ' + tooltipItems.xLabel.toFixed(3) }
                    }
                },
            }
        });



        var LGR_plot_MA = document.getElementById("myLGR_MA");   

        if (LGR_MA[1] == null) {
            LGR_MA[1] = [{"y": 0, "x": 0}];
        }
        if (LGR_MA[2] == null) {
            LGR_MA[2] = [{"y": 0, "x": 0}];
        }
        if (LGR_MA[3] == null) {
            LGR_MA[3] = [{"y": 0, "x": 0}];
        }
        if (LGR_MA[4] == null) {
            LGR_MA[4] = [{"y": 0, "x": 0}];
        }

        var LGRChart_MA = new Chart(LGR_plot_MA, {
            type: 'line',
            data: {
                datasets: [{
                    label: 'Polos',
                    borderColor: "rgb(30,144,255)",
                    backgroundColor: "rgba(255,255,255,0.4)",
                    lineTension: 0.1,
                    data: LGR_MA[0],
                    pointRadius: 0,
                },
                {
                    label: 'Eixo',
                    borderColor: "green",
                    pointRadius: 0,
                    backgroundColor: "rgba(255,255,255,0.4)",
                    lineTension: 0.1,
                    data: [{"y": 0, "x": 0}],
                },
                {
                    label: 'Polos',
                    borderColor: "red",
                    backgroundColor: "rgba(255,255,255,0.4)",
                    lineTension: 0.1,
                    data: LGR_MA[1],
                    pointRadius: 0,
                },
                {
                    label: 'Polos',
                    borderColor: "green",
                    backgroundColor: "rgba(255,255,255,0.4)",
                    lineTension: 0.1,
                    data: LGR_MA[2],
                    pointRadius: 0,
                },
                {
                    label: 'Polos',
                    borderColor: "purple",
                    backgroundColor: "rgba(255,255,255,0.4)",
                    lineTension: 0.1,
                    data: LGR_MA[3],
                    pointRadius: 0,
                },
                {
                    label: 'Polos',
                    borderColor: "yellow",
                    backgroundColor: "rgba(255,255,255,0.4)",
                    lineTension: 0.1,
                    data: LGR_MA[4],
                    pointRadius: 0,
                }
                ]
            },
            options: {
                scales: {
                    xAxes: [{
                        type: 'linear',
                        position: 'bottom'
                    }]
                },
                legend: {
                    display: false,
                },
                showLines: true,
                responsive: false,
                maintainAspectRatio: false,
                pointDotRadius  : 0,
                tooltips: {
                    enabled: false,
                    mode: 'single',
                    callbacks: {
                        title: function (tooltipItem, data) { return  'Resposta ao Degrau' },
                        beforeLabel: function(tooltipItems, data) { return  'Amplitude: ' + tooltipItems.yLabel.toFixed(3) },
                        label: function(tooltipItems, data) { return  'Tempo: ' + tooltipItems.xLabel.toFixed(3) }
                    }
                },
            }
        });

        var stepMF = document.getElementById("myStepMF");
        var stepMFChart = new Chart(stepMF, {
            type: 'line',
            data: {
                datasets: [{
                    label: 'MF',
                    borderColor: "rgb(30,144,255)",
                    backgroundColor: "rgba(255,255,255,0.4)",
                    lineTension: 0.1,
                    data: Step[0]
                },
                {
                    label: 'G(s)',
                    borderColor: "red",
                    backgroundColor: "rgba(255,255,255,0.4)",
                    lineTension: 0.1,
                    data: Step[1]
                },
                {
                    label: 'Erro',
                    borderColor: "green",
                    backgroundColor: "rgba(255,255,255,0.4)",
                    lineTension: 0.1,
                    data: Step[2]
                }]

                
            },
           options: {
                scales: {
                    xAxes: [{
                        type: 'linear',
                        position: 'bottom'
                    }]
                },
                showLines: true,
                responsive: false,
                maintainAspectRatio: false,
                tooltips: {
                    enabled: true,
                    mode: 'single',
                    callbacks: {
                        title: function (tooltipItem, data) { return  'Step Response' },
                        beforeLabel: function(tooltipItems, data) { return  'Amplitude: ' + tooltipItems.yLabel.toFixed(3) },
                        label: function(tooltipItems, data) { return  'Tempo: ' + tooltipItems.xLabel.toFixed(3) }
                    }
                },
            }
        });


        var ImpulsepMF = document.getElementById("myImpulseMF");
        var ImpulseMFChart = new Chart(ImpulsepMF, {
            type: 'line',
            data: {
                datasets: [{
                    label: 'MF',
                    borderColor: "rgb(30,144,255)",
                    backgroundColor: "rgba(255,255,255,0.4)",
                    lineTension: 0.1,
                    data: Impulse[0]
                },
                {
                    label: 'G(s)',
                    borderColor: "red",
                    backgroundColor: "rgba(255,255,255,0.4)",
                    lineTension: 0.1,
                    data: Impulse[1]
                },
                {
                    label: 'Erro',
                    borderColor: "green",
                    backgroundColor: "rgba(255,255,255,0.4)",
                    lineTension: 0.1,
                    data: Impulse[2]
                }]

                
            },
           options: {
                scales: {
                    xAxes: [{
                        type: 'linear',
                        position: 'bottom'
                    }]
                },
                showLines: true,
                responsive: false,
                maintainAspectRatio: false,
                tooltips: {
                    enabled: true,
                    mode: 'single',
                    callbacks: {
                        title: function (tooltipItem, data) { return  'Step Response' },
                        beforeLabel: function(tooltipItems, data) { return  'Amplitude: ' + tooltipItems.yLabel.toFixed(3) },
                        label: function(tooltipItems, data) { return  'Tempo: ' + tooltipItems.xLabel.toFixed(3) }
                    }
                },
            }
        });
         
      //////

      //On success show the data posted to server as a message
     // alert('Hi '+json['email'] +'!.' + ' You have entered password:'+      json['password']);
 },

 // handle a non-successful response
 error : function(xhr,errmsg,err) {
 console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
 }
 });


///////////////////////////////
// CONTÍNUO
///////////////////////////////

if (k > buck.critico) {
    $("#modo_conducao_buck").html("<pre>CONTINUOUS CONDUCTION MODE*</pre>");
    $('li.podenao_buck').show()
    cond = "cont";
    $("#potencia_atual_buck").hide();
//    k = (buck.Io * buck.Lo) / (entrada_buck * buck.T);
//    D = buck.q;
//    $("#tensao_atual_buck").hide();
    $("#tensao_atual_buck").html("<br>");
    $("#potencia_atual_buck").hide();
    saida = saida_buck;
    if ($("#check_load_buck").is(':checked')) {
        $("#potencia_atual_buck").show();
        $("#potencia_atual_buck").html("Po* (W): " + (saida * buck.Io).toFixed(2));
    }
} 

///////////////////////////////
// CRÍTICO
///////////////////////////////

else if (buck.critico === k) {
    $("#modo_conducao_buck").html("<pre>CRITICAL CONDUCTION MODE*</pre>");
    cond = "crit";
    k = ((buck.q * buck.q) / 2) * ((1 / buck.q) - 1);
//    D = buck.q;
//    $("#tensao_saida_box_buck").show();
    saida = saida_buck;
    $("#potencia_atual_buck").show();
    $("#potencia_atual_buck").html("Po* (W): " + (saida * buck.Io).toFixed(2));
}

///////////////////////////////
// DESCONTÍNUO
///////////////////////////////

else {
    $("#modo_conducao_buck").html("<pre>DISCONTINUOUS CONDUCTION MODE*</pre>");
    $('li.podenao_buck').hide()

    cond = "desc";
    D = buck.q;
    ganho_ponto = ((D*Math.sqrt(carga_buck)*Math.sqrt(buck.T)*Math.sqrt(D*D*carga_buck*buck.T+8*buck.Lo))-D*D*(carga_buck)*buck.T)/(4*buck.Lo)
    console.log(ganho_ponto)
    k = (buck.Lo * entrada_buck * ganho_ponto)/(carga_buck*entrada_buck*buck.T);
    buck.q = ganho_ponto;

    saida = parseFloat((buck.q * entrada_buck).toFixed(1));
    buck.Io = saida / carga_buck;
//    $("#tensao_atual_buck").show();
$("#tensao_atual_buck").html("Vo* (V): " + saida);
$("#potencia_atual_buck").show();
$("#potencia_atual_buck").html("Po* (W): " + (saida * buck.Io).toFixed(2));
}

///////////////////////////////
// PLOT PRO HTML
///////////////////////////////

$("#capacitancia_tag_buck").html("Capacitance (uF): " + (buck.capacitancia * 1000000).toFixed(2));
$("#ganho_tag_buck").html("Static Gain: " + (saida / entrada_buck).toFixed(2));
$("#duty_tag_buck").html("Duty Cycle: " + D.toFixed(2));
$("#indutancia_critica_buck").html("Critical Induct. (uH): " + (buck.Lcri * 1000000).toFixed(2));
$("#io_param_buck").html("k (param.): " + k.toFixed(2));
$("#io_critica_buck").html("I<sub>o</sub> Critical (A): " + buck.Iocrit.toFixed(3));
$("#io_buck").html("I<sub>o</sub> (A): " + buck.Io.toFixed(2));
$("#indutancia_tag_buck").html("Inductance (uH): " + (buck.Lo * 1000000).toFixed(2));
handle_check_buck();

///////////////////////////////
// PLOT DA TENSÃO NA CARGA
///////////////////////////////

v_carga = [];
i = 0;
while (i < (5 * buck.T)) {
    v_carga.push([i, saida + ((delta_v / 100) / 2) * saida * Math.sin(2 * Math.PI * frequencia_buck * 1000 * i)]);
    i += 0.0000001;
}
data = [
{
    label: "Load Voltage",
    data: v_carga
}
];
tensao_saida_buck = $("#tensao_saida_buck");
options = {
    xaxis: {
    ticks: 4,
    zoomRange: [0.0001, 5 * buck.T],
    panRange: [0, 5 * buck.T]
},
yaxis: {
    zoomRange: [1.1 * saida_buck / 100 * delta_v, 1.3 * saida],
    panRange: [0, 1.2 * saida],
    min: 0,
    max: 1.2 * saida,
},
zoom: {
    interactive: true
},
pan: {
    interactive: true
}
};

plot = $.plot(tensao_saida_buck, data, options);

textox('Time (s)','#tensao_saida_buck');
textoy('Voltage (V)','#tensao_saida_buck');

///////////////////////////////
// PLOT DA OPERAÇÃO
///////////////////////////////

d1_plot = [];
d2_plot = [];
d3_plot = [];
i = 0;
while (i < 0.15) {
    d1_plot.push([i, (1 + Math.sqrt(1 - 8 * i)) / 2]);
    i += 0.00005;
}
i = 0;
while (i < 0.15) {
    d1_plot.push([i, (1 - Math.sqrt(1 - 8 * i)) / 2]);
    i += 0.00005;
}
i = 0;
while (i < buck.critico) {
    d2_plot.push([i, (buck.D*buck.D)/(buck.D*buck.D+2*i)]);
    i += 0.0005;
}
i = buck.critico;
while (i < 0.6) {
    d2_plot.push([i, D]);
    i += 0.0005;
}
if (k > 0.5) {
    k = 0.5;
}
d3_plot = [[k, buck.q - 0.02], [k, buck.q + 0.02]];
$.plot($("#grafico_operacao_buck"), [
{
    label: "Critical Curve",
    data: d1_plot
}, {
    label: "Operation Curve",
    color: 6,
    data: d2_plot
}, {
    label: "Operation Point",
    data: d3_plot,
    color: 2,
}
], {
    yaxis: {
    max: 1,
    min: 0
},
xaxis: {
    ticks: 4,
    max: 0.5
},
grid: {
    hoverable: true,
    clickable: true
}
});
$("#grafico_operacao_buck").bind("plothover", function(event, pos, item) {
    var critico, previousPoint;
    if (item && (item.series.label === "Operation Curve")) {
    if (previousPoint !== item.datapoint) {
        previousPoint = item.datapoint;
        if (pos.x > 0 && pos.x < 1 && pos.y > 0 && pos.y < 1) {
        $("#valor_k_buck").html("k = " + pos.x.toFixed(2));
        if (pos.x > (critico = ((pos.y * pos.y) / 2) * ((1 / pos.y) - 1))) {
            $("#valor_ganho_buck").html("Static Gain = " + D.toFixed(2));
            $("#continha_buck").html("CONTINUOUS");
            $("#valor_vo_buck").html("Vo (V) = " + (entrada_buck * buck.D).toFixed(2));
            carga_nova = ((buck.Lo * item.datapoint[1]) / (item.datapoint[0] * buck.T)).toFixed(2);
            $("#valor_novo_carga_buck").html("Load (&Omega;) = " + carga_nova);
            $("#valor_io_novo_buck").html("Io (A) = " + ((item.datapoint[1] * entrada_buck) / carga_nova).toFixed(2));
        } else {
            $("#valor_ganho_buck").html("Static Gain = " + pos.y.toFixed(2));
            $("#continha_buck").html("DISCONTINUOUS");
            $("#valor_vo_buck").html("Vo (V) = " + (item.datapoint[1] * entrada_buck).toFixed(2));
            carga_nova = ((buck.Lo * item.datapoint[1]) / (item.datapoint[0] * buck.T)).toFixed(2);
            $("#valor_novo_carga_buck").html("load (&Omega;) = " + carga_nova);
            $("#valor_io_novo_buck").html("Io (A) = " + ((item.datapoint[1] * entrada_buck) / carga_nova).toFixed(2));
        }
    }
}
}
});

$("#grafico_operacao_buck").bind("plotclick", function (event, pos, item) {
//    carga_nova = Math.round(carga_nova);
if ($("#check_load_buck").is(':checked')) {
    $("#carga_manual_buck").val(carga_nova);
} else {
    $("#check_load_buck").prop('checked', true);
    handle_check_buck();
    $("#carga_manual_buck").val(carga_nova);
}
});

textox('Parametrized Current','#grafico_operacao_buck');
textoy('Gain','#grafico_operacao_buck');

///////////////////////////////
// PLOT DAS CORRENTES E TENSÕES
///////////////////////////////

i1_plot = [];
i2_plot = [];
i3_plot = [];
t1_plot = [];
t2_plot = [];
t3_plot = [];

if (cond === "cont") {
    var varia_corrente;
    varia_corrente = ((entrada_buck - saida) / buck.Lo) * buck.ton;
    buck.delta_i = 100*varia_corrente/buck.Io;
    // indutor
    i1_plot = [[0, buck.Io - ((buck.Io * buck.delta_i / 100) / 2)], [buck.ton, buck.Io + ((buck.Io * buck.delta_i / 100) / 2)], [buck.T, buck.Io - ((buck.Io * buck.delta_i / 100) / 2)], [buck.T + buck.ton, buck.Io + ((buck.Io * buck.delta_i / 100) / 2)], [2 * buck.T, buck.Io - ((buck.Io * buck.delta_i / 100) / 2)], [2 * buck.T + buck.ton, buck.Io + ((buck.Io * buck.delta_i / 100) / 2)], [3 * buck.T, buck.Io - ((buck.Io * buck.delta_i / 100) / 2)], [3 * buck.T + buck.ton, buck.Io + ((buck.Io * buck.delta_i / 100) / 2)]];
    // chave
    i2_plot = [[0, buck.Io - ((buck.Io * buck.delta_i / 100) / 2)], [buck.ton, buck.Io + ((buck.Io * buck.delta_i / 100) / 2)], [buck.ton, 0], [buck.T, 0], [buck.T, buck.Io - ((buck.Io * buck.delta_i / 100) / 2)], [buck.T + buck.ton, buck.Io + ((buck.Io * buck.delta_i / 100) / 2)], [buck.T + buck.ton, 0], [2 * buck.T, 0], [2 * buck.T, buck.Io - ((buck.Io * buck.delta_i / 100) / 2)], [2 * buck.T + buck.ton, buck.Io + ((buck.Io * buck.delta_i / 100) / 2)], [2 * buck.T + buck.ton, 0], [3 * buck.T, 0], [3 * buck.T, buck.Io - ((buck.Io * buck.delta_i / 100) / 2)], [3 * buck.T + buck.ton, buck.Io + ((buck.Io * buck.delta_i / 100) / 2)]];
    // diodo
    i3_plot = [[0, 0], [buck.ton, 0], [buck.ton, buck.Io + ((buck.Io * buck.delta_i / 100) / 2)], [buck.T, buck.Io - ((buck.Io * buck.delta_i / 100) / 2)], [buck.T, 0], [buck.T + buck.ton, 0], [buck.T + buck.ton, buck.Io + ((buck.Io * buck.delta_i / 100) / 2)], [2 * buck.T, buck.Io - ((buck.Io * buck.delta_i / 100) / 2)], [2 * buck.T, 0], [2 * buck.T + buck.ton, 0], [2 * buck.T + buck.ton, buck.Io + ((buck.Io * buck.delta_i / 100) / 2)], [3 * buck.T, buck.Io - ((buck.Io * buck.delta_i / 100) / 2)], [3 * buck.T, 0], [3 * buck.T + buck.ton, 0]];
    // diodo
    t1_plot = [[0, entrada_buck], [buck.ton, entrada_buck], [buck.ton, 0], [buck.T, 0], [buck.T, entrada_buck], [buck.T + buck.ton, entrada_buck], [buck.T + buck.ton, 0], [2 * buck.T, 0], [2 * buck.T, entrada_buck], [2 * buck.T + buck.ton, entrada_buck], [2 * buck.T + buck.ton, 0], [3 * buck.T, 0], [3 * buck.T, entrada_buck], [3 * buck.T + buck.ton, entrada_buck]];
    // chave
    t2_plot = [[0, 0], [buck.ton, 0], [buck.ton, entrada_buck], [buck.T, entrada_buck], [buck.T, 0], [buck.T + buck.ton, 0], [buck.T + buck.ton, entrada_buck], [2 * buck.T, entrada_buck], [2 * buck.T, 0], [2 * buck.T + buck.ton, 0], [2 * buck.T + buck.ton, entrada_buck], [3 * buck.T, entrada_buck], [3 * buck.T, 0], [3 * buck.T + buck.ton, 0]];
    // indutor
    t3_plot = [[0, entrada_buck-saida], [buck.ton, entrada_buck-saida], [buck.ton, -saida], [buck.T, -saida], [buck.T, entrada_buck-saida], [buck.T + buck.ton, entrada_buck-saida], [buck.T + buck.ton, -saida], [2 * buck.T, -saida], [2 * buck.T, entrada_buck-saida], [2 * buck.T + buck.ton, entrada_buck-saida], [2 * buck.T + buck.ton, -saida], [3 * buck.T, -saida], [3 * buck.T, entrada_buck-saida], [3 * buck.T + buck.ton, entrada_buck-saida]];
} 
else {
    pico = ((entrada_buck - saida) / buck.Lo) * buck.ton;
    tcorte=buck.T-(entrada_buck*buck.D*buck.T)/saida;
    tcorte=buck.T-tcorte;
    // indutor    
    i1_plot = [[0, 0], [buck.ton, pico], [tcorte, 0], [buck.T, 0], [buck.ton + buck.T, pico], [tcorte + buck.T, 0], [buck.T * 2, 0], [buck.ton + buck.T * 2, pico], [tcorte + buck.T * 2, 0], [buck.T * 3, 0], [buck.ton + buck.T * 3, pico]];
    // chave
    i2_plot = [[0, 0], [buck.ton, pico], [buck.ton, 0], [tcorte, 0], [buck.T, 0], [buck.ton + buck.T, pico], [buck.ton + buck.T, 0], [tcorte + buck.T, 0], [buck.T * 2, 0], [buck.ton + buck.T * 2, pico], [buck.ton + buck.T * 2, 0], [tcorte + buck.T * 2, 0], [buck.T * 3, 0], [buck.ton + buck.T * 3, pico]];
    // diodo
    i3_plot = [[0, 0], [buck.ton, 0], [buck.ton, pico], [tcorte, 0], [buck.T, 0], [buck.ton + buck.T, 0], [buck.ton + buck.T, pico], [tcorte + buck.T, 0], [buck.T * 2, 0], [buck.ton + buck.T * 2, 0], [buck.ton + buck.T * 2, pico], [tcorte + buck.T * 2, 0], [buck.T * 3, 0], [buck.ton + buck.T * 3, 0]];
    // diodo
    t1_plot = [[0, entrada_buck], [buck.ton, entrada_buck], [buck.ton, 0], [tcorte, 0], [tcorte, saida], [buck.T, saida], [buck.T, entrada_buck], [buck.ton + buck.T, entrada_buck], [buck.ton + buck.T, 0], [tcorte + buck.T, 0], [tcorte + buck.T, saida], [buck.T * 2, saida], [buck.T * 2, entrada_buck], [buck.ton + buck.T * 2, entrada_buck], [buck.ton + buck.T * 2, 0], [tcorte + buck.T * 2, 0], [tcorte + buck.T * 2, saida], [buck.T * 3, saida], [buck.T * 3, entrada_buck], [buck.ton + buck.T * 3, entrada_buck]];
    // chave
    t2_plot = [[0, 0], [buck.ton, 0], [buck.ton, entrada_buck], [tcorte, entrada_buck], [tcorte, entrada_buck-saida], [buck.T, entrada_buck-saida], [buck.T, 0], [buck.ton + buck.T, 0], [buck.ton + buck.T, entrada_buck], [tcorte + buck.T, entrada_buck], [tcorte + buck.T, entrada_buck-saida], [buck.T * 2, entrada_buck-saida], [buck.T * 2, 0], [buck.ton + buck.T * 2, 0], [buck.ton + buck.T * 2, entrada_buck], [tcorte + buck.T * 2, entrada_buck], [tcorte + buck.T * 2, entrada_buck-saida], [buck.T * 3, entrada_buck-saida], [buck.T * 3, 0], [buck.ton + buck.T * 3, 0]];
    // indutor
    t3_plot = [[0, entrada_buck-saida], [buck.ton, entrada_buck-saida], [buck.ton, -saida], [tcorte, -saida], [tcorte, 0], [buck.T, 0], [buck.T, entrada_buck-saida], [buck.ton + buck.T, entrada_buck-saida], [buck.ton + buck.T, -saida], [tcorte + buck.T, -saida], [tcorte + buck.T, 0], [buck.T * 2, 0], [buck.T * 2, entrada_buck-saida], [buck.ton + buck.T * 2, entrada_buck-saida], [buck.ton + buck.T * 2, -saida], [tcorte + buck.T * 2, -saida], [tcorte + buck.T * 2, 0], [buck.T * 3, 0], [buck.T * 3, entrada_buck-saida], [buck.ton + buck.T * 3, entrada_buck-saida]];
}
$.plot($("#corrente_indutor_buck"), [
{
    color: 6,
    label: "Inductor Current",
    data: i1_plot
},
], {
    yaxis: {
        min: 0
    }
});

textox('Time (s) ','#corrente_indutor_buck');
textoy('Current (A) ','#corrente_indutor_buck');

$.plot($("#tensao_indutor_buck"), [
{
    color: 0,
    label: "Inductor Voltage",
    data: t3_plot
},
], {
    yaxis: {
//      min: -50
}
});

textox('Time (s)','#tensao_indutor_buck');
textoy('Voltage (V)','#tensao_indutor_buck');

$.plot($("#corrente_chave_buck"), [
{
    color: 6,
    label: "Switch Current",
    data: i2_plot
}
], {
    yaxis: {
        min: 0
    }
});

textox('Time (s)','#corrente_chave_buck');
textoy('Current (A)','#corrente_chave_buck');

$.plot($("#corrente_diodo_buck"), [
{
    color: 6,
    label: "Diode Current",
    data: i3_plot
}
], {
    yaxis: {
        min: 0
    }
});

textox('Time (s)','#corrente_diodo_buck');
textoy('Current (A)','#corrente_diodo_buck');

$.plot($("#tensao_diodo_buck"), [
{
    color: 0,
    label: "Diode Voltage",
    data: t1_plot
}
], {
    yaxis: {
        min: 0
    }
});

textox('Time (s)','#tensao_diodo_buck');
textoy('Voltage (V)','#tensao_diodo_buck');

$.plot($("#tensao_chave_buck"), [
{
    color: 0,
    label: "Switch Voltage",
    data: t2_plot
}
], {
    yaxis: {
        min: 0
    }
});

textox('Time (s)','#tensao_chave_buck');
textoy('Voltage (V)','#tensao_chave_buck');

///////////////////////////////
// DIAGRAMA DE BODE
///////////////////////////////

g_plot = [];
f_plot = [];

if (cond == "cont") {
    Ggo=saida_buck / entrada_buck;
    Gdo=saida_buck/buck.D;
    wo=1/Math.sqrt(buck.Lo*buck.capacitancia);
    Q=carga_buck*Math.sqrt(buck.capacitancia/buck.Lo);
    si = 1/(2*Q);

    j = 100;
    while (j < 1000000) {
    g_plot.push([j, 20 * Math.log((Gdo/(Math.sqrt(( (1-(j/wo)*(j/wo))*(1-(j/wo)*(j/wo)) ) + ( (1/(Q*Q))*((j/wo)*(j/wo)) )))))/Math.log(10) ]);
    fase = (180 / Math.PI) * Math.atan( ( (1/(Q))*(j/wo)) / ( (1-(j/wo)*(j/wo)) ));
    if (fase < 0) {
        fase = fase + 180;
    }
    f_plot.push([j, -fase]);
    j += 100;
}
$.plot($("#diagrama_bode_buck"), [
{
    color: 2,
    label: "Gain Diagram",
    data: g_plot
}
], {
    xaxis: {
        ticks: [100,1000,10000,100000],
        transform:  function(v) {return Math.log(v);} , tickDecimals: 1 ,
        tickFormatter: function (v, axis) {return "10" + (Math.round( Math.log(v)/Math.LN10)).toString().sup();}
    },
    yaxis: {
        ticks: 4
    }
});
$.plot($("#diagrama_fase_buck"), [
{
    color: 2,
    label: "Phase Diagram",
    data: f_plot
}
], {
    xaxis: {
        ticks: [100,1000,10000,100000],
        transform:  function(v) {return Math.log(v);} , tickDecimals: 1 ,
        tickFormatter: function (v, axis) {return "10" + (Math.round( Math.log(v)/Math.LN10)).toString().sup();}
    }
});

textox('Frequence (Hz)','#diagrama_bode_buck');
textoy('Gain (V)','#diagrama_bode_buck');

textox('Frequence (Hz)','#diagrama_fase_buck');
textoy('Angle (°)','#diagrama_fase_buck');

///////////////////////////////
// RESPOSTA AO DEGRAU
///////////////////////////////
step_plot = [];

t=0;
if (si > 1) {
    while (t < 5*((3*si)/wo)) {
    step_plot.push([t, entrada_buck * Ggo * ( 1 + ((-si-Math.sqrt(si*si-1)) * Math.exp(-wo*(si-Math.sqrt(si*si-1))*t) - (-si+Math.sqrt(si*si-1)) * Math.exp(-wo*(si+Math.sqrt(si*si-1))*t))/(2*Math.sqrt(si*si-1))) ]);
    t+=((5*((3*si)/wo))/100);
}
}
else {
    while (t < 4.6/(si*wo)) {
    step_plot.push([t, entrada_buck * Ggo * ( 1 - (1/(Math.sqrt(1-si*si))) * Math.exp(-si*wo*t) * Math.sin(wo*Math.sqrt(1-si*si)*t+Math.acos(si))) ] );
    t+=((5*((3*si)/wo))/100);
}
}

$.plot($("#resposta_degrau_buck"), [
{
    color: 3,
    label: "Step Response",
    data: step_plot
}
], {
    xaxis: {
    min: 0
},
yaxis: {
    min: 0
},
grid: {
    hoverable: true,
    clickable: true
}

});

textox('Time (s)','#resposta_degrau_buck');
textoy('Voltage (V)','#resposta_degrau_buck');

$("#resposta_degrau_buck").bind("plothover", function(event, pos, item) {
    var previousPoint;
    if (item.series.label === "Step Response") {
    if (previousPoint !== item.datapoint) {
        previousPoint = item.datapoint;
        $("#valor_tensao_step_buck").html("Vo (V) =  " + pos.y.toFixed(2));
        $("#valor_tempo_step_buck").html("t (s) = " + pos.x.toFixed(6));
    }
}
});
}

if (carga_manual_buck = "null") {
    carga_manual_buck = carga_buck.toFixed(2);
}







};