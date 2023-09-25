import customtkinter
from tkinter import PhotoImage
from mainform import MainApplication
import mysql.connector
import tkinter.messagebox


class login(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        customtkinter.set_appearance_mode("System")
        customtkinter.set_default_color_theme("green")

        self.geometry("500x350")
        self.title("Se connecter")
        icon = PhotoImage(file='Photo/coins.png')
        self.iconphoto(False, icon)

        frame = customtkinter.CTkFrame(master=self)
        frame.pack(pady=20, padx=60, fill="both", expand=True)

        label = customtkinter.CTkLabel(master=frame, text="Se connecter", font=("Roboto", 24))
        label.pack(pady=12, padx=10)

        self.entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Nom d'utilisateur")
        self.entry1.pack(pady=12, padx=10)

        self.entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Mot de passe", show="*")
        self.entry2.pack(pady=12, padx=10)

        buttonlogin = customtkinter.CTkButton(master=frame, text="Se connecter", command=self.login)
        buttonlogin.pack(pady=12, padx=10)


    def login(self):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="selection_db"
            )

            cursor = conn.cursor()

            # Get username and password from the database
            query = "SELECT username, password FROM users WHERE username = %s"
            cursor.execute(query, (self.entry1.get(),))
            result = cursor.fetchone()

            if result:
                username, db_password = result
                entered_password = self.entry2.get()

                if entered_password == db_password:
                    print("Login successful")
                    self.open_main_window()
                else:
                    print("Incorrect password")
            else:
                tkinter.messagebox.showwarning("Utilisateur non trouvé", "Utilisateur non trouvé")

            cursor.close()
            conn.close()
        except mysql.connector.Error as err:
            tkinter.messagebox.showerror("Erreur de la base de données", f"Erreur: {err}")

    def open_main_window(self):
        self.destroy()
        main_window = MainApplication()
        main_window.mainloop()





