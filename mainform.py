import customtkinter
from tkinter import filedialog , PhotoImage

class MainApplication(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        customtkinter.set_appearance_mode("System")
        customtkinter.set_default_color_theme("blue")

        
        self.geometry("800x600")
        self.title("Main Application")
    

        frame = customtkinter.CTkFrame(master=self)
        frame.pack(pady=10, padx=10, fill="both", expand=True)


        buttonimportimage = customtkinter.CTkButton(master=frame, text="Add Image", command=self.add_Image)
        buttonimportimage.pack(pady=12, padx=10)
    def add_Image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.png;*.gif")])
        if file_path:
            image = PhotoImage(file=file_path)
            image_label = customtkinter.CTkLabel(self, image=image)
            image_label.image = image
            image_label.pack(in_=self.frame, pady=10, padx=10)


