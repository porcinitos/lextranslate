// globales 
const ESPAÑOL = 0, ENGLISH = 1;
let lenguajeActual = ESPAÑOL;
//elementos
const app = document.getElementById("app")
const entradaIzquierda = document.getElementById("entradaIzquierda")
const entradaDerecha   = document.getElementById("entradaDerecha")
const cabeceras = document.getElementById("cabeceras")

// clases
class ImportarRecursos{
	constructor(){}
 
	async cargarIconos(){
		const barraIzquierda = entradaIzquierda.getElementsByClassName("entrada__barra")[0]
    const microfono = await importarRecurso("../assets/iconos/micro.svg")
		const bocina = await importarRecurso("../assets/iconos/bocina.svg")
		barraIzquierda.innerHTML += microfono + bocina ;
		const iconos = barraIzquierda.getElementsByClassName("barra__icono")
		for(let icono of iconos){ icono.addEventListener("click", iconosBarra);}
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

function iconosBarra(e){
  let classList = e.currentTarget.classList;
	if(!classList.contains("icono-desactivado")){
		if(classList.contains("micro")){
		  console.log("Detectar Voz")
		}else if (classList.contains("bocina")){
		  console.log("Escuchar Audio")
		}
	}
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

function comenzandoAEscribir(e){
	const archivo = entradaIzquierda.getElementsByClassName("entrada__archivo")[0]
	const barra = entradaIzquierda.getElementsByClassName("entrada__barra")[0]
	const bocina = barra.getElementsByClassName("bocina")[0]
	const micro = barra.getElementsByClassName("micro")[0]
	const traducir = document.getElementById("traducir")
	if ( e.target.value.length > 0){
		if (!archivo.classList.contains("invisible")){
		  archivo.classList.add("invisible")
			micro.classList.add("icono-desactivado")
			traducir.classList.remove("desactivado")
			bocina.classList.remove("icono-desactivado")
		}
	}else if (e.target.value.length === 0){
		archivo.classList.remove("invisible")
		micro.classList.remove("icono-desactivado")
		traducir.classList.add("desactivado")
		bocina.classList.add("icono-desactivado")
	}
}

(function events(){

	document.addEventListener('DOMContentLoaded', () =>{
		new ImportarRecursos().cargarRecursos();
	});	

	entradaIzquierda.getElementsByClassName("entrada__textarea")[0].addEventListener("keyup", comenzandoAEscribir)
	entradaIzquierda.getElementsByClassName("entrada__archivo")[0].addEventListener("click", () => console.log("subir archivo"))

})();
