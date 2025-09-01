from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import json
import PyPDF2
from api import convert_text_to_audio


window = Tk()
window.title("Convert Pdf To Audio")
window.config(width=500, height=500)


def read_json_file():
    with open("voices.text", mode="r") as data:
        data_list = json.loads(data.read().strip())  # Parse the JSON content
    return data_list

def values_list():
    return [
        f"{item['name']} gender {item['gender']} {item['accent']} accent ,language {item['language']}"
        for item in read_json_file()
    ]

def pdf_to_text(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
        return text



class TTS:
    def __init__(self, master):
        self.window = master
        self.canvas = Canvas(width=500, height=500)
        self.canvas.place(x=0, y=0)
        self.logo = PhotoImage(file="bac.png")
        self.canvas.create_image(250, 250, image=self.logo)
        self.selected_voice = ""
        self.pdf_text = ""
        self.location_path = ""

        self.open = Button(text="Open", font=("Courier", 15, "normal"), width=10, highlightthickness=0, borderwidth=0, command=self.open_pdf_file)
        self.open.place(x=185, y=210)

        self.location = Button(text="Location", font=("Courier", 15, "normal"), width=10, highlightthickness=0, borderwidth=0, command=self.saved_location)
        self.location.place(x=185, y=315)

        self.convert = Button(text="Convert", font=("Courier", 20, "normal"), width=10, highlightthickness=0, background="#fb5e65", borderwidth=0, command=self.start_convert)
        self.convert.place(x=164, y=380)

        self.voice_type = StringVar()
        self.voice_box = ttk.Combobox(textvariable=self.voice_type, font=("Courier", 12, "normal"), width=40)
        self.voice_box["values"] = tuple(values_list())

        self.voice_box.bind("<<ComboboxSelected>>", self.selected_box)
        self.voice_box.place(x=40, y=270)

    def selected_box(self, event=None):
        self.selected_voice = self.voice_box.get().strip()
        index_voice = values_list().index(self.selected_voice)
        self.selected_voice = read_json_file()[index_voice]["id"]

    def open_pdf_file(self):
        file_path = filedialog.askopenfilename()
        print(file_path)
        if ".pdf" not in file_path:
            messagebox.showerror(title="Format Error", message="You have entered an incorrectly formatted file.")
        else:
            self.pdf_text = pdf_to_text(file_path)

    def saved_location(self):
        self.location_path = filedialog.askdirectory()

    def start_convert(self):
        convert_text_to_audio(self.selected_voice, self.pdf_text, self.location_path)












if __name__ == "__main__":
    tts = TTS(window)
    window.mainloop()