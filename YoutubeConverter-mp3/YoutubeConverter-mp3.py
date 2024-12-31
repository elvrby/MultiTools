import yt_dlp
# install yt_dlp dengan "pip install yt-dlp"
import os
# Import Library Python

# Membuat atau generate file baru bernama "downloads"
def youtube_to_mp3(youtube_url, output_dir="downloads"): 
    try:
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Menkonversi Video Youtube Menjadi mp3 dari hasil yt_dip
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': f'{output_dir}/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        # Mendownload hasil audio yang telah di konvert
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_url])

        print("File MP3 berhasil dibuat!")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

youtube_url = input("Masukkan URL YouTube: ")
youtube_to_mp3(youtube_url)

# Noted: kalau gk ada ffmpeg dan terdapat error, itu tidak menjadi masalah
