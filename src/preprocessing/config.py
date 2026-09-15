from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]

INPUT_PATH: Path = BASE_DIR / "data" / "raw" / "housing.csv"
