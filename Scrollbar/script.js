function my_fonction() {
	user_name = prompt("Quel est votre nom ?");
	document.getElementById('user_name').innerHTML = user_name;
}
function grandir(size) {
	document.getElementById("grandir").setAttribute("size", size);
		
}
function reduire(size) {
	document.getElementById("grandir").setAttribute("size", size);
}