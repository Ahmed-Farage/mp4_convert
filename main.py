import os
from moviepy.editor import VideoFileClip, AudioFileClip



def main():
    """
    Convert video into an audio file
    """
    vid = input("Enter Vedio name & path(Sparate each with a ','): ")
    list_songs= vid.split(",")
    for i in list_songs:        
        mp3_file = os.path.join(i + ".mp3")
        video = VideoFileClip(i + ".mp4")
        audioclip = video.audio
        audioclip.write_audiofile(mp3_file)
        audioclip.close()
        video.close()


if __name__ == "__main__":
    main()