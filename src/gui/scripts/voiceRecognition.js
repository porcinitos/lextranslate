const artyom = new Artyom();

artyom.initialize();

let dictado = artyom.newDictation(settings);

function startRecognition(){
  UserDictation.start();
}

function stopRecognition(){
  UserDictation.stop();
}
