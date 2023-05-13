import tkinter as tk
from tkinter import filedialog
import PyPDF2


class PDFMerger:
    def __init__(self, master):
        self.master = master
        master.title("PDF Merger")

        master.geometry("350x150")
        master.config(bg="#f2f2f2")

        master.resizable(False, False)

        self.files = []
        self.file_selector_button = tk.Button(
            master,
            text="Select Files",
            command=self.select_files,
            bg="#1E90FF",
            fg="#FFFFFF",
            activebackground="#1E90AF",
            activeforeground="#1E90FF",
            padx=10,
            pady=4,
            border=1,
        )
        self.file_selector_button.pack()

        self.merge_button = tk.Button(
            master,
            text="Merge",
            command=self.merge_files,
            bg="green",
            fg="#FFFFFF",
            activebackground="#FFFFFF",
            activeforeground="#1E90FF",
            padx=10,
            pady=4,
            border=1,
        )
        self.file_label = tk.Label(master, text="")
        self.file_label.pack()

        self.merge_button.pack(pady=(20, 30))

    def select_files(self):
        file = None
        file = filedialog.askopenfilenames(
            initialdir="\\Desktop",
            title="Select Files",
            filetypes=(("PDF files", "*.pdf"), ("all files", "*.*")),
        )[0]

        print(file)

        if (file != None):

            self.files.append(file)

        if len(self.files) > 0:
            self.file_label.config(
                text="Selected files: \n" + "\n".join(self.files))

    def merge_files(self):
        if len(self.files) > 0:

            merged_destination = filedialog.asksaveasfilename()

            merger = PyPDF2.PdfWriter()
            print(self.files)
            for pdf in self.files:
                merger.append(pdf)

            merger.write(merged_destination)
            merger.close()
            print("Files merged successfully!")

        else:
            print("No files selected!")


root = tk.Tk()
pdf_merger = PDFMerger(root)
root.mainloop()
