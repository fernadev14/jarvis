from rich.console import Console

from jarvis.core.assistant import Assistant

console = Console()


def main():

    assistant = Assistant()

    console.print("[bold cyan]JARVIS AI[/bold cyan]")
    console.print()

    while True:

        question = console.input("[bold green]Nano > [/bold green]")

        if question.lower() in ["exit", "quit", "salir"]:
            break

        answer = assistant.chat(question)

        console.print()
        console.print(f"[bold cyan]Jarvis:[/bold cyan] {answer}")
        console.print()


if __name__ == "__main__":
    main()
