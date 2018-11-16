
var slider = document.getElementById("myRangeConsole");
var output = document.getElementById("OConsole");

var slider2 = document.getElementById("myRangeGenre");
var output2 = document.getElementById("Ogenre");

var slider3 = document.getElementById("myRangeAge");
var output3 = document.getElementById("Oageres");

output.innerHTML = slider.value;
output2.innerHTML = slider2.value;
output3.innerHTML = slider3.value;

slider.oninput = function() {
  output.innerHTML = this.value;
}

slider2.oninput = function() {
  output2.innerHTML = this.value;
}

slider3.oninput = function() {
  output3.innerHTML = this.value;
}

