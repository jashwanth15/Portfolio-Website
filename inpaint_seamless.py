import cv2
import numpy as np
import os

video_path = 'video.mp4'
output_dir = 'hd_frames'
os.makedirs(output_dir, exist_ok=True)

cap = cv2.VideoCapture(video_path)
total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print(f"Processing {total} frames with Telea seamless inpainting...")

# Create precise mask for logo on 1280x720 video frames
mask = np.zeros((720, 1280), dtype=np.uint8)
cv2.rectangle(mask, (1120, 560), (1200, 640), 255, -1)

count = 0
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    count += 1

    # Seamlessly blend surrounding texture into logo region (NO black boxes or patches!)
    clean_frame = cv2.inpaint(frame, mask, inpaintRadius=7, flags=cv2.INPAINT_TELEA)

    # Upscale to 4K Ultra HD (3840x2160)
    frame_4k = cv2.resize(clean_frame, (3840, 2160), interpolation=cv2.INTER_LANCZOS4)

    filename = os.path.join(output_dir, f"frame_{count:03d}.webp")
    cv2.imwrite(filename, frame_4k, [cv2.IMWRITE_WEBP_QUALITY, 98])

    if count % 30 == 0:
        print(f"Inpainted & upscaled {count}/{total} frames")

cap.release()
print("Seamless inpainting complete for all 240 frames!")
