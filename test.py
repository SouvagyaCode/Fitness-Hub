import os

# Path to your image directory
image_folder = "static/images"

# Loop through all files in the folder
for filename in os.listdir(image_folder):
    old_path = os.path.join(image_folder, filename)

    # Skip if not a file
    if not os.path.isfile(old_path):
        continue

    # Convert to lowercase, replace spaces with dashes
    name, ext = os.path.splitext(filename)
    new_name = name.lower().replace(" ", "-") + ext.lower()

    new_path = os.path.join(image_folder, new_name)

    # Only rename if name changed
    if old_path != new_path:
        os.rename(old_path, new_path)
        print(f"Renamed: {filename} → {new_name}")
