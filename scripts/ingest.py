import os
import shutil

def ingest():
    src = "data/raw/synthetic_dataset.csv"
    dest = "data/staged/synthetic_dataset.csv"
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    shutil.copy(src, dest)

if __name__ == "__main__":
    ingest()
