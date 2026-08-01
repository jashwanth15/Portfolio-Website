import cv2
import glob
import os

print("Starting 4K Lanczos-4 Ultra HD Upscaling...")
files = sorted(glob.glob('hd_frames/*.webp'))

# 4K UHD dimensions
TARGET_W = 3840
TARGET_H = 2160

count = 0
for f in files:
    img = cv2.imread(f)
    if img is None:
        continue
    # Upscale using Lanczos-4 algorithm (highest quality image resampling algorithm in OpenCV)
    img_4k = cv2.resize(img, (TARGET_W, TARGET_H), interpolation=cv2.INTER_LANCZOS4)
    # Re-apply logo removal on 4K dimensions just to be 100% clean
    # y: 1620..1980, x: 3330..3630
    img_4k[1620:1980, 3330:3630] = (14, 9, 12)

    cv2.imwrite(f, img_4k, [cv2.IMWRITE_WEBP_QUALITY, 98])
    count += 1
    if count % 30 == 0:
        print(f"Upscaled {count}/{len(files)} frames to 4K Ultra HD")

print("Finished upscaling all frames to 3840x2160 4K Ultra HD!")
