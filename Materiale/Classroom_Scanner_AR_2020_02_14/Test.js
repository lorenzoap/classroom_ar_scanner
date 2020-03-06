<!DOCTYPE html>
<html>
<body onload="myFunction()">

<p>Click the button to get your coordinates.</p>

<p id="demo"></p>

<script>
var x = document.getElementById("demo");

function myFunction(){
setInterval(getLocation, 10);
}

function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition);
  } else {
    x.innerHTML = "Geolocation is not supported by this browser.";
  }
}

function showPosition(position) {
  x.innerHTML = "Latitude: " + position.coords.latitude +
  "<br>Longitude: " + position.coords.longitude;
}
</script>

</body>
</html>
