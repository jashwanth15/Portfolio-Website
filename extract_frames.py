import cv2
import os

video_path = 'video.mp4'
output_dir = 'hd_frames'
os.makedirs(output_dir, exist_ok=True)

cap = cv2.VideoCapture(video_path)
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print(f"Total frames in video: {total_frames}")

count = 0
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    count += 1
    filename = os.path.join(output_dir, f"frame_{count:03d}.webp")
    # Save as high-quality WebP (quality 95) for small file size + crystal clear HD
    cv2.imwrite(filename, frame, [cv2.IMWRITE_WEBP_QUALITY, 95])

cap.release()
print(f"Extracted {count} HD WebP frames successfully!")
