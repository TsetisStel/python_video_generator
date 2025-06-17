# from moviepy.editor import VideoFileClip, concatenate_videolips
from moviepy import VideoFileClip, concatenate_videoclips
from pathlib import Path

folder = Path('./resources')

clips = []

# List your video files
video_files = list(folder.glob("*.mp4"))

for video_path in video_files:
    clip = VideoFileClip(str(video_path))
    duration = clip.duration
    
    print(f"\nProcessing: {video_path.name} (Duration: {duration: 2f} seconds)")
    try:
        while True:
            # Ask user for start & end time:
            start = float(input("Enter start time in seconds: "))
            end = float(input("Enter end time in seconds: "))

            if start < 0 or end > duration or start >= end:
                print("⚠️ Invalid time range.")
            break

        # Load and trim video
        trimmed_clip = clip.subclipped(start, end)
        clips.append(trimmed_clip)

    except Exception as e:
        print(f"Skipping {video_path.name} due to error: {e}")

# Load and concatenate
if clips:
    final_clip = concatenate_videoclips(clips, method="compose")
    final_clip.write_videofile("output.mp4", codec="libx264", fps=24)
else:
    print("No clips to process")
