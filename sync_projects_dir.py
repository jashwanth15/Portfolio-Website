import os
import shutil

# Ensure 'projects' directory exists
os.makedirs("projects", exist_ok=True)

# Copy projects.html to projects/index.html
shutil.copyfile("projects.html", os.path.join("projects", "index.html"))
print("Successfully created projects/index.html to support clean URL /projects")
