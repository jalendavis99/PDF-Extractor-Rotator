PDF Page Rotator
This is a simple application that allows you to rotate individual pages of a PDF file and save them as separate PDF files. It also provides an option to rotate all the PDF files in a selected folder and save the rotated versions in a separate output folder.

Features
Select a PDF file and a destination folder to save the rotated pages.
Specify the rotation angle in degrees for the pages.
Save each rotated page as a separate PDF file in the destination folder.
Display the total page count of the selected PDF file.
Display the number of saved PDF files in the destination folder.
Rotate all PDF files in a selected folder and save them in a separate output folder.
Show a progress bar during the rotation process.
User-friendly GUI interface.
Requirements
Python 3.7 or higher
PyPDF2 library
Tkinter library
ttkthemes library
Usage
Install the required libraries by running the following command:

Copy code
pip install PyPDF2 tkinter ttkthemes
Run the script using the following command:

Copy code
python pdf_page_rotator.py
The application window will open.

Click the "Browse" button next to "Select PDF file" to choose a PDF file to rotate.
Click the "Browse" button next to "Select Destination Folder" to choose a folder where the rotated PDF pages will be saved.
Enter the rotation angle in degrees in the "Rotation Angle" field (optional).
Click the "Save Pages" button to rotate the pages and save them as individual PDF files.
The progress bar will show the progress of the rotation process.
The "Page Count" field will display the total number of pages in the selected PDF file.
The "Saved Files" field will display the number of PDF files saved in the destination folder.
To rotate all PDF files in a folder, click the "Rotate Folder PDFs" button and select a folder.
Note
The application supports rotating PDF files with angles that are multiples of 90 degrees.
The output files will be saved with names in the format: <original_file_name>_page_<page_number>.pdf.
The application may take some time to rotate and save large PDF files or a large number of PDF files in a folder.