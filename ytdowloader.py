import customtkinter as ctk
import pytube

def download_video():
    video_url = link.get()
    youtube = pytube.YouTube(video_url)
    if video_url:
        selected_resolution = optionmenu_var.get()
        video = None

        for stream in youtube.streams:
            if stream.resolution == selected_resolution:
                video = stream
                break

        if video:
            video.download()

app = ctk.CTk()

window_width = 450
window_height = 250

screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()

center_x = int(screen_width/2 - screen_width / 2)
center_y = int(screen_height/2 - screen_height / 2)

app.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

link = ctk.CTkEntry(app, placeholder_text="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
link.pack(pady=40, padx=40,ipady=5, ipadx=90)

def optionmenu_callback(choice):
    print("option menu dropdown clicked:", choice)

optionmenu_var = ctk.StringVar(value="720p")

quality = ctk.CTkOptionMenu(app, values=["360p", "720p"], variable=optionmenu_var, command=optionmenu_callback)
quality.pack(ipadx=40)

download_button = ctk.CTkButton(app, text="Download the Video", command=download_video)
download_button.pack(ipadx=40, ipady=7, pady=6)

app.mainloop()