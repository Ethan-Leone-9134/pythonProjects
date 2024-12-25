import os
import random

# Define the folder path
def add_random_prefix(folder_path):
    try:
        # Get all files in the folder
        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

        for file_name in files:
            if file_name[4] != "_":
                # Generate a random number
                random_number = random.randint(1000, 9999)

                # Construct new file name
                new_name = f"{random_number:04}_{file_name}"

                # Get full paths
                old_path = os.path.join(folder_path, file_name)
                new_path = os.path.join(folder_path, new_name)

                # Rename the file
                os.rename(old_path, new_path)
                print(f"Renamed: {file_name} -> {new_name}")

        print("All files have been renamed.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
folder_path = "D:\\"
add_random_prefix(folder_path)
