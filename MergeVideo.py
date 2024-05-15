import os
from moviepy.editor import VideoFileClip, concatenate_videoclips

def merge_videos(folder_path):
    # Get the folder name to use as the output file name
    folder_name = os.path.basename(os.path.normpath(folder_path))
    output_file = f"{folder_name}1.mp4"

    # Get a list of all mp4 files in the directory
    video_files = [f for f in os.listdir(folder_path) if f.endswith('.mp4')]
    
    # Initialize a list to hold video clips
    video_clips = []

    # Load each video file and add to the list of video clips
    for video_file in video_files:
        video_path = os.path.join(folder_path, video_file)
        video_clips.append(VideoFileClip(video_path))

    # Check if there are any video clips to concatenate
    if video_clips:
        # Concatenate all video clips into one
        final_clip = concatenate_videoclips(video_clips)
        # Write the final concatenated video to the output file
        final_clip.write_videofile(output_file, codec="libx264")
    else:
        print("No MP4 files found in the specified folder.")

# Example usage

merge_videos(r"Add path to your folder")
