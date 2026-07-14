from jarvis.platforms.userdirs.user_directories import UserDirectories


dirs = UserDirectories()

print()

print("Desktop")
print(dirs.desktop())

print()

print("Documents")
print(dirs.documents())

print()

print("Downloads")
print(dirs.downloads())

print()

print("Music")
print(dirs.music())

print()

print("Pictures")
print(dirs.pictures())

print()

print("Videos")
print(dirs.videos())
