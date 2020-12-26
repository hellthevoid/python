import music_database as MD


df=MD.read_db('music_database.csv')


df=MD.translate_forbidden_symbols(df)


print (df)