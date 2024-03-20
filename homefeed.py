import tkinter as tk

class SwiftgramHomeFeedPage:  #the basic idea is that people can view and post pictures and videos online and also like, comment and share them
    def __init__(self, master):
        self.master = master
        master.title("Swiftgram - Home Feed")
        master.geometry("600x600")  # Set window size
        master.configure(bg="#fafafa")  # Background color

        # Top toolbar
        self.toolbar_frame = tk.Frame(master, bg="#FF6B6B")  
        self.toolbar_frame.pack(side=tk.TOP, fill=tk.X)

        self.logo_label = tk.Label(self.toolbar_frame, text="Swiftgram", font=("Helvetica", 24, "bold"), bg="#FF6B6B", fg="#ffffff")  
        self.logo_label.pack(side=tk.LEFT, padx=10)

        self.search_entry = tk.Entry(self.toolbar_frame, width=30, bg="#ffffff")  
        self.search_entry.pack(side=tk.LEFT, padx=10)

        self.search_button = tk.Button(self.toolbar_frame, text="Search", bg="#ffffff", fg="#FF6B6B", relief=tk.FLAT)  
        self.search_button.pack(side=tk.LEFT, padx=10)

        # Main content frame
        self.main_frame = tk.Frame(master, bg="#fafafa")  
        self.main_frame.pack(expand=True, fill=tk.BOTH)

        # Create multiple posts
        for i in range(3):
            self.create_post("User " + str(i), "Post content " + str(i))

    def create_post(self, username, content):
        post_frame = tk.Frame(self.main_frame, bg="#ffffff", bd=1, relief=tk.RIDGE)
        post_frame.pack(pady=10, padx=10, fill=tk.BOTH)                          

        post_user_label = tk.Label(post_frame, text=username, font=("Helvetica", 12, "bold"), bg="#ffffff", fg="#000000")
        post_user_label.pack(anchor=tk.W, padx=10, pady=5)

        post_content_label = tk.Label(post_frame, text=content, bg="#ffffff")
        post_content_label.pack(padx=10, pady=5)

        post_like_button = tk.Button(post_frame, text="Like", bg="#ffffff", fg="#FF6B6B", relief=tk.FLAT, command=lambda: self.like_post(post_like_button))
        post_like_button.pack(side=tk.LEFT, padx=10)

        post_comment_button = tk.Button(post_frame, text="Comment", bg="#ffffff", fg="#FF6B6B", relief=tk.FLAT, command=lambda: self.comment_post(post_comment_button))
        post_comment_button.pack(side=tk.LEFT, padx=10)

        post_share_button = tk.Button(post_frame, text="Share", bg="#ffffff", fg="#FF6B6B", relief=tk.FLAT, command=lambda: self.share_post(post_share_button))
        post_share_button.pack(side=tk.LEFT, padx=10)

    def like_post(self, button):
        button.config(text="Liked")

    def comment_post(self, button):
        button.config(text="Commented")

    def share_post(self, button):
        button.config(text="Shared")

def main():
    root = tk.Tk()
    app = SwiftgramHomeFeedPage(root)
    root.mainloop()

if __name__ == "__main__":
    main()
