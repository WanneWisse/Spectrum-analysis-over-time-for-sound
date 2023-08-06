from pytube import YouTube
import moviepy.editor as mp

def download_youtube_audio(video_url, output_path):
    try:
        # Create a YouTube object and get the highest-quality audio stream available
        yt = YouTube(video_url)
        audio_stream = yt.streams.filter(only_audio=True).first()

        # Download the audio in its original format (e.g., webm)
        audio_stream.download(output_path, filename="temp.webm")

        # Convert the downloaded audio to MP3
        audio_file = mp.AudioFileClip("temp.webm")
        audio_file.write_audiofile("test.mp3")

        # Remove the temporary webm file
        audio_file.reader.close_proc()
        audio_file.reader.proc.terminate()

        print("Audio downloaded successfully as MP3!")
    except Exception as e:
        print("Error:", str(e))

if __name__ == "__main__":
    video_url = "https://www.youtube.com/watch?v=xbHPTPUpQ1I"
    output_path = ""
    download_youtube_audio(video_url, output_path)