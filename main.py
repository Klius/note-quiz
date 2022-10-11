import random
import typer
from rich import print
from typing import Tuple

Question = Tuple[str, str]


def __get_question() -> Question:
    notes_int = ["A", "B", "C", "D", "E", "F", "G"]
    notes_clas = ["La", "Si", "Do", "Re", "Mi", "Fa", "Sol"]
    x = random.randint(0, 6)
    return (notes_int[x], notes_clas[x])


def __grading(ok: int, total: int) -> None:
    print(f"You got {ok}/{total}")


def main(notes: int = 10):
    ok = 0
    for i in range(0, notes):
        question = __get_question()
        answer: str = typer.prompt(f"{i+1}. Que es {question[0]} ?")
        if answer.lower() == question[1].lower():
            print("[green]De putis[/green]")
            ok += 1
        else:
            print(f"[bold red]Nope![/bold red] la respuesta correcta es {question[1]}")
    __grading(ok, notes)


if __name__ == "__main__":
    random.seed()
    typer.run(main)
