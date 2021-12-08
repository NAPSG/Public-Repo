// Utilized in Crisis Communication Catalog Public Map
// This script returns text describing the completion/ data status of communities
// Input this into a new Arcade expression in the ArcGIS Online pop-up configuration, then add that expression to your pop-up. 

If($feature["completion_status"] == 'not_complete'){
    return 'No information has been submitted for this community'
}
If($feature["completion_status"]=='in_progress'){
    return 'Information for this community is being reviewed'
}
If($feature["completion_status"]=='complete'){
    return 'Information has been reviewd and validated'
}