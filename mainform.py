import customtkinter

class MainApplication(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        customtkinter.set_appearance_mode("System")
        customtkinter.set_default_color_theme("blue")
        


        self.geometry("800x600")
        self.title("Main Application")