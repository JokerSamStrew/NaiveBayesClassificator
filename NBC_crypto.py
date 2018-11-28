import copy
import pickle
'''
GlobalFrequencyTable -
    сущность позволяющая работать хранить и дополнять
    данные, на основании которых вычисляется вероятность того,
    что текст содержит информацию о криптоволюте
'''
class FrequencyTable:
    '''
        Словарь содержит ключи слова и под каждым ключом
        содержится словарь с ключами возможного исхода (идет речь о криптоволюте или нет)
        эти ключи содержат количество упоминаний данного слова в документах
        с данным исходом
    '''
    frequency_table_dict_instance = {}
    classes_dict = {
         "CRYPTO_DATA" : 0,
         "NOT_CRYPTO_DATA" : 0
        }

    # создание нового словаря
    def NewFTable(self):
        self.frequency_table_dict_instance = {
            "TOTAL" : copy.deepcopy(self.classes_dict)
        }
    # cериализация словаря (нужны права администратора на запуск)
    def SaveTable(self, file_name = "freq_table_obj"):
        with open(file_name, 'wb') as f:
            pickle.dump(
                self.frequency_table_dict_instance,
                f, pickle.HIGHEST_PROTOCOL
                )
    # десериализация словар (нужны права администратора на запуск)
    def LoadTable(self, file_name = "freq_table_obj"):
        with open(file_name, 'rb') as f:
            self.frequency_table_dict_instance = pickle.load(f)
    # обращение к словарю за данными
    def TableData(self, event, result):
        if event in self.frequency_table_dict_instance:
            return self.frequency_table_dict_instance[event][result]
        else:
            return 0; 
    # обучение (добавление новой информации)
    def AddData(self, doc_freq_table, result):
        for event in doc_freq_table.keys():
            if event not in self.frequency_table_dict_instance:
                self.frequency_table_dict_instance[event] = copy.deepcopy(self.classes_dict)
            self.frequency_table_dict_instance[event][result] += doc_freq_table[event]
            self.frequency_table_dict_instance["TOTAL"][result] += doc_freq_table[event]

if __name__ == "__main__":
    my_table = FrequencyTable()
    my_table.NewFTable()
    test_data = {
        "crypto_word" : 12,
        "not_crypto_word" : 2
    }
    my_table.AddData(test_data, "CRYPTO_DATA")
    print(my_table.TableData("crypto_word", "CRYPTO_DATA"))
    print(my_table.TableData("TOTAL", "CRYPTO_DATA"))
    my_table.SaveTable("file.txt")
    new_table = FrequencyTable()
    new_table.LoadTable("file.txt")
    print(new_table.TableData("crypto_word", "CRYPTO_DATA"))
    print(new_table.TableData("TOTAL", "CRYPTO_DATA"))
