function myFunction() {
    document.getElementById("myDropdown").classList.toggle("show");
}

window.onclick = function(e) {
  if (!e.target.matches('.dropbtn')) {
    var myDropdown = document.getElementById("myDropdown");
      if (myDropdown.classList.contains('show')) {
        myDropdown.classList.remove('show');
      }
  }
}

// google map

function initMap() { 
  var test= {lat: 0.3476, lng: 32.5825}; 
  var map = new google.maps.Map(document.getElementById('map'), { 
    zoom: 10, 
    center: test 
  }); 
  var marker = new google.maps.Marker({ 
    position: test, 
    map: map 
  }); 
} 