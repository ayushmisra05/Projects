import os
import shutil
import tkinter as tk
from tkinter import filedialog

def organize_files():
    source_path = source_path_var.get()
    file_names = os.listdir(source_path)

    folder_names = ['pdf files', 'image files', 'text files', 'video files', 'docx files', 'exe files']

    for folder_name in folder_names:
        folder_path = os.path.join(source_path, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    for file_name in file_names:
        try:
            # PDF FILES
            if ".pdf" in file_name and not os.path.exists(os.path.join(source_path, "pdf files", file_name)):
                shutil.move(os.path.join(source_path, file_name), os.path.join(source_path, "pdf files", file_name))
                output_text.insert(tk.END, f"PDF Files Moved Successfully: {file_name}\n")
            # IMAGE FILES (PNG, JPG, WEBP, GIF)
            if any(ext in file_name for ext in [".png", ".jpg", ".webp", ".gif", ".HEIC"]) and not os.path.exists(os.path.join(source_path, "image files", file_name)):
                shutil.move(os.path.join(source_path, file_name), os.path.join(source_path, "image files", file_name))
                output_text.insert(tk.END, f"Image Files Moved Successfully: {file_name}\n")
            # TEXT FILES (TXT)
            if ".txt" in file_name and not os.path.exists(os.path.join(source_path, "text files", file_name)):
                shutil.move(os.path.join(source_path, file_name), os.path.join(source_path, "text files", file_name))
                output_text.insert(tk.END, f"Text Files Moved Successfully: {file_name}\n")
            # VIDEO FILES (MP4, MP3, MOV)
            if any(ext in file_name for ext in [".mp4", ".mp3", ".mov", ".bak", ".sfk"]) and not os.path.exists(os.path.join(source_path, "video files", file_name)):
                shutil.move(os.path.join(source_path, file_name), os.path.join(source_path, "video files", file_name))
                output_text.insert(tk.END, f"Video Files Moved Successfully: {file_name}\n")
            # EXE FILES (EXE, ZIP)
            if any(ext in file_name for ext in [".exe", ".zip"]) and not os.path.exists(os.path.join(source_path, "exe files", file_name)):
                shutil.move(os.path.join(source_path, file_name), os.path.join(source_path, "exe files", file_name))
                output_text.insert(tk.END, f"Installer Files Moved Successfully: {file_name}\n")
            if ".docx" in file_name and not os.path.exists(os.path.join(source_path, "docx files", file_name)):
                shutil.move(os.path.join(source_path, file_name), os.path.join(source_path, "docx files", file_name))
                output_text.insert(tk.END, f"Microsoft Word Files Moved Successfully: {file_name}\n")
        except FileNotFoundError as err:
            output_text.insert(tk.END, f"Error: {err}\n")

    output_text.insert(tk.END, "All Provided Files Moved Successfully!\n")

def browse_folder():
    folder_selected = filedialog.askdirectory()
    source_path_var.set(folder_selected)

#GUI START
root = tk.Tk()
root.title("File Organizer")


source_path_var = tk.StringVar()


label_source = tk.Label(root, text="Select Source Folder:")
label_source.grid(row=0, column=0, padx=10, pady=10)

entry_source = tk.Entry(root, textvariable=source_path_var, width=50)
entry_source.grid(row=0, column=1, padx=10, pady=10)

button_browse = tk.Button(root, text="Browse", command=browse_folder)
button_browse.grid(row=0, column=2, padx=10, pady=10)

button_organize = tk.Button(root, text="Organize Files", command=organize_files)
button_organize.grid(row=1, column=0, columnspan=3, pady=10)

output_text = tk.Text(root, height=10, width=60)
output_text.grid(row=2, column=0, columnspan=3, padx=10, pady=10)


root.mainloop()
