
csv = 'Eric,John,Michael,Terry,Graham:TerryG,Brian'
friends_list = ['Eric', 'John', 'Michael', 'Terry', 'Graham:TerryG', 'Brian']
print(friends_list)
print(csv.split())
print('-'.join(friends_list + friends_list))
print(' '.join(friends_list))