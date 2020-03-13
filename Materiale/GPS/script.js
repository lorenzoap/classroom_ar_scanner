function load(){
    setInterval(getGeoLocation, 500);
}




function getGeoLocation(){
    if(navigator.geolocation){
      navigator.geolocation.watchPosition(onSuccess, onError);
    }
    else
    {
      console.log('Not supported');
    }
}

function onSuccess(position){
    const{latitude, longitude} = position.coords;


    document.getElementById('demo').innerHTML =
    "Latitudine: " + latitude + "</br>" +
    "Longitudine: " + longitude + "</br>" +
    "Timestamp: " + position.timestamp + "</br>" +
    "Distanza: " + calculateDistance(46.033328, 8.967561, latitude,  longitude);

    console.log(latitude);
    console.log(longitude)
}

function onError(error){
    console.log(error);
}


var earthRadius = 6371;

function calculateDistance(lat, long, start_lat, start_long) {
    var lat = lat - start_lat; // Difference of latitude
    var lon = long - start_long; // Difference of longitude


    console.log(lat);
    console.log(lon);

    var disLat = (lat*Math.PI*earthRadius)/180; // Vertical distance
    var disLon = (lon*Math.PI*earthRadius)/180; // Horizontal distance

    var ret = Math.pow(disLat, 2) + Math.pow(disLon, 2);
    ret = Math.sqrt(ret); // Total distance (calculated by Pythagore: a^2 + b^2 = c^2)

    return ret;
}
