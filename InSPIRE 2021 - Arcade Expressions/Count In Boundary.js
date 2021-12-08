// Simple count in a boundary. See NAPSG's techical document, "No Coins Required: Using Arcade to Enhance Your Public Safety Applications" for more information.
// https://inspire2021.napsgfoundation.org/pages/arcade

var irwin = FeatureSetByName($map,"Active Fires (IRWIN / Esri)")
var countIrwin = round(Count(Intersects(irwin, $feature)), 1)
return countIrwin