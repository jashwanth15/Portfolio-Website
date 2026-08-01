import cv2
import glob
import os

print("Optimizing frames to Full HD 1080p (1920x1080) for 60 FPS smooth scrolling...")

files = sorted(glob.glob('hd_frames/*.webp'))

# Re-extract clean frames from video.mp4 directly to 1080p with seamless inpainting
cap = cv2.VideoCapture('video.mp4')
total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# Mask for logo on 1280x720 video
import numpy as np
mask = np.zeros((720, 1280), dtype=np.uint8)
cv2.rectangle(mask, (1120, 560), (1200, 640), 255, -1)

count = 0
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    count += 1

    # Seamless inpaint
    clean_frame = cv2.inpaint(frame, mask, inpaintRadius=7, flags=cv2.INPAINT_TELEA)

    # Resize to 1920x1080 (1080p Full HD) - optimal for 60fps smooth canvas rendering
    frame_1080p = cv2.resize(clean_frame, (1920, 1080), interpolation=cv2.INTER_LANCZOS4)

    filename = os.path.join('hd_frames', f"frame_{count:03d}.webp")
    cv2.imwrite(filename, frame_1080p, [cv2.IMWRITE_WEBP_QUALITY, 92])

cap.release()
print(f"Successfully converted {count} frames to 1080p Full HD!")
