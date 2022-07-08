# для запуска функции необходимо установить библитеку Wikipedia-API==0.5.4
# pip install wikipedia-api

import wikipediaapi

def count_animal_names(all_names_table):
    """ Считает количество животных на каждую букву алфавита"""
    count_table = {}

    # создает пустой словарь с алфавитом
    for letter in 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯ':
        count_table[letter] = 0

    # проходит по ключам словаря с животными, подсчитывая первые буквы названий
    for key in all_names_table:
        if key[0] in count_table:
            count_table[key[0]] += 1

    for letter, number in count_table.items():
        print(letter, number)

if __name__ == "__main__":
    wiki_ru = wikipediaapi.Wikipedia('ru')
    categories = wiki_ru.page('Категория:Животные по алфавиту')

    # создает словарь со всеми животными из категории, ключ - название животного
    all_names_table = categories.categorymembers
    count_animal_names(all_names_table)