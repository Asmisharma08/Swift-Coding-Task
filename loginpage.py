import tkinter as tk
from tkinter import messagebox      #i tried learning flutter but it was impossible to do it so soon so i did it like this on vs code
import re                                                    

class SwiftgramLoginPage:
    def __init__(self, master):
        self.master = master
        master.title("Swiftgram Clone - Login")
        master.configure(bg="#FF6B6B")  # Background color (pink)

        # Swiftgram logo
        self.logo_label = tk.Label(master, text="Swiftgram", font=("Helvetica", 24, "bold"), bg="#FF6B6B", fg="#ffffff")  # Text color (white)
        self.logo_label.pack(pady=20)

        # Username entry
        self.username_label = tk.Label(master, text="Username:", bg="#FF6B6B", fg="#ffffff")       #pink and orange colour mainly has been chosen to trying to duplicate instagram
        self.username_label.pack()

        self.username_entry = tk.Entry(master, width=30)
        self.username_entry.pack()

        # Password entry
        self.password_label = tk.Label(master, text="Password:", bg="#FF6B6B", fg="#ffffff")
        self.password_label.pack()

        self.password_entry = tk.Entry(master, show="*", width=30)
        self.password_entry.pack()

        # Login button
        self.login_button = tk.Button(master, text="Login", command=self.login, bg="#FFA07A", fg="#ffffff")  # Background color (orange), text color (white)
        self.login_button.pack(pady=10)

    def validate_username(self, username):
        if len(username) != 8:
            return "Username must be 8 characters long."
        if not any(char.isupper() for char in username):
            return "Username must include at least one uppercase letter."                 #these are the conditions for the username 
        if not any(char.islower() for char in username):
            return "Username must include at least one lowercase letter."
        if not any(char in "!@#$%^&*()-_+=<>?/:;" for char in username):
            return "Username must include at least one special character."
        return None

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Validate username
        username_error = self.validate_username(username)
        if username_error:
            messagebox.showerror("Validation Error", username_error)
            return

        # Check if username and password are valid 
        if username == "admin" and password == "password":
            messagebox.showinfo("Login Successful", "Welcome to Swiftgram, " + username + "!")
            # Close the login window and open the main Swiftgram clone window here
            self.master.destroy()
            # Code for opening the main Swiftgram clone window goes here
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

def main():
    root = tk.Tk()
    app = SwiftgramLoginPage(root)
    root.mainloop()

if __name__ == "__main__":
    main()
