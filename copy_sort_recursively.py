import os
import shutil
import argparse

def copy_and_sort(src_dir, dest_dir):
    try:
        # Перевірка чи існує директорія призначення, інакше створити
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        # Перебираємо всі елементи у вихідній директорії
        for item in os.listdir(src_dir):
            item_path = os.path.join(src_dir, item)

            # Якщо елемент є директорією, викликаємо функцію рекурсивно
            if os.path.isdir(item_path):
                copy_and_sort(item_path, dest_dir)

            # Якщо елемент є файлом, обробляємо його для копіювання
            elif os.path.isfile(item_path):
                # Отримуємо розширення файлу
                _, extension = os.path.splitext(item_path)
                # Створюємо шлях до піддиректорії за розширенням файлу
                sub_dir = os.path.join(dest_dir, extension[1:])

                # Якщо піддиректорія не існує, створюємо її
                if not os.path.exists(sub_dir):
                    os.makedirs(sub_dir)

                # Створюємо шлях до нового файлу
                new_file_path = os.path.join(sub_dir, os.path.basename(item_path))

                # Копіюємо файл у відповідну піддиректорію
                shutil.copy2(item_path, new_file_path)
                print(f"Copied: {item_path} -> {new_file_path}")


    except Exception as e:
        print(f"Error: {e}")

def main():
    parser = argparse.ArgumentParser(description="Copy and sort files recursively.")
    parser.add_argument("-src_dir", dest="src_directory", required=True, help="Source directory")
    parser.add_argument("-dest_dir", dest="dest_directory", default='dist', required=False, help="Destination directory")

    args = parser.parse_args()
    copy_and_sort(args.src_directory, args.dest_directory)
    print("Files copied and sorted successfully.")

if __name__ == "__main__":
    main()