function initMap() {
    // Create a new Google Map
    var map = new google.maps.Map(document.getElementById('map'), {
      center: { lat: 0, lng: 0 },
      zoom: 2
    });
  
    // Fetch the wildfire data from the server
    fetch('/data')
      .then(response => response.json())
      .then(data => {
        // Add markers to the map
        addMarkers(map, data);
      });
}

function addMarkers(map, data) {
    data.forEach(wildfire => {
        var latLng = new google.maps.LatLng(wildfire.Latitude, wildfire.Longitude);
  
        // Create a marker for each wildfire
        var marker = new google.maps.Marker({
            position: latLng,
            map: map
        });
    });
}

window.onload = initMap;

  
