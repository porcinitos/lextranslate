// globales 
const ESPAÑOL = 0, ENGLISH = 1;
let lenguajeActual = ESPAÑOL;

//elementos
const app = document.getElementById("app")
const botonTraducir = document.getElementById("traducir")
const entradaIzquierda = document.getElementById("entradaIzquierda")
const entradaDerecha   = document.getElementById("entradaDerecha")
const barraIzquierda = entradaIzquierda.getElementsByClassName("entrada__barra")[0]
const barraDerecha= entradaDerecha.getElementsByClassName("entrada__barra")[0]
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

	activarHablar(area){ eel.hablar(area.value, area.classList.contains("textarea-izquierda") ? lenguajeActual: lenguajeActual ? 0 : 1); }
 			
}

const reconocimientoPorVoz = new ReconocimientoPorVoz();

class ImportarRecursos{
	constructor(){}
 
	async cargarIconos(){
		const bocina       = await importarRecurso("../assets/iconos/bocina.svg")
    const microfono    = await importarRecurso("../assets/iconos/micro.svg")
		const portapapeles = await importarRecurso("../assets/iconos/portapapeles.svg")
		barraIzquierda.innerHTML += microfono + bocina ;
		barraDerecha.innerHTML += portapapeles + bocina ;
		let iconos = [...barraIzquierda.getElementsByClassName("barra__icono")]
		iconos.push(...barraDerecha.getElementsByClassName("barra__icono"))
		for(let icono of iconos){ icono.addEventListener("click", iconoClick );}
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
	let entrada = e.currentTarget.parentElement.parentElement
  let area = entrada.getElementsByClassName("entrada__textarea")[0]
	if(!classList.contains("icono-desactivado")){
		if (classList.contains("micro")){
      microfonoClick(area,e.currentTarget)  
		}else if(classList.contains("bocina")){
      reconocimientoPorVoz.activarHablar(area)
		}else if (classList.contains("portapapeles")){
      alert("Copiar al clipboard")
		}
	}
}

function cambiarEstadoAlEscribir(){
	ocultarResultados()
	// solo se puede escribir en la barra izquierda
	const micro   = barraIzquierda.getElementsByClassName("micro")[0]
	const bocina  = barraIzquierda.getElementsByClassName("bocina")[0]
	const archivo = entradaIzquierda.getElementsByClassName("entrada__archivo")[0]
	const texto= entradaIzquierda.getElementsByClassName("entrada__textarea")[0].value
	if ( texto.length > 0){
    if (!archivo.classList.contains("invisible")){
		  archivo.classList.add("invisible")
			micro.classList.add("icono-desactivado")
			botonTraducir.classList.remove("desactivado")
			bocina.classList.remove("icono-desactivado")
		}
	}else {
 	  archivo.classList.remove("invisible")
	  micro.classList.remove("icono-desactivado")
	  botonTraducir.classList.add("desactivado")
	  bocina.classList.add("icono-desactivado")
	}

}

eel.expose(mostrarTabla)
function mostrarTabla(tablaObj){
  tablaObj = JSON.parse(tablaObj)
	const salida = document.getElementById(tablaObj.tipo === "errores" ? "salidaDerecha" : "salidaIzquierda" )
	salida.innerText = tablaObj.tabla
	salida.classList.remove("invisible")
}

function ocultarResultados(){
	const salidaErrores  = document.getElementById("salidaDerecha")
	const salidaTokens   = document.getElementById("salidaIzquierda")
  const iconos = barraDerecha.getElementsByClassName("barra__icono")
  const textarea = entradaDerecha.getElementsByClassName("entrada__textarea")[0]
	salidaErroresVisible = !salidaErrores.classList.contains("invisible")
	salidaTokensVisible   = !salidaTokens.classList.contains("invisible")

	if (salidaTokensVisible && !salidaErroresVisible){
    entradaDerecha.classList.add("desactivado")
    textarea.classList.add("desactivado")
		textarea.value = "Traduccion"
	  for(let icono of iconos){ icono.classList.add("icono-desactivado")}
	}

	if (salidaTokensVisible){
		salidaTokens.classList.add("invisible")
	}

	if (salidaErroresVisible){
    salidaErrores.classList.add("invisible")
		textarea.value = "Traduccion"
	}	
}

eel.expose(mostrarTraduccion)
function mostrarTraduccion(texto){
	let textarea = entradaDerecha.getElementsByClassName("entrada__textarea")[0]
  const iconos = barraDerecha.getElementsByClassName("barra__icono")
	for(let icono of iconos){ icono.classList.remove("icono-desactivado")}

	textarea.value = texto
  entradaDerecha.classList.remove("desactivado")
  textarea.classList.remove("desactivado")
}

eel.expose(mostrarArchivo)
function mostrarArchivo(texto){
  entradaIzquierda.getElementsByClassName("entrada__textarea")[0].value = texto
	cambiarEstadoAlEscribir()
}

eel.expose(mostrarErrorTraduccion)
function mostrarErrorTraduccion(){
	entradaDerecha.getElementsByClassName("entrada__textarea")[0].value =  "Errores durante el análisis"
}

function botonTraducirClick(){
	const texto = entradaIzquierda.getElementsByClassName("entrada__textarea")[0].value.length
	eel.analizar(texto)
}

(function events(){

	document.addEventListener('DOMContentLoaded', () =>{
		new ImportarRecursos().cargarRecursos();
	});	

	entradaIzquierda.getElementsByClassName("entrada__textarea")[0].addEventListener("keyup", cambiarEstadoAlEscribir)
	entradaIzquierda.getElementsByClassName("entrada__archivo")[0].addEventListener("click", () => eel.cargar_archivo() )
	botonTraducir.addEventListener("click", botonTraducirClick)

})();
