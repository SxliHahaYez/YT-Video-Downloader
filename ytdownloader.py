# Import the needed packages
import os
import pytube
import customtkinter as ctk
import tkinter as tk

# The core of the app
app = ctk.CTk()
app.title("YT Downloader")
app.iconbitmap("C:\\Users\\Toughpad\\Desktop\\Stuff\\Python_Stuff\\Assets\\Youtube.ico")

# The download function here
def download_video():
    video_url = link.get()
    if video_url:
            youtube = pytube.YouTube(video_url)
            selected_quality = quality_var.get()
            selected_format = format_var.get()
            selected_audio = check_var.get() == "True"

            # For the only audio mode because I don't know how to make it mp3
            if selected_audio:
                audio_stream = youtube.streams.filter(only_audio=selected_audio).first()
                if audio_stream:

                    # Create a directory for audio downloads if it doesn't exist
                    os.makedirs("Audio", exist_ok=True)
                    title = youtube.title
                    audio_file_path = os.path.join("C:\\Users\\Toughpad\\Music\\audio", f"{title}.mp3")
                    audio_stream.download(output_path="C:\\Users\\Toughpad\\Music\\audio", filename=title)
                    os.rename(os.path.join("C:\\Users\\Toughpad\\Music\\audio", title), audio_file_path)

            # Here the way to make a video instead of audio
            else:
                os.makedirs("Videos", exist_ok=True)
                video_stream = youtube.streams.filter(res=selected_quality, file_extension=selected_format).first()
                if video_stream:

                    # Specify a custom output path for video downloads
                    custom_output_path = "C:\\Users\\Toughpad\\Music"
                    os.makedirs(custom_output_path, exist_ok=True)
                    title = youtube.title
                    video_file_path = os.path.join(custom_output_path, f"{title}.mp4")
                    video_stream.download(output_path=custom_output_path, filename=title)
                    os.rename(os.path.join(custom_output_path, title), video_file_path)

#Here the window size stuff
window_width = 400
window_height = 300

screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()

center_x = int((screen_width - window_width) / 2)
center_y = int((screen_height - window_height) / 2)

app.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
#Here the link things
link = ctk.CTkEntry(app, placeholder_text="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
link.pack(pady=20, ipady=5, ipadx=87)

#Here is the quality things
quality_var = ctk.StringVar(value="Quality here!")

quality = ctk.CTkOptionMenu(app, values=["1080p", "720p", "480p"], font=("Jetbrains_Mono", 27), variable=quality_var)
quality.pack(ipadx=70)

#Here to change the format
format_var = ctk.StringVar(value="Format here!")

format_video = ctk.CTkOptionMenu(app, values=["mp4", "webm"], font=("Jetbrains_Mono", 27), variable=format_var)
format_video.pack(ipadx=70)

#If you want only audio
check_var = ctk.StringVar(value="Audio only?")
check_audio = ctk.CTkOptionMenu(app, values=["True", "False"], font=("Jetbrains_Mono", 27), variable=check_var)
check_audio.pack(ipadx=77)

#The download button
download_button = ctk.CTkButton(app, text="Download the Video", font=("Jetbrains_Mono", 30), command=download_video)
download_button.pack(ipadx=31, pady=20)

#The end of the app
app.mainloop()
