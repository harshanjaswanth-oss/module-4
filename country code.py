country_code={' India' : '0091', ' Australia' : '0025', 'Nepal' : '00977',' United states of america'  : '2067',' Austria' :'1234'}

print(country_code)

name_of_country=str(input("enter the country of your choice and get the code of it"))
print(country_code.get(name_of_country))

print(country_code.pop(name_of_country))
print(country_code)
for key,value in country_code.items():

    print(key,":",value)
country_code['japan']='3166'
print(country_code)

