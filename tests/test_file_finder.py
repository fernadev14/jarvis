from jarvis.files.finder import FileFinder

finder = FileFinder()

tests = [
    "contrato.pdf",
    "factura.xlsx",
    "imagen.png",
]

for test in tests:

    print("-" * 40)
    print(test)

    result = finder.find(test)

    print(result)
