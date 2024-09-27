# IronSights to Wide Area Search Standalone tool
# Alpha build version 1.2
import arcpy
import customtkinter as ctk
import tkinter as tk
import re
from datetime import date

# Function to handle GPX file selection
def select_gpx_file():
    file_path = tk.filedialog.askopenfilename(title="Select GPX File", filetypes=[("GPX files", "*.gpx")])
    gpx_file_entry.delete(0, ctk.END)
    gpx_file_entry.insert(0, file_path)

# Function to handle database file selection
def select_db_file():
    file_path = tk.filedialog.askdirectory()
    db_file_entry.delete(0, ctk.END)
    db_file_entry.insert(0, file_path)

def tracklog(OutputFeatureClass, team_name, squadID, searchType):
    print("Starting tracklog...")
    stepLabel.configure(text="Running Tracklog")
    with arcpy.da.SearchCursor(fr"{OutputFeatureClass}", 'Type', where_clause="Type = 'TRKPT'") as cursor:
        rows = {row[0] for row in cursor}

    count = 0
    for row in rows:
        count += 1

    if count >= 1:
        pass
    else:
        print("Not enough features to create a tracklog")
        return
    arcpy.management.SelectLayerByAttribute(
        in_layer_or_view=fr"{OutputFeatureClass}",
        selection_type="NEW_SELECTION",
        where_clause="Type = 'TRKPT'",
        invert_where_clause=None
    )
    arcpy.management.PointsToLine(
        Input_Features=fr"{OutputFeatureClass}",
        Output_Feature_Class=f"{OutputFeatureClass}_Tracklog",
        Line_Field="Name",
        Sort_Field="DateTimeS",
        Close_Line="NO_CLOSE",
        Line_Construction_Method="CONTINUOUS",
        Attribute_Source="NONE",
        Transfer_Fields=None
    )
    with arcpy.da.UpdateCursor(fr"{OutputFeatureClass}", 'Type', where_clause="Type = 'TRKPT'") as cursor:
        for row in cursor:
            cursor.deleteRow()

    print("Adding Attributes")
    stepLabel.configure(text="Creating Tracklog Attributes")
    team_name = f'"{team_name}"'
    arcpy.management.CalculateField(
        in_table=f"{OutputFeatureClass}_Tracklog",
        field="team_name",
        expression=team_name,
        expression_type="PYTHON3",
        code_block="",
        field_type="TEXT",
        enforce_domains="NO_ENFORCE_DOMAINS"
    )

    arcpy.management.CalculateField(
        in_table=f"{OutputFeatureClass}_Tracklog",
        field="squad_id",
        expression=squadID,
        expression_type="PYTHON3",
        code_block="",
        field_type="LONG",
        enforce_domains="NO_ENFORCE_DOMAINS"
    )

    searchType = f'"{searchType}"'
    arcpy.management.CalculateField(
        in_table=f"{OutputFeatureClass}_Tracklog",
        field="mission_type",
        expression=searchType,
        expression_type="PYTHON3",
        code_block="",
        field_type="TEXT",
        enforce_domains="NO_ENFORCE_DOMAINS"
    )


    arcpy.management.CalculateField(
        in_table=f"{OutputFeatureClass}_Tracklog",
        field="data_source",
        expression='"GPS"',
        expression_type="PYTHON3",
        code_block="",
        field_type="TEXT",
        enforce_domains="NO_ENFORCE_DOMAINS"
    )

    arcpy.management.CalculateField(
        in_table=f"{OutputFeatureClass}_Tracklog",
        field="delete_this",
        expression='"No"',
        expression_type="PYTHON3",
        code_block="",
        field_type="TEXT",
        enforce_domains="NO_ENFORCE_DOMAINS"
    )
    print("Tracklog Complete")
    stepLabel.configure(text="Tracklog Complete")

