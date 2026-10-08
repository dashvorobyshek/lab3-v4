import json
from pathlib import Path
from tempfile import TemporaryDirectory


class JsonSerializer:
    """Класс для сохранения и загрузки словарей в формате JSON."""

    def __init__(self, filepath: str):
        """Запоминает путь к JSON-файлу."""
        self.filepath = Path(filepath)

    def save_to_json(self, data: dict) -> None:
        """Сохраняет JSON-совместимый словарь в файл."""
        if not isinstance(data, dict):
            raise TypeError("Для сохранения ожидается словарь.")

        # Преобразуем данные до открытия файла, чтобы ошибка
        # сериализации не стёрла ранее сохранённое содержимое.
        json_text = json.dumps(
            data,
            ensure_ascii=False,
            indent=4,
            allow_nan=False,
        )

        with self.filepath.open("w", encoding="utf-8") as file:
            file.write(json_text + "\n")

    def load_from_json(self) -> dict:
        """Читает JSON-файл и возвращает словарь."""
        with self.filepath.open("r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, dict):
            raise ValueError("В JSON-файле должен находиться словарь.")

        return data


if __name__ == "__main__":
    sample_data = {
        "student": "Воробьева Дарья Сергеевна",
        "group": 221341,
        "lab": 3,
    }

    try:
        # Папка и файл удалятся при выходе из with,
        # даже если во время работы возникнет ошибка.
        with TemporaryDirectory() as temporary_directory:
            filepath = Path(temporary_directory) / "temp_data.json"
            serializer = JsonSerializer(str(filepath))

            serializer.save_to_json(sample_data)
            print("Данные успешно сохранены в JSON.")

            loaded_data = serializer.load_from_json()
            print(f"Десериализованные данные: {loaded_data}")
            print(f"Данные совпадают: {loaded_data == sample_data}")

    except (OSError, TypeError, ValueError) as error:
        print(f"Ошибка работы с JSON: {error}")
