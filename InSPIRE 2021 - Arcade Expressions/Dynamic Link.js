// Dynamic links in Arcade 

// See NAPSG's techical document, "No Coins Required: Using Arcade to Enhance Your Public Safety Applications" for more information.
// https://inspire2021.napsgfoundation.org/pages/arcade

// If you have a Lat-lon, that makes it easy. Follow the code below

"https://forecast.weather.gov/MapClick.php?lon=" +
LEFT($feature.iaLongitude,7) + "&lat=" + LEFT($feature.iaLatitude,7)

// Pay attention to the URL on varous websites and place the number of digits with the lat-lon (example above is 7)

// If you do not have lat-lon, use the code below

function MetersToLatLon(x, y) {
    var originShift = 2.0 * PI * 6378137.0 / 2.0;
    var lon = (x / originShift) * 180.0;
    var lat = (y / originShift) * 180.0;
    lat = 180.0 / PI * (2.0 * Atan( Exp( lat * PI / 180.0)) - PI / 2.0);
    return [lat, lon];
}
function CreateNOAAurl(lat, lon) {
    return "https://forecast.weather.gov/MapClick.php?lon=" + LEFT(lon,17) + "&lat=" + LEFT(lat,17)
}
var latlon = MetersToLatLon(Geometry($feature).X, Geometry($feature).Y);
var url = createNOAAurl(latlon[0], latlon[1]);
return url;
