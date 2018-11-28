import re

'''
    Данный модель содержит методы для обработки текста
    в частотную таблицу
'''


# Перевод файла в строку
def fileToString(file_name):
    result_str = str()
    with open(file_name, "r") as f:
        for line in f:
            result_str += line[:-1]
    return result_str

# Преобразование строки в список слов
def translateString(str_instance):
    result_lwords = []
    lwords = re.split("[^a-zA-Z]", str_instance)
    for word in lwords:
        if word != "":
            result_lwords.append(word.lower())
    return result_lwords

# Создание частотной таблицы
def wordslToFreqTable(lwords):
    freqTable = {}
    for word in lwords:
        if word not in freqTable:
            freqTable[word] = 1
        else:
            freqTable[word] += 1
    return freqTable

def makeFreqTable(file_name):
    return wordslToFreqTable(translateString(fileToString(file_name)))

if __name__ == "__main__":
    print(makeFreqTable("C:\\Users\\Simon\\Desktop\\Classificator\\TextConverter_Test.txt"))
