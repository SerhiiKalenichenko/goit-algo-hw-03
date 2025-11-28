def move_disk(towers: dict[str, list[int]], src: str, dest: str):
    disk = towers[src].pop()
    towers[dest].append(disk)
    print(f"Перемістити диск з {src} на {dest}: {disk}")
    print(f"Проміжний стан: {towers}")


def hanoi(n: int, src: str, aux: str, dest: str, towers: dict[str, list[int]]):
    if n == 0:
        return
    hanoi(n - 1, src, dest, aux, towers)
    move_disk(towers, src, dest)
    hanoi(n - 1, aux, src, dest, towers)


def main():
    n_str = input("Введи кількість дисків: ")
    try:
        n = int(n_str)
    except ValueError:
        print("Потрібно ввести ціле число.")
        return

    if n <= 0:
        print("Кількість дисків має бути додатною.")
        return

    towers = {
        "A": list(range(n, 0, -1)),
        "B": [],
        "C": [],
    }

    print(f"Початковий стан: {towers}")
    hanoi(n, "A", "B", "C", towers)
    print(f"Кінцевий стан: {towers}")


if __name__ == "__main__":
    main()