d = [
('Hendrix' , '1942'),
('Allman' , '1946'),
('King' , '1925'),
('Clapton' , '1945'),
('Johnson' , '1911'),
('Berry' , '1926'),
('Vaughan' , '1954'),
('Cooder' , '1947'),
('Page' , '1944'),
('Richards' , '1943'),
('Hammett' , '1962'),
('Cobain' , '1967'),
('Garcia' , '1942'),
('Beck' , '1944'),
('Santana' , '1947'),
('Ramone' , '1948'),
('White' , '1975'),
('Frusciante', '1970'),
('Thompson' , '1949'),
('Burton' , '1939')
]

dict = {}

for i , j in d:
    dict[j] = i
    print(j, ":", i)



# transformar em dicionario
#extrair antes ou depois os dados?

# def Convert(lst):
#     res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
#     return res_dct
         