def waypoint(OutputFeatureClass, team_name, squadID, searchType):
    print("Starting Waypoint processing")
    stepLabel.configure(text="Starting Waypoint processing")
    with arcpy.da.SearchCursor(fr"{OutputFeatureClass}", 'Type', where_clause="Type = 'WPT'") as cursor:
        rows = {row[0] for row in cursor}
    count = 0
    for row in rows:
        count += 1
    if count >= 1:
        pass
    else:
        print("No waypoint features collected")
        return
    stepLabel.configure(text="Configuring Waypoints")
    team_name = f'"{team_name}"'
    arcpy.management.CalculateField(
        in_table=f"{OutputFeatureClass}",
        field="team_name",
        expression=team_name,
        expression_type="PYTHON3",
        code_block="",
        field_type="TEXT",
        enforce_domains="NO_ENFORCE_DOMAINS"
    )

    arcpy.management.CalculateField(
        in_table=f"{OutputFeatureClass}",
        field="squad_id",
        expression=squadID,
        expression_type="PYTHON3",
        code_block="",
        field_type="LONG",
        enforce_domains="NO_ENFORCE_DOMAINS"
    )
    searchType = f'"{searchType}"'
    arcpy.management.CalculateField(
        in_table=f"{OutputFeatureClass}",
        field="mission_type",
        expression=searchType,
        expression_type="PYTHON3",
        code_block="",
        field_type="TEXT",
        enforce_domains="NO_ENFORCE_DOMAINS"
    )

    arcpy.management.CalculateField(
        in_table=f"{OutputFeatureClass}",
        field="Symbol",
        expression="updatevalue(!Symbol!)",
        expression_type="PYTHON3",
        code_block="""def updatevalue(value):
        if value == "Custom 0":
            return "unaffected"
        if value == "Custom 1":
            return "minor"
        if value == "Custom 2":
            return "major"
        if value == "Custom 3":
            return "destroyed"
        if value == "Custom 4":
            return "assist"
        if value == "Custom 5":
            return "evac"
        if value == "Custom 6":
            return "rescue"
        if value == "Custom 7":
            return ""
        if value == "Custom 8":
            return "detect"
        if value == "Custom 9":
            return "confirm"
        if value == "Custom 10":
            return "remains_detected"
        if value == "Custom 11":
            return "remains"
        if value == "Custom 12":
            return "removed"
        if value == "Custom 13":
            return "animal"
        if value == "Custom 14":
            return "fire"
        if value == "Custom 15":
            return "flood"
        if value == "Custom 16":
            return "hazmat"
        if value == "Custom 17":
            return "flood"
        if value == "Custom 18":
            return "heli"
        if value == "Custom 19":
            return "block"
        if value == "Custom 20":
            return "extra21"
        if value == "Custom 21":
            return "extra22"
        if value == "Custom 22":
            return "extra23"
        if value == "Custom 23":
            return "extra24" """,
        field_type="TEXT",
        enforce_domains="NO_ENFORCE_DOMAINS"
    )

    arcpy.management.CalculateField(
        in_table=f"{OutputFeatureClass}",
        field="data_source",
        expression='"GPS"',
        expression_type="PYTHON3",
        code_block="",
        field_type="TEXT",
        enforce_domains="NO_ENFORCE_DOMAINS"
    )

    arcpy.management.CalculateField(
        in_table=f"{OutputFeatureClass}",
        field="delete_this",
        expression='"No"',
        expression_type="PYTHON3",
        code_block="",
        field_type="TEXT",
        enforce_domains="NO_ENFORCE_DOMAINS"
    )

    arcpy.management.CalculateGeometryAttributes(
        in_features=f"{OutputFeatureClass}",
        geometry_property="MGRS POINT_COORD_NOTATION",
        length_unit="",
        area_unit="",
        coordinate_system=None,
        coordinate_format="MGRS"
    )

    arcpy.management.CalculateField(
        in_table=f"{OutputFeatureClass}",
        field="followup_status",
        expression="updatevalue(!Symbol!)",
        expression_type="PYTHON3",
        code_block="""def updatevalue(value):
        if "detect" or "confirm" or "remains_detected" or "remains" or "search":
            return "needs_followup"
        else:
            print("None")
        """,
        field_type="TEXT",
        enforce_domains="NO_ENFORCE_DOMAINS"
    )
    print("Waypoints complete")
    stepLabel.configure(text="Waypoints Complete")

def close(OutputFeatureClass):
    boxMessage = f"Script complete, Here is your database:\n\n{OutputFeatureClass}\n\nDo you want to close the tool?"
    close = tk.messagebox.askyesno("Script Complete", boxMessage)
    if close == True:
        app.destroy()

    elif close == False:
        gpx_file_entry.delete(0, 'end')
        squad_id_entry.delete(0, 'end')
        search_type_dropdown.set("Hasty")
        wptVar.set('on')
        TRKPTVar.set('on')
    else:
        pass

def clear():
        gpx_file_entry.delete(0, 'end')
        db_file_entry.delete(0, 'end')
        team_name_entry.delete(0, 'end')
        squad_id_entry.delete(0, 'end')
        search_type_dropdown.set("Hasty")



