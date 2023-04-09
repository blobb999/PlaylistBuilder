import os
from tkinter import filedialog
from tkinter import messagebox
from tkinter import Tk, Button, Label, Entry, StringVar
from urllib.parse import quote
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom import minidom


def delete_old_playlists(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.xspf') or file.endswith('.m3u'):
                os.remove(os.path.join(root, file))


def create_playlist(directory):
    media_files = sorted([f for f in os.listdir(directory) if f.endswith('.mp4') or f.endswith('.mp3')])

    if not media_files:
        return 0

    playlist = Element('playlist', {'version': '1', 'xmlns': 'http://xspf.org/ns/0/'})
    title = SubElement(playlist, 'title')
    title.text = 'Playlist'

    track_list = SubElement(playlist, 'trackList')

    for media_file in media_files:
        track = SubElement(track_list, 'track')
        location = SubElement(track, 'location')
        file_path = os.path.join(directory, media_file).replace('\\', '/')
        encoded_path = quote(file_path, safe=":/")
        location.text = f'file:///{encoded_path}'

    xml_string = tostring(playlist, 'utf-8')
    pretty_xml = minidom.parseString(xml_string).toprettyxml(indent='  ')

    # Use the folder name for the playlist file
    folder_name = os.path.basename(directory)
    parent_directory = os.path.dirname(directory)
    playlist_filename = os.path.join(parent_directory, f'{folder_name}.xspf')

    with open(playlist_filename, 'w', encoding='utf-8') as f:
        f.write(pretty_xml)

    return len(media_files)


def create_playlists_recursively(directory):
    playlist_count = 0
    file_count = 0

    delete_old_playlists(directory)
    for root, dirs, files in os.walk(directory):
        files_added = create_playlist(root)
        if files_added > 0:
            playlist_count += 1
            file_count += files_added

    messagebox.showinfo("Result", f"{playlist_count} playlists created with a total of {file_count} files.")


def browse_directory():
    directory = filedialog.askdirectory()
    folder_path.set(directory)


def main():
    global folder_path

    root = Tk()
    root.title("VLC Playlist Creator")
    root.geometry("400x200")

    folder_path = StringVar()

    browse_button = Button(root, text="Browse Directory", command=browse_directory)
    browse_button.pack(pady=10)

    folder_label = Label(root, text="Directory:")
    folder_label.pack()

    folder_entry = Entry(root, textvariable=folder_path, width=50)
    folder_entry.pack(pady=10)

    create_button = Button(root, text="Create Playlists", command=lambda: create_playlists_recursively(folder_path.get()))
    create_button.pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()
