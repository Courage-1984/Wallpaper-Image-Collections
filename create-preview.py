import os


def create_md_file(folder_path, md_file_path):
    with open(md_file_path, "w") as md_file:
        md_file.write("# Wallpapers in /{}\n\n".format(folder_name))
        for filename in os.listdir(folder_path):
            if filename.endswith((".png", ".jpg", ".jpeg", ".gif", ".webp", ".mp4")):
                md_file.write(
                    "![](/{}/{})\n".format(
                        folder_name.replace(" ", "%20"), filename.replace(" ", "%20")
                    )
                )


folder_name = "Black Wallpapers"
md_file_name = "black_wallpapers-preview.md"

current_directory = os.getcwd()
folder_path = os.path.join(current_directory, folder_name)
md_file_directory = os.path.join(current_directory, "Previews")
md_file_path = os.path.join(md_file_directory, md_file_name)

if os.path.exists(folder_path):
    if not os.path.exists(md_file_directory):
        os.makedirs(md_file_directory)
    create_md_file(folder_path, md_file_path)
    print(
        f"Markdown file '{md_file_name}' created successfully in the 'Previews' directory."
    )
else:
    print(f"Folder '{folder_name}' does not exist in the current directory.")
