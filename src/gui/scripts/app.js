// globales 
const ESPAÑOL = 0, ENGLISH = 1;
let lenguajeActual = ESPAÑOL;

//elementos
const app = document.getElementById("app")
const botonTraducir = document.getElementById("traducir")
const entradaIzquierda = document.getElementById("entradaIzquierda")
const barraIzquierda = entradaIzquierda.getElementsByClassName("entrada__barra")[0]
const entradaDerecha   = document.getElementById("entradaDerecha")
const cabeceras = document.getElementById("cabeceras")

// clases


class ReconocimientoPorVoz{
	constructor(){
    this.artyom = new Artyom();
    this.artyom.initialize({lang:"es-ES", debug: false}) 
		this.dicatado = {}
	}

	activarEscucharYEscribir(area){
    let archivo = entradaIzquierda.getElementsByClassName("entrada__archivo")[0]
  	let configs = {
			lang: lenguajeActual == ESPAÑOL? "es-ES" : "en-US",
      continuous:true, 
			onResult: texto => area.value = texto != "" ? texto : area.value,
			onStart: () => archivo.classList.add("invisible"),
			onEnd:() => {archivo.classList.remove("invisible"); cambiarEstadoAlEscribir()}
		}
		this.dictado = this.artyom.newDictation(configs)
		this.dictado.start()
  }
	
  detenerEscucharYEscribir(){ this.dictado.stop()}

	activarHablar(area){ eel.hablar(area.value, lenguajeActual)}
 			
}

const reconocimientoPorVoz = new ReconocimientoPorVoz();

class ImportarRecursos{
	constructor(){}
 
	async cargarIconos(){
    const microfono = await importarRecurso("../assets/iconos/micro.svg")
		const bocina = await importarRecurso("../assets/iconos/bocina.svg")
		barraIzquierda.innerHTML += microfono + bocina ;
		const iconos = barraIzquierda.getElementsByClassName("barra__icono")
		for(let icono of iconos){ icono.addEventListener("click", iconoClick );}
	  document.getElementById("traducir").addEventListener("click", () => console.log(lenguajeActual))
	}
	async cargarCambiar(){
  	let cambiar = await importarRecurso("../assets/iconos/cambiar.svg")
    cambiar = document.createRange().createContextualFragment(cambiar) 
		cabeceras.insertBefore(cambiar,cabeceras.lastElementChild)
    document.getElementById("cambiarLenguaje").addEventListener("click", cambiarLenguaje); 
	}
	async cargarRecursos(){
    this.cargarIconos();
		this.cargarCambiar();
	}
}

// funciones
async function importarRecurso(path){
  const response = await fetch(path);
  let text = await response.text();
  return text;
}


function cambiarLenguaje(){
	const cabeceraIzquierda = document.getElementById("cabeceraIzquierda")
	const cabeceraDerecha= document.getElementById("cabeceraDerecha")
	switch (lenguajeActual){
		case ESPAÑOL:
			lenguajeActual = ENGLISH;
			cabeceraIzquierda.innerText = "Inglés"
			cabeceraDerecha.innerText = "Español"
		break;
    case ENGLISH:
			lenguajeActual = ESPAÑOL;
			cabeceraIzquierda.innerText = "Español"
			cabeceraDerecha.innerText  = "Inglés"
		break;
	}
}

function microfonoClick(area,currentTarget){
  if(currentTarget.classList.contains("seleccionado")){
    currentTarget.classList.remove("seleccionado")
		reconocimientoPorVoz.detenerEscucharYEscribir(area)
	}else{
	  currentTarget.classList.add("seleccionado")
		reconocimientoPorVoz.activarEscucharYEscribir(area)
 	}
}

function iconoClick(e){
  let classList = e.currentTarget.classList;
  let area = entradaIzquierda.getElementsByClassName("entrada__textarea")[0]
	if(!classList.contains("icono-desactivado")){
		classList.contains("micro") ? microfonoClick(area,e.currentTarget) : reconocimientoPorVoz.activarHablar(area)
	}
}


function cambiarEstadoAlEscribir(){
	// solo se puede escribir en la barra izquierda
	const micro   = barraIzquierda.getElementsByClassName("micro")[0]
	const bocina  = barraIzquierda.getElementsByClassName("bocina")[0]
	const archivo = entradaIzquierda.getElementsByClassName("entrada__archivo")[0]
	const texto   = entradaIzquierda.getElementsByClassName("entrada__textarea")[0].value.length
	if ( texto > 0){
    if (!archivo.classList.contains("invisible")){
		  archivo.classList.add("invisible")
			micro.classList.add("icono-desactivado")
			document.getElementById("traducir").classList.remove("desactivado")
			bocina.classList.remove("icono-desactivado")
		}
	}else {
 	  archivo.classList.remove("invisible")
	  micro.classList.remove("icono-desactivado")
	  document.getElementById("traducir").classList.add("desactivado")
	  bocina.classList.add("icono-desactivado")
	}
}

(function events(){

	document.addEventListener('DOMContentLoaded', () =>{
		new ImportarRecursos().cargarRecursos();
	});	

	entradaIzquierda.getElementsByClassName("entrada__textarea")[0].addEventListener("keyup", cambiarEstadoAlEscribir)
	entradaIzquierda.getElementsByClassName("entrada__archivo")[0].addEventListener("click", () => console.log("subir archivo"))

})();
