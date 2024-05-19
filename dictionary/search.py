dict2 = {'name':'Qozeem Odeniran', 'degree':'MSc. Information Technology', 'job':'Software Engineer'}


def searchDict(mydict, target):
    for key in mydict:
        if mydict[key] == target:
            return f"The value you seek is: {key}, {target}"
        return f"{target} does not exist in the dictionary"

print(searchDict(dict2, 'Qozeem Odeniran'))
