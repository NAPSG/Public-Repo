# Check Webmaps for Broken Layers

The scripts in this folder and designed to check each webmap for any unreachable or broken layers. Before deploying this script, you must create a secrets.csv to hold your webhook URL. This document will explain how to create the secrets.csv. In the future, you can use this same file to hold login information or other webhooks.

#### Create the Secrets CSV
1. Open any software to create an excel sheet (Microsoft Excel, Google Sheets, etc).
2. In the very first cell, type "secret_key" as your first column header.
3. In cell B1, type "secret_value" as your second column header.
4. Place the name of your webhook into cell A3 under secret_key (remember what you put here as you will need to put it into the Check Layers in Webmaps script).
5. Place the webhook URL into cell B2 under secret_value.
6. Save your document as a CSV, naming it "secrets.csv".

#### Upload to ArcGIS Online
1. From your Content page on ArcGIS Online, click New Item.
2. Drag your CSV file into the window.
3. When prompted, select "Add secrets.csv Only" and click Next.
4. Add whatever title, description, and tags you want. Make sure to include something saying what this is so it is not deleted by accident.
5. Click Save to upload the file.

#### Update Secrets.csv
In case you need to update your secrets.csv, either update the webhook URLs or add more, you can follow this workflow.
1. Navigate to the secrets.csv on your ArcGIS Online content.
2. Click Download on the Overview page.
3. Open the secrets.csv on your computer.
4. Make your edits as needed. Save the file.
5. Go back to the secrets.csv on ArcGIS Online and click Update on the Overview page.
6. Select your updated CSV from your computer and click Update Item.
