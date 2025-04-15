import os, sys

print("\nGet Renaming bulk files in one Go..!")

folder_path = input("\nEnter folder path: ")

try:
    if not os.path.exists(folder_path):           # invalid path
        raise FileNotFoundError("\nInvalid folder path")
    
    files = os.listdir(folder_path)

    if not files:                          # empty folder 
        print("\nFolder is empty.\n")
        sys.exit(0)           # clean exit with status code

    rename = input("\nEnter Rename: ")

    for index, file_name in enumerate(files):
        old_path = os.path.join(folder_path, file_name)

        new_name = f"{rename}_{index + 1}{os.path.splitext(file_name)[1]}"

        new_path = os.path.join(folder_path, new_name)

        if os.path.exists(new_path):                 # file already exists
            print(f"\nSkipping... {file_name} - {new_name} already exists.\n")
            continue

        # if not file_name.lower().endswith(('.png', '.jpg', '.pdf')):          # condition to rename only specific extension file
        #     continue

        try:
            os.rename(old_path, new_path)
        except PermissionError:
            print(f"\nPermission denied for {file_name}\n")
        except OSError as e:
            print(f"\nError renaming {file_name}: {e}\n")

    print("\nFiles Renamed Successfully..!\n")

except Exception as e:
    print(f"\nError: {e}\n")
