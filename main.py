# from moviepy.editor import VideoFileClip, concatenate_videolips
from moviepy import VideoFileClip, concatenate_videoclips

# List your video files
video_files = ['/src/video1.mp4', '/src/video2.mp4']

# Load and concatenate
clips = [VideoFileClip(f) for f in video_files]
final_clip = concatenate_videoclips(clips, method="compose")

final_clip.write_videofile("output.mp4", codec="libx264", fps=24)

