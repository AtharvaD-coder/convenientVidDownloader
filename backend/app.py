from flask import Flask, request, jsonify
from pytube import YouTube
import os
import ssl
from flask_cors import CORS

import yt_dlp

app = Flask(__name__)
CORS(app)

ssl._create_default_https_context = ssl._create_stdlib_context

@app.route('/download', methods=['POST'])
def download_video():
    data = request.json
    video_url = data.get('url')

    if not video_url:
        return jsonify({'message': 'No URL provided'}), 400
    
    if 'youtube.com' in video_url or 'youtu.be' in video_url:
        try:
            yt = YouTube(video_url)
            stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
            output_path = os.path.join(os.getcwd(), 'downloads')
            os.makedirs(output_path, exist_ok=True)
            video_file_path = stream.download(output_path=output_path)

            return jsonify({'message': f'Video downloaded: {yt.title}', 'file_path': video_file_path}), 200
        except Exception as e:
            return jsonify({'message': str(e)}), 500
    else:
        try:
            ydl_opts = {
                'format': 'bestvideo+bestaudio/best',
                'outtmpl': '%(title)s.%(ext)s',
                'restrictfilenames': True,
                'noplaylist': True,
                'nocheckcertificate': True,
                'ignoreerrors': False,
                'logtostderr': False,
                'quiet': True,
                'no_warnings': True,
                'prefer_ffmpeg': True,
                'ffmpeg_location': '/path/to/ffmpeg',
                'postprocessors': [{
                    'key': 'FFmpegVideoConvertor',
                }],
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([video_url])

            return jsonify({'message': 'Video downloaded'}), 200
        except Exception as e:
            return jsonify({'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)







# from flask import Flask, request, jsonify
# from pytube import YouTube
# import os
# import ssl
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)

# ssl._create_default_https_context = ssl._create_stdlib_context

# @app.route('/download', methods=['POST'])
# def download_video():
#     data = request.json
#     video_url = data.get('url')

#     if not video_url:
#         return jsonify({'message': 'No URL provided'}), 400

#     try:
#         yt = YouTube(video_url)
#         stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
#         # print("stream: {stream}")
#         output_path = os.path.join(os.getcwd())
#         os.makedirs(output_path, exist_ok=True)
#         video_file_path = stream.download(output_path=output_path)
#         print("reached 5")
#         # return jsonify({'message': f'Video downloaded: {yt.title}', 'file_path': video_file_path}), 200
#         return jsonify({'message': f'Video downloaded'}), 200
#     except Exception as e:
#         return jsonify({'message': e}), 500

# if __name__ == '__main__':
#     app.run(debug=True)
