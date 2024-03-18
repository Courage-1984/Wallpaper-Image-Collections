import os


def create_md_file(folder_path, md_file_name):
    with open(md_file_name, "w") as md_file:
        for filename in os.listdir(folder_path):
            if filename.endswith((".png", ".jpg", ".jpeg", ".gif")):
                md_file.write("![]({}/{})\n".format(folder_name, filename))


folder_name = "Gradient Wallpapers"
md_file_name = "gradient-wallpapers-preview.md"

current_directory = os.getcwd()
folder_path = os.path.join(current_directory, folder_name)
md_file_path = os.path.join(current_directory, md_file_name)

if os.path.exists(folder_path):
    create_md_file(folder_path, md_file_path)
    print(
        f"Markdown file '{md_file_name}' created successfully in the current directory."
    )
else:
    print(f"Folder '{folder_name}' does not exist in the current directory.")
