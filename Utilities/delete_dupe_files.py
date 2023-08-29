import os

folder_path = "/Volumes/Maschine+/Native Instruments/Maschine 2/Samples"


def read_dir(path):
    files = os.listdir(path)
    return files


import os


def is_duplicate(file, files):
    # Remove '.wav' extension from the file for comparison
    file_base = os.path.splitext(file)[0]

    if " - " in file_base:
        # The 'original' is the part before the ' - '
        original = file_base.split(" - ")[0]

        # Create a list to hold the versions of this original
        versions = [os.path.splitext(f)[0] for f in files if f.startswith(original)]

        # Extract the tag numbers from the versions
        tag_numbers = []
        for v in versions:
            if " - " in v:
                try:
                    tag_numbers.append(int(v.split(" - ")[-1]))
                except ValueError:
                    # Skip if the tag is not a number
                    continue

        if tag_numbers:
            # Find the lowest tag number among the versions
            min_tag = min(tag_numbers)

            # Only keep the version with the lowest tag number, mark others as duplicates
            if file_base.endswith(f" - {min_tag}"):
                return False
            else:
                return True
        else:
            return False
    else:
        return False


def delete_duplicate(file, folder_path, files):
    full_path = os.path.join(folder_path, file)
    if is_duplicate(file, files):
        print(f"Removing duplicate file: {full_path}")
        os.remove(full_path)
    else:
        print(f"File is not a duplicate: {full_path}")


# Initialize counters
count_to_remove = 0
size_to_remove = 0

# List the files in the directory
files = read_dir(folder_path)
print(files)

# Check for duplicates and calculate size
for file in files:
    is_dup = is_duplicate(file, files)
    print(file, is_dup)

    if is_dup:
        count_to_remove += 1
        full_path = os.path.join(folder_path, file)
        size_to_remove += os.path.getsize(full_path)

# Display count and size to be removed
print(f"Number of files to remove: {count_to_remove}")
print(f"Total size of files to remove: {size_to_remove} bytes")

# Delete duplicates
for file in files:
    delete_duplicate(file, folder_path, files)
