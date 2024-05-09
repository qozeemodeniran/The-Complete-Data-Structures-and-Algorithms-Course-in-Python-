# Create dictionary using dict() constructor
dict1 = dict(name='Qozeem Odeniran', degree='MSc. Information Technology', job='Software Engineer')
print(f"dict1: {dict1}")

# Create dictionary using {}
dict2 = {'name':'Qozeem Odeniran', 'degree':'MSc. Information Technology', 'job':'Software Engineer'}
print(f"dict2: {dict2}")

# Create dictionary using list of tuples
dict3 = [('name','Qozeem Odeniran'), ('degree','MSc. Information Technology'), ('job','Software Engineer')]
dict3 = dict(dict3)
print(f"dict3: {dict3}")
