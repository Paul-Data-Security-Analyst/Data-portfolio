# src/day2_reload_inspect.py
import pandas as pd
from pathlib import Path
import io

# ---------- Paths ----------
ROOT = Path(__file__).resolve().parents[1]   # project root
DATA = ROOT / "data"
OUT = ROOT / "outputs"
CLEAN_CSV = OUT / "netflix_movies_2015plus_clean.csv"
RAW_CSV = DATA / "netflix_titles.csv"

OUT.mkdir(parents=True, exist_ok=True)

# ---------- Load dataset (resilient) ----------
if CLEAN_CSV.exists():
    df = pd.read_csv(CLEAN_CSV)
    loaded_from = str(CLEAN_CSV)
elif RAW_CSV.exists():
    # If only raw exists, load raw and do a minimal day1-style quick-clean
    df = pd.read_csv(RAW_CSV)
    # Quick column cleaning
    df.columns = (
        df.columns.str.strip()
                  .str.lower()
                  .str.replace(" ", "_")
                  .str.replace(r"[^a-z0-9_]", "", regex=True)
    )
    # Attempt to convert release_year
    if "release_year" in df.columns:
        df["release_year"] = pd.to_numeric(df["release_year"], errors="coerce")
    # Try to save a cleaned subset for Day1 continuity (non-destructive)
    try:
        df.to_csv(CLEAN_CSV, index=False)
    except Exception:
        pass
    loaded_from = str(RAW_CSV) + " (cleaned & saved to outputs)"
else:
    raise FileNotFoundError(
        f"Missing datasets. Please add either:\n - {CLEAN_CSV}\n - {RAW_CSV}\nThen re-run."
    )

# ---------- Inspect & collect summary ----------
summary_lines = []
summary_lines.append(f"Loaded from: {loaded_from}")
summary_lines.append("\n=== SHAPE ===")
summary_lines.append(str(df.shape))

# Capture df.info() output
buf = io.StringIO()
df.info(buf=buf)
info_text = buf.getvalue()
summary_lines.append("\n=== INFO ===")
summary_lines.append(info_text)

summary_lines.append("\n=== FIRST 5 ROWS ===")
summary_lines.append(df.head(5).to_string())

summary_lines.append("\n=== UNIQUE VALUES PER COLUMN ===")
summary_lines.append(df.nunique(dropna=False).to_string())

summary_lines.append("\n=== DTYPEs ===")
summary_lines.append(df.dtypes.to_string())

summary_lines.append("\n=== MISSING VALUES (per column) ===")
summary_lines.append(df.isna().sum().sort_values(ascending=False).to_string())

# Save summary to outputs file
out_txt = OUT / "day2_reload_inspect.txt"
out_txt.write_text("\n".join(summary_lines), encoding="utf-8")

# Also print short console message
print(f"[+] Loaded dataset from: {loaded_from}")
print(f"[+] Shape: {df.shape}")
print(f"[+] Summary written → {out_txt}")
print("\n--- Head (first 5 rows) ---")
print(df.head(5))
