from pathlib import Path

from jarvis.platforms.userdirs.user_directories import (
    UserDirectories,
)

from jarvis.search.filesystem.scanner import FileScanner


dirs = UserDirectories()

documents = dirs.documents()

print(documents)
print(documents.exists())
print(documents.is_dir())

scanner = FileScanner()

index = scanner.index(documents)

print()

print("----------------------------------")
print("TOTAL:", len(index))
print("----------------------------------")

for record in index.all()[:20]:

    print(record)
