from jarvis.search.desktop.scanner import DesktopScanner

scanner = DesktopScanner()

files = scanner.index()

print("Total:", len(files.all()))

for record in files.all():
    print(record.path)
