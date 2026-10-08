class TextAnalyzer:
    """Утилитарный класс для анализа текстовой информации."""

    @staticmethod
    def count_vowels(text: str) -> int:
        """Считает русские и английские гласные без учёта регистра.

        Русские гласные: а, е, ё, и, о, у, ы, э, ю, я.
        Английские гласные: a, e, i, o, u. Буква y не учитывается,
        поскольку её роль зависит от слова.
        Аргумент должен быть строкой; результат - целое число.
        """
        if not isinstance(text, str):
            raise TypeError("Ожидается строковый тип данных.")

        vowels = set("аеёиоуыэюяaeiou")
        count = 0
        for char in text.lower():
            if char in vowels:
                count += 1
        return count


if __name__ == "__main__":
    sample_texts = (
        "Привет, мир!",
        "Hello, world!",
        "ООП на Python",
        "АЕЁИОУЫЭЮЯ AEIOU",
        "бвгд 123!",
        "",
    )

    for sample_text in sample_texts:
        try:
            vowel_count = TextAnalyzer.count_vowels(sample_text)
            print(f"{sample_text!r}: гласных — {vowel_count}")
        except TypeError as error:
            print(f"Ошибка типа: {error}")
