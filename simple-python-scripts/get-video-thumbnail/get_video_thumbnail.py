import cv2
import os

# Get the current directory (i.e., the path of the script)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Define paths for input and output folders
video_folder = os.path.join(current_dir, "videos")
output_folder = os.path.join(current_dir, "thumbnails")

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

def get_video_thumbnail(video_path, output_image):
    # Open the video file
    cap = cv2.VideoCapture(video_path)
    
    # Read the first frame
    success, frame = cap.read()
    
    if success:
        # Save the extracted frame as an image
        cv2.imwrite(output_image, frame)
        print(f"Thumbnail saved as {output_image}")
    else:
        print("Failed to extract frame.")
    
    # Release video resources
    cap.release()

# Get user input for mp4 file name
mp4_filename = input("Please enter the mp4 file name (without extension): ").strip() + ".mp4"

# Generate the output file path in the output folder
output_image = os.path.join(output_folder, "video-thumbnail.jpg")

# Construct the full path for the input mp4 file
mp4_path = os.path.join(video_folder, mp4_filename)

# Example call to extract a thumbnail
get_video_thumbnail(mp4_path, output_image)
