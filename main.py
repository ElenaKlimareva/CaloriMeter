import typer

app = typer.Typer()


@app.command()
def add(meal_description: str):
    print(f"Meal added: {meal_description}")



@app.command()
def get(day: int):
    print(f"Retrieving data for day {day}")

if __name__ == "__main__":
    app()
