# NAPSG's Public Code Repository
This repository was created to serve as a place to hold template versions of scripts created by NAPSG Foundation to be used by our partners and the public safety community. Every script here is free and open to the public.

Every script in here has been modified to be a blank template of what NAPSG uses and includes instructions on how to utilize them best in your environment. Each script is subject to modification without notice and new scripts are added as they become available.

Most scripts in this repository are designed to be used in either ArcGIS Online Notebooks or within Arcade in Esri's WebMap viewer. See the sections below on how to best utilize them.

Reach out to NAPSG Foundation at <a href="mailto:admin@publicsafetygis.org">admin@publicsafetygis.org</a> if you have any questions. If you discover any bugs or want to make any suggestions to the scripts, use the Issues tab here on Github and post your bug or suggestion.

### Notebooks
ArcGIS Online Notebooks use a python coding system called Jupyter Notebooks which allows you to run one cell of code at a time or add notes above the cells of code. Each script will require some modification to run with your organization, which are outlined in both cell headers and comments (identified as # as the first character in the line) within the code itself.

Follow these steps to download and use them in your environment:
1. From the home page of this repository, click the green Code button and select Download Zip.
2. When the repo is done downloading, you will have access to every code in this repo from your desktop.
3. Go to your Content page on ArcGIS Online.
4. Click Add Content and upload the .ipynb file of the script you wish to bring into ArcGIS Online. It will automatically upload as a new notebook
5. When the notebook has been uploaded, go to the Settings tab from the Overview tab. Find the section titled "Notebook Settings" and "Notebook Runtime" at the bottom of the page. Click the dropdown and select "ArcGIS Notebook Python 3 Standard - 6.0". If this is already selected, you can skip this step.
6. Open your new Notebook and edit accordingly to fit your need for your organization using the notes within the script. Remember to save often!
7. Test your Notebook to ensure you have no errors.
8. (Optional) Schedule a task to make your Notebook run automatically. See the <a href="https://doc.arcgis.com/en/arcgis-online/create-maps/prepare-a-notebook-for-automated-execution.htm">Esri Technical Document, <i>Schedule a notebook task</i></a> for more information.

Notes:
- If you cannot schedule a task or the tasks option is missing altogether, you may need to get your system administrator to enable it for you. This option is found under Orgaizaion > Settings > Member Roles > Edit Role > Content


## Arcade
Arcade is a programming language similar to JavaScript that is built within ArcGIS and allows us to create enhanced popups, dynamic symbology, or calculate fields. The scripts in this repository currently are only for pop-ups but may include symbology or field calculations in the future. If you are completely new to Arcade, use the Esri <a href="https://www.esri.com/about/newsroom/arcuser/arcade-4-steps/"><i>Learn ArcGIS Arcade in Four Easy Steps</i></a> document to understand how and where it is used. Several of these scripts come from NAPSG's InSPIRE 2021 document, <a href="https://inspire2021.napsgfoundation.org/pages/arcade"><i>No Coins Required: Using Arcade to Enhance Your Public Safety Applications</i></a>, so refer to that document for further information on their use and application.

These scrips are kept here as Javascript files. They can still be downloaded as .js files to keep as your reference, but you can also copy/ paste the data from here to your ArcGIS Online environment.
