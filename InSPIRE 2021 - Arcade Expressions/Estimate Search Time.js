// Estiamates the amount of time in hours it may take for search team of 5 to complete area 
// See NAPSG's techical document, "No Coins Required: Using Arcade to Enhance Your Public Safety Applications" for more information.
// https://inspire2021.napsgfoundation.org/pages/arcade

var itemID = 'bb69f10baf334d4c935a0fb23d758f38'
var prtl = Portal("https://www.arcgis.com")
var buildings = FeatureSetByPortalItem(prtl,itemID, 0)

var countBuildings = Count(Intersects(buildings,$feature))

var timeBuildings = (5*countBuildings)/60

var timeSearch = (timeBuildings/5)

return timeSearch