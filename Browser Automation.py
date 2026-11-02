import webbrowser

url = "https://i.imageupload.app/5752e92d62cc940a2d87.png"

print("Opening websites...")

for i in range(30):
    webbrowser.open_new_tab(url)

print("All links opened successfully!")
