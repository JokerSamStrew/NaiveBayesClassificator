import NBC_ProbFormula as pf
import NBC_crypto as ft
import TextConverter as tc

if __name__ == "__main__":
    my_freq_table = ft.FrequencyTable()
    #my_freq_table.LoadTable()
    my_freq_table.NewFTable()
    not_crypto_data = tc.makeFreqTable("C:\\Users\\Simon\\Desktop\\Classificator\\not_crypto_1.txt")
    crypto_data = tc.makeFreqTable("C:\\Users\\Simon\\Desktop\\Classificator\\crypto_1.txt")
    #test_crypto_data = tc.makeFreqTable("C:\\Users\\Simon\\Desktop\\Classificator\\crypto_2.txt")
    test_not_crypto_data = tc.makeFreqTable("C:\\Users\\Simon\\Desktop\\Classificator\\not_crypto_2.txt")
    my_freq_table.AddData(not_crypto_data, "NOT_CRYPTO_DATA")
    my_freq_table.AddData(test_not_crypto_data, "NOT_CRYPTO_DATA")
    my_freq_table.AddData(crypto_data, "CRYPTO_DATA")
    #my_freq_table.SaveTable()
    prob_sum = 0
    event_counter = 1
    for event in test_not_crypto_data:
        if event in my_freq_table.frequency_table_dict_instance:
            prob_sum += pf.apostorioriProb("CRYPTO_DATA", event, my_freq_table)
            event_counter += 1

    print(prob_sum / event_counter)
