const artyom = new Artyom();

artyom.initialize({lang:"es-ES"});

let settings = {
    continuous:true, // Don't stop never because i have https connection
    onResult:function(text){
        // text = the recognized text
        console.log(text);
    },
    onStart:function(){
        console.log("Escuchando voz");
    },
    onEnd:function(){
        console.log("Detenido");
    }
};

var UserDictation = artyom.newDictation(settings);

function startRecognition(){
  UserDictation.start();
}

function stopRecognition(){
  UserDictation.stop();
}
