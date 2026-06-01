phones={
    "john":12345,
    "ria":524896,
    "sia":254687,
    "kia":179514
        }
print(phones)
#access item in dict
print(phones["john"])
print(phones.keys())
#update
phones["john"]=14582
print(phones["john"])
#remove element 
phones.pop("john")
print(phones)