//elementos
const app = document.getElementById("app")
const entradaIzquierda = document.getElementById("entradaIzquierda")
const entradaDerecha   = document.getElementById("entradaDerecha")
const cabeceras = document.getElementById("cabeceras")

// clases
class ImportarRecursos{
	constructor(){}
	
	async cargarRecursos(){
		const microfono = await importarRecurso("../assets/iconos/micro.svg")
		const bocina = await importarRecurso("../assets/iconos/bocina.svg")
		const barraIzquierda = entradaIzquierda.getElementsByClassName("entrada__barra")[0]
		let cambiar = await importarRecurso("../assets/iconos/cambiar.svg")
    cambiar = document.createRange().createContextualFragment(cambiar) 
		cabeceras.insertBefore(cambiar,cabeceras.lastElementChild)
	  barraIzquierda.innerHTML += microfono + bocina;
	}
}

// funciones
async function importarRecurso(path){
		const response = await fetch(path);
		let text = await response.text();
		return text;
}

(function events(){
	document.addEventListener('DOMContentLoaded', () =>{
		new ImportarRecursos().cargarRecursos();

	})

})();