def main(stepLabel, inputGPX, outputGDB, team_name, squadID, searchType, wptVar,TRKPTVar):
    today = date.today().strftime('%Y%m%d')
    characters_to_replace = [' ', '-', '(', ')', '/']
    for char in characters_to_replace:
        team_name = team_name.replace(char, "")
    special_chars_regex = r"[^\d_]"
    if re.search(special_chars_regex, squadID):
        print(wptVar)
        print(TRKPTVar)
        tk.messagebox.showerror("Squad ID Error", "Squad ID must be a number.")
        return
    OutputFeatureClass = fr"{outputGDB}\{searchType}_{today}_{team_name}_Squad{squadID}"
    print("Creating Features")
    try:
        arcpy.conversion.GPXtoFeatures(
            Input_GPX_File=fr"{inputGPX}",
            Output_Feature_class=fr"{OutputFeatureClass}",
            Output_Type="POINTS"
        )
    except:
        tk.messagebox.showerror("Create features error", "There was an error creating features, the feature layer likely already exists. Modify the parameters and try again.")
        return
    if TRKPTVar == 'on':
        
        tracklog(OutputFeatureClass, team_name, squadID, searchType)
    if wptVar == 'on':
        waypoint(OutputFeatureClass, team_name, squadID, searchType)
    close(OutputFeatureClass)



# Initialize CustomTkinter window
ctk.set_appearance_mode("System")  # Modes: "System" (default), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (default), "dark-blue", "green"

app = ctk.CTk()  
app.geometry("500x500")
app.title("IronSights Tool v1.2")

stepLabel = ctk.CTkLabel(app, text="")
stepLabel.grid(row=11, column=1, pady=10)

label = ctk.CTkLabel(app, text="Place in the parameters")
label.grid(row=0, column=1, padx=20, pady=10, sticky="e")

gpx_label = ctk.CTkLabel(app, text="GPX File:")
gpx_label.grid(row=1, column=0, padx=20, pady=10, sticky="e")
gpx_file_entry = ctk.CTkEntry(app, placeholder_text="Select GPX File")
gpx_file_entry.grid(row=1, column=1, padx=20, pady=10)
gpx_file_button = ctk.CTkButton(app, text="Browse", command=select_gpx_file)
gpx_file_button.grid(row=1, column=2, padx=10, pady=10)

db_label = ctk.CTkLabel(app, text="Database File:")
db_label.grid(row=2, column=0, padx=20, pady=10, sticky="e")
db_file_entry = ctk.CTkEntry(app, placeholder_text="Select or Create Geodatabase")
db_file_entry.grid(row=2, column=1, padx=20, pady=10)
db_file_button = ctk.CTkButton(app, text="Browse", command=select_db_file)
db_file_button.grid(row=2, column=2, padx=0, pady=0)

# Widgets for the form
team_label = ctk.CTkLabel(app, text="Team Name:")
team_label.grid(row=3, column=0, padx=20, pady=10, sticky="e")
team_name_entry = ctk.CTkEntry(app, placeholder_text="Enter Team Name")
team_name_entry.grid(row=3, column=1, padx=20, pady=10)

squad_label = ctk.CTkLabel(app, text="Squad ID:")
squad_label.grid(row=4, column=0, padx=20, pady=10, sticky="e")
squad_id_entry = ctk.CTkEntry(app, placeholder_text="Enter Squad ID")
squad_id_entry.grid(row=4, column=1, padx=20, pady=10)


# Dropdown for search type
search_label = ctk.CTkLabel(app, text="Search Type:")
search_label.grid(row=5, column=0, padx=20, pady=10, sticky="e")
search_type_var = ctk.StringVar(value="Hasty")
search_type_dropdown = ctk.CTkComboBox(app, values=["Hasty", "Primary", "Secondary", "Targeted"], variable=search_type_var)
search_type_dropdown.grid(row=5, column=1, padx=20, pady=10)


wptVar = ctk.StringVar(value="on")
wyptswitch = ctk.CTkSwitch(app, text="Process Waypoints",variable=wptVar, onvalue="on", offvalue="off")
wyptswitch.grid(row=6, column=1, padx=5, pady=5)


TRKPTVar = ctk.StringVar(value="on")
TRKPTVarswitch = ctk.CTkSwitch(app, text="Process Tracklogs",variable=TRKPTVar, onvalue="on", offvalue="off")
TRKPTVarswitch.grid(row=7, column=1, padx=10, pady=5)

clear_button = ctk.CTkButton(app, text="Clear",fg_color='white', text_color='gray', command=lambda:clear())
clear_button.grid(row=8, column=1, padx=10, pady=10)
# Submit button
submit_button = ctk.CTkButton(app, text="Run", command=lambda:main(stepLabel,gpx_file_entry.get(),db_file_entry.get(),team_name_entry.get(),squad_id_entry.get(),search_type_var.get(),wptVar.get(),TRKPTVar.get()))
submit_button.grid(row=9, column=1)


# Start the main loop
app.mainloop()