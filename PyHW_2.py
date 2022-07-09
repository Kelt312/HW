#домашняя работа №2
#список

m_f_b=["Достоевский Ф.М.: Идиот", "Булгаков М.А.: Белая гвардия", "Чехов А.П.: Три сестры",
       "Мураками Х.: Хроники заводной птицы"]
print(m_f_b,)
# список похож на массив, из плюсов: возможность обращения по индексу, элементы могут быть разнородными,
# в список можно добавлять/удалять/менять элементы, сортировать элементы. Наиболее удобно работать с числами

print("-----------------------------------------------")

# добавление нового элемента
m_f_b.append("Лукьяненко С.В.: Ночной дозор")
print(m_f_b)

print("-----------------------------------------------")

# кортеж
m_f_b=tuple(m_f_b)

a=m_f_b[0]
print(a)
# элементы в кортеже менять/удалять/добавлять нельзя, зато можно создавать сложные структуры данных
# хотя и в списке это тоже можно сделать. Видимо так повелось: структура - кортеж, порядок - список

print("-----------------------------------------------")

#словари
m_f_b={"Достоевский Ф.М.": "Идиот", "Булгаков М.А.": "Белая гвардия", "Чехов А.П.": "Три сестры",
       "Мураками Х.": "Хроники заводной птицы"}
for b in m_f_b:
    print(b, m_f_b[b])

# основное преимущества словаря - структура хранения данных ключ:значение, что позволяет обращаться к значению не поего
# порядковому номеру как в списке, а по ключу. Разумеется в словаре можно добавлять/удалять/изменять элементы
