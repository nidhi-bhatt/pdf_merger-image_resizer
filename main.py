import tkinter as tk
from tkinter import messagebox
import PyPDF2
import cv2


def pdf_merger():
    pdfiles = ["1.pdf", "2.pdf"]
    merger = PyPDF2.PdfMerger()

    for filename in pdfiles:
        pdfFile = open(filename, 'rb')
        pdfcurrent = PyPDF2.PdfReader(pdfFile)
        merger.append(pdfcurrent)

    pdfFile.close()
    merger.write("merged.pdf")
    messagebox.showinfo("Pdf Merger", "Done!")


def image_resizer():
    source = "hey.jpg"
    destination = "newImage.jpg"
    scale_percent = 50

    src = cv2.imread(source, cv2.IMREAD_UNCHANGED)
    # cv2.imshow("Original",src)
    cv2.waitKey(0)

    # calculate the new dimension

    width = int(src.shape[1] * scale_percent/100)
    height = int(src.shape[0] * scale_percent/100)

    # dsize
    dsize = (width, height)

    # resize image
    output = cv2.resize(src, dsize)
    cv2.imwrite(destination, output)
    cv2.waitKey(0)
    messagebox.showinfo("Image resizer", "Done!")


root = tk.Tk()
root.title("Welcome to MorphMerge!")
root.configure(bg="lightgray")

label = tk.Label(
    root, text="Please choose which operation you want to perform:")
label.pack(pady=10)

button1 = tk.Button(root, text="PdfMerger", command=pdf_merger, width=100)
button1.pack()

button2 = tk.Button(root, text="ImageResizer",
                    command=image_resizer, width=100)
button2.pack(pady=10)


root.mainloop()
