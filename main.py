import os

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    line = "My phone promised all-day battery, then died at 3 p.m. — the only thing it charges faster than its battery is my anxiety."
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    os.chmod(path, 0o644)

if __name__ == "__main__":
    main()
