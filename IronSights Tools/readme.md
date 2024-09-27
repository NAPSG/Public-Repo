## Use
This tool is designed to take data from IronSights and convert it into a feature class that can later be appended to the Search and Rescue Common Operating Platform (SARCOP). It is open-sourced and available to the public.

## Limitations and Requirements
#### Alpha Build version 1.2
This script is currently in an alpha build and, while functional, is not a very user-friendly experience. Users will find that when running the script, nothing appears to happen in the GUI. For this, you will need to utilize the counsel window that opens with the tool to see what the tool is doing. 

<img src=https://github.com/NAPSG/Public-Code/blob/7e72133c37c112ca6fcdb6329401908da3f9ff75/IronSights%20Tools/Mis/RunningScreenshot.png>

The script also does not look for geodatabases specifically, and the input will need to be in a folder with the ".gdb" extension in the name. Any other directory input will cause the tool to fail.

#### Pro Requirements
This tool requires ArcGIS Pro to be installed on the machine you are running this script from. ArcGIS Pro does not need to be running for the tool to work, but it must be at least installed and set up. This tool utilizes the ArcPy Python library that comes with ArcGIS Pro and runs in the Python environment with the software.

#### Pro Environment Clone
For this tool to work with a batch file and desktop shortcut, you will need to <a href="https://pro.arcgis.com/en/pro-app/latest/arcpy/get-started/clone-an-environment.htm">clone your ArcGIS Pro Python environment</a> because the default environment does not allow for the installation of outside Python packages or libraries. The primary library to create the GUI is "Custom TKinter," which is a library not installed by default in the Python environment in ArcGIS Pro. This library can be installed following the steps in this article: <a href="https://www.linkedin.com/pulse/how-add-python-packages-arcgis-pro-rhys-donoghue-evohc/">https://www.linkedin.com/pulse/how-add-python-packages-arcgis-pro-rhys-donoghue-evohc/</a>

## Create Batch File and Shortcut
There are a few ways to run this, but I have found the most user-friendly way for non-GIS personnel is to run it from a desktop shortcut attached to a Windows batch File (.bat file). Creating a batch file is easy:
1. Create a new text file anywhere on your PC
2. Follow the same format as the RUNIronSights2WAS_A12.bat file in this repo to set up the location of the python environment and file location
    - The python environment should point back to your cloned environment which will look something like "C:\Users\yourusername\AppData\Local\ESRI\conda\envs\arcgispro-py3-clone\python.exe"
3. Save your text file and change the file's extension from ".txt" to ".bat"
4. Double-clicking on the batch file should open the tool as expected. It does take a second to open because ArcPy needs to be verified

<img src="https://github.com/NAPSG/Public-Code/blob/7e72133c37c112ca6fcdb6329401908da3f9ff75/IronSights%20Tools/Mis/BatFileScreenshot.png">

Note if you have issues opening the file, try disabling your antivirus. 
## Future Development Roadmap
There are many planned updates to this script including the following:
- Filter out any directory or file that is not a Geodatabase
- Create new geodatabasse if one is not selected
- Progress or running bar beneath buttons to tell the user that the tool is running
- Progress messages within the tool's GUI window to eliminate need for counsel window to remain open
- Symbol field calculates to a default value if the input GPX file does not had a compatible symbol field
- Open geodatabase location upon tool completion
- Auto append data from the tool into SARCOP

The current goal is to complete all these tasks by March of 2025
