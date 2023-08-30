import pandas as pd

dfLanguages = pd.read_csv('S1_LanguageData.csv')
dfLanguages = dfLanguages.set_index("num")
df = pd.read_hdf('GreatLanguageGameData.h5')

print("Leu o arquivo!")
languageComb = []
for language1 in dfLanguages['Language']:
    for language2 in dfLanguages['Language']:
        if(language1 != language2):
            probConf1 = len(df.query('Target == "' + language1 + '" & Guess == "' + language2 + '"').index) / len(df.query('Target == "' + language1 + '"').index)
            probConf2 = len(df.query('Target == "' + language1 + '" & Guess == "' + language2 + '"').index) / len(df.query('Target == "' + language1 + '" & Guess != Target').index)
            print(language1 + " - " + language2 + " -> prob1: " + str(probConf1) + " | -> prob2: " + str(probConf2))
            languageComb.append([language1, language2, probConf1, probConf2])
dfLanguageComb = pd.DataFrame(languageComb, columns = ['Target Language', 'Guess Language', 'Prob1', 'Prob2'])
dfLanguageComb.to_csv("langugeComb.csv")