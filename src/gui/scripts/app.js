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
    const microfono = await importarRecurso("../assets/iconos/micro.svg")
		const bocina = await importarRecurso("../assets/iconos/bocina.svg")
		const barraIzquierda = entradaIzquierda.getElementsByClassName("entrada__barra")[0]
	  barraIzquierda.innerHTML += microfono + bocina;
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

(function events(){

	document.addEventListener('DOMContentLoaded', () =>{
		new ImportarRecursos().cargarRecursos();
	});	

})();
