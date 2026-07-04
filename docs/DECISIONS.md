DECISION-001
  Jarvis nunca utilizará webbrowser.

  Toda interacción con el sistema operativo se realizará mediante las herramientas nativas de cada plataforma:

  Linux → xdg-open
  Windows → os.startfile()
  macOS → open

  Con esto:

  ✔️ evitamos mensajes como Opening in existing browser session.
  ✔️ el comportamiento es consistente entre plataformas.
  ✔️ mantenemos toda la interacción con el SO encapsulada en la capa Platform.

