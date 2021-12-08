// Utilized in Crisis Communication Catalog Public Map

// This first part is used as a section header to determine if any data exists. If any information in any field, it will return "Fire Department Information".
// If there is nothing in every field, "No Fire Department Information Available" will display instead
var result = When($feature["FD_web"] != NULL, "Fire Department Information", $feature["FD_twitter"] != NULL, "Fire Department Information", $feature["FD_facebook"] != NULL, "Fire Department Information", "No Fire Department Information Available")
return result


// For single fields use the script below. This is helpful if you want the pop-up to show only data that exists
if($feature["LE_web"] != NULL){
    return "Official"
}
else{
    return NULL
}