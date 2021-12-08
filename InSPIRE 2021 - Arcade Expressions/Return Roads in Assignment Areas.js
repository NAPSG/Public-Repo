// List Road Names in selected boundary 
// See NAPSG's techical document, "No Coins Required: Using Arcade to Enhance Your Public Safety Applications" for more information.
// https://inspire2021.napsgfoundation.org/pages/arcade

var roads = FeatureSetByName($map,"Roads (Base Data)", ["Street_Name"]);
var intersectRoads = Intersects(roads, $feature);
var uniqueRoads = [];
for (var feat in intersectRoads) {
    if (IndexOf(uniqueRoads, feat.Street_Name) == -1) {
        uniqueRoads[Count(uniqueRoads)] = feat.Street_Name;
    }
}

return uniqueRoads