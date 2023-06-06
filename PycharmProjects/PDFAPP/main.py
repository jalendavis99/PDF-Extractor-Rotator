import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfReader, PdfWriter
import tkinter.ttk as ttk
from ttkthemes import ThemedTk

def rotate_pdf_pages(input_path, output_path):
    with open(input_path, 'rb') as file:
        reader = PdfReader(file)
        writer = PdfWriter()

        for page in reader.pages:
            page.rotate(180)
            writer.add_page(page)

        with open(output_path, 'wb') as output_file:
            writer.write(output_file)

def select_pdf():
    try:
        file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if file_path:
            pdf_entry.delete(0, tk.END)
            pdf_entry.insert(0, file_path)
            update_page_count()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def select_folder():
    try:
        folder_path = filedialog.askdirectory()
        if folder_path:
            folder_entry.delete(0, tk.END)
            folder_entry.insert(0, folder_path)
            update_saved_files_count()
            update_pdf_count()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def save_pages():
    try:
        pdf_file_path = pdf_entry.get()
        folder_path = folder_entry.get()
        rotation_angle = rotation_entry.get()
        file_base_name = os.path.splitext(os.path.basename(pdf_file_path))[0]

        pdf = PdfReader(pdf_file_path)

        # Set the maximum value of the progress bar
        progress["maximum"] = len(pdf.pages)

        for page_num in range(len(pdf.pages)):
            pdf_writer = PdfWriter()
            page = pdf.pages[page_num]
            if rotation_angle:
                rotation = int(rotation_angle) % 360
                if rotation % 90 != 0:
                    messagebox.showerror("Invalid Rotation Angle", "Rotation angle must be a multiple of 90")
                    return
                page.rotate(rotation)
            pdf_writer.add_page(page)

            output_path = os.path.join(folder_path, f"{file_base_name}_page_{page_num+1}.pdf")
            with open(output_path, 'wb') as f:
                pdf_writer.write(f)

            # Update the progress bar
            progress["value"] = page_num + 1
            window.update_idletasks()  # Refresh the GUI to display the updated progress

        messagebox.showinfo("Save Complete", "Individual pages saved successfully!")
        update_saved_files_count()

        # Reset the progress bar
        progress["value"] = 0

    except Exception as e:
        messagebox.showerror("Error", str(e))

def update_page_count():
    pdf_file_path = pdf_entry.get()
    if pdf_file_path:
        pdf = PdfReader(pdf_file_path)
        page_count = len(pdf.pages)
        page_count_var.set(str(page_count))
    else:
        page_count_var.set("0")

def update_saved_files_count():
    folder_path = folder_entry.get()
    if folder_path:
        files = [f for f in os.listdir(folder_path) if f.endswith(".pdf")]
        saved_files_count = len(files)
        saved_files_var.set(str(saved_files_count))
    else:
        saved_files_var.set("0")

def update_pdf_count():
    folder_path = folder_entry.get()
    if folder_path:
        pdf_files = [f for f in os.listdir(folder_path) if f.endswith(".pdf")]
        pdf_count = len(pdf_files)
        pdf_count_var.set(str(pdf_count))
    else:
        pdf_count_var.set("0")

def update_save_button_state(*args):
    pdf_path = pdf_entry.get()
    folder_path = folder_entry.get()

    if pdf_path and folder_path:
        save_button.config(state="normal")
    else:
        save_button.config(state="disabled")

def rotate_folder_pdfs():
    folder_path = filedialog.askdirectory(title='Select Folder')

    if folder_path:
        output_folder = os.path.join(folder_path, 'rotated')
        os.makedirs(output_folder, exist_ok=True)

        for filename in os.listdir(folder_path):
            if filename.endswith('.pdf'):
                input_path = os.path.join(folder_path, filename)
                output_path = os.path.join(output_folder, filename)
                rotate_pdf_pages(input_path, output_path)
                print(f'Rotated: {filename}')

        print('PDF rotation completed.')
        messagebox.showinfo("Folder Rotation Complete", "PDFs in the folder have been rotated successfully.")
        update_saved_files_count()
        update_pdf_count()

# Create the main window
window = ThemedTk(theme="arc")
window.title("PDF Page Extractor")

# Configure window size and padding
window.geometry("700x350")
window.configure(padx=20, pady=20)

# Create the PDF selection label and entry
pdf_label = ttk.Label(window, text="Select PDF file:")
pdf_label.grid(row=0, column=0, sticky="w")

pdf_entry_var = tk.StringVar()
pdf_entry = ttk.Entry(window, width=40, textvariable=pdf_entry_var)
pdf_entry.grid(row=0, column=1, padx=10)

pdf_button = ttk.Button(window, text="Browse", command=select_pdf)
pdf_button.grid(row=0, column=2, padx=10)

# Create the folder selection label and entry
folder_label = ttk.Label(window, text="Select Destination Folder:")
folder_label.grid(row=1, column=0, sticky="w")

folder_entry_var = tk.StringVar()
folder_entry = ttk.Entry(window, width=40, textvariable=folder_entry_var)
folder_entry.grid(row=1, column=1, padx=10)

folder_button = ttk.Button(window, text="Browse", command=select_folder)
folder_button.grid(row=1, column=2, padx=10)

# Create the rotation label and entry
rotation_label = ttk.Label(window, text="Rotation Angle (in degrees):")
rotation_label.grid(row=2, column=0, sticky="w")

rotation_entry = ttk.Entry(window, width=40)
rotation_entry.grid(row=2, column=1, padx=10)

# Create the save button
save_button = ttk.Button(window, text="Save Pages", command=save_pages, state="disabled")
save_button.grid(row=3, column=0, columnspan=3, pady=10)

# Create the page count label and value
page_count_label = ttk.Label(window, text="Page Count:")
page_count_label.grid(row=4, column=0, sticky="w")

page_count_var = tk.StringVar()
page_count_value_label = ttk.Label(window, textvariable=page_count_var)
page_count_value_label.grid(row=4, column=1, sticky="w")

# Create the saved files count label and value
saved_files_label = ttk.Label(window, text="Saved Files:")
saved_files_label.grid(row=5, column=0, sticky="w")

saved_files_var = tk.StringVar()
saved_files_value_label = ttk.Label(window, textvariable=saved_files_var)
saved_files_value_label.grid(row=5, column=1, sticky="w")

# Create the PDF count label and value
pdf_count_label = ttk.Label(window, text="PDF Count:")
pdf_count_label.grid(row=6, column=0, sticky="w")

pdf_count_var = tk.StringVar()
pdf_count_value_label = ttk.Label(window, textvariable=pdf_count_var)
pdf_count_value_label.grid(row=6, column=1, sticky="w")

# Create the progress bar
progress = ttk.Progressbar(window, mode="determinate")
progress.grid(row=7, column=0, columnspan=3, pady=10, padx=10)

# Bind functions to update fields and button state
pdf_entry_var.trace_add("write", update_save_button_state)
folder_entry_var.trace_add("write", update_save_button_state)

# Disable the save button initially
save_button.config(state="disabled")

# Create the folder rotation button
folder_rotate_button = ttk.Button(window, text="Rotate Folder PDFs", command=rotate_folder_pdfs)
folder_rotate_button.grid(row=8, column=0, columnspan=3, pady=10)

# Start the main event loop
window.mainloop()
