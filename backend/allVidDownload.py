

# import yt_dlp

# # Define the URL of the video
# url = ""

# # Define the download options
# ydl_opts = {
#     'format': 'bestvideo+bestaudio/best',  # Prioritize best video + best audio
#     'outtmpl': '%(title)s.%(ext)s',
#     'restrictfilenames': True,
#     'noplaylist': True,
#     'nocheckcertificate': True,
#     'ignoreerrors': False,
#     'logtostderr': False,
#     'quiet': False,
#     'no_warnings': True,
#     'prefer_ffmpeg': True,  # Ensure prefer_ffmpeg is enabled for better compatibility
#     'ffmpeg_location': '/path/to/ffmpeg',  # Specify the path to your FFmpeg executable if needed
#     'postprocessors': [{
#         'key': 'FFmpegVideoConvertor',
#     }],
# }

# # Create a YouTubeDL object
# ydl = yt_dlp.YoutubeDL(ydl_opts)

# # Download the video
# ydl.download([url])
