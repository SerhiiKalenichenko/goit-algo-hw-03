import argparse
import shutil
from pathlib import Path


def parse_args():
    parser = argparse.ArgumentParser(description="Рекурсивне сортування файлів за розширеннями.")
    parser.add_argument("src_dir", help="Шлях до вихідної директорії")
    parser.add_argument("dst_dir", nargs="?", default="dist", help="Шлях до директорії призначення")
    return parser.parse_args()


def copy_and_sort(src: Path, dst_root: Path):
    try:
        for item in src.iterdir():
            try:
                if item.is_dir():
                    if dst_root in item.resolve().parents:
                        continue
                    copy_and_sort(item, dst_root)
                elif item.is_file():
                    ext = item.suffix.lower().lstrip(".") or "no_extension"
                    target_dir = dst_root / ext
                    target_dir.mkdir(parents=True, exist_ok=True)
                    target_path = target_dir / item.name
                    shutil.copy2(item, target_path)
            except (OSError, PermissionError) as error:
                print(f"Помилка обробки {item}: {error}")
    except (OSError, PermissionError) as error:
        print(f"Помилка доступу до {src}: {error}")


def main():
    args = parse_args()
    src = Path(args.src_dir).resolve()
    dst = Path(args.dst_dir).resolve()

    if not src.exists() or not src.is_dir():
        print("Вихідна директорія не існує або не є директорією.")
        return

    dst.mkdir(parents=True, exist_ok=True)
    copy_and_sort(src, dst)
    print(f"Файли скопійовано та відсортовано в {dst}")


if __name__ == "__main__":
    main()