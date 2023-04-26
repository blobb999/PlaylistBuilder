This project is a script for creating VLC playlists from media files in a specified directory and its subdirectories. It uses the tkinter library for the user interface, which allows users to browse for a directory and create playlists for media files in that directory. It supports different media file formats, such as .mp4, .mp3, .mkv, and .avi. The script also combines multiple playlists in a single directory, creates playlists based on a "Storyline.txt" file, and removes old playlist files before creating new ones.

Here's a summary of the main functionalities:

1.    Browse and select a directory containing media files.
2.    Delete old playlists in the directory and its subdirectories.
3.    Create individual playlists for each directory containing media files.
4.    Create a separate storyline playlist based on a "Storyline.txt" file, if present in a directory.
5.    Combine multiple playlists in a single directory into one playlist.
6.    Show the number of created and combined playlists along with the total number of files added to the playlists.