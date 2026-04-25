import typer
from rich import print

from app.ingestion import load_data
from app.preprocessing import clean_data
from app.anomaly import detect_anomalies
from app.insights import generate_insight

app = typer.Typer()

@app.command()
def run(file: str):

    print("[bold green]STEP 1: Loading data[/bold green]")
    df = load_data(file)

    print("[bold yellow]STEP 2: Cleaning data[/bold yellow]")
    df = clean_data(df)

    print("[bold red]STEP 3: Detecting anomalies[/bold red]")
    df = detect_anomalies(df)

    anomaly_count = (df["anomaly"] == -1).sum()

    summary = f"""
    Dataset Shape: {df.shape}
    Columns: {list(df.columns)}
    Anomalies Detected: {anomaly_count}
    Sample Data:
    {df.head(5).to_string()}
    """

    print("[bold blue]STEP 4: Generating AI Insights[/bold blue]")
    insight = generate_insight(summary)

    print("\n[bold magenta]FINAL INSIGHT REPORT[/bold magenta]\n")
    print(insight)

if __name__ == "__main__":
    app()