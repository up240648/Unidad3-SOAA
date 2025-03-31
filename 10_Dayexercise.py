# Nivel 1

 # Ejercicio 1
for i in range(11):
    print(i)
    i = 0
while i <= 10:
    print(i)
    i += 1

# Ejercicio 2
for i in range(10, -1, -1):
    print(i)
    i = 10
while i >= 0:
    print(i)
    i -= 1

# Ejercicio 3
for i in range(1, 8):
    print('#' * i)

# Ejercicio 4
for i in range(5):  # 5 rows
    for j in range(5):  # 5 columns
        print('#', end=' ')
    print()

# Ejercicio 5
for i in range(11):
    print(f"{i} x {i} = {i * i}")

# Ejercicio 6
my_list = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for item in my_list:
    print(item)

# Ejercicio 7
for i in range(0, 101, 2):
    print(i)

# Ejercicio 8
for i in range(1, 101, 2):
    print(i)

# Nivel 2

# Ejercicio 1
total_sum = 0
for i in range(101):
    total_sum += i
print("The sum of all numbers is", total_sum)

# Ejercicio 2

sum_evens = 0
sum_odds = 0
for i in range(101):
    if i % 2 == 0:
        sum_evens += i
    else:
        sum_odds += i
print("The sum of all evens is", sum_evens, "And the sum of all odds is", sum_odds)

# Nivel 3

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
];

# Ejercicio 1
import countries 
countries_with_land = [country for country in countries if 'land' in country.lower()]
print(countries_with_land)

#2.
fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_fruits = []
for fruit in fruits:
    reversed_fruits.insert(0, fruit)

print(reversed_fruits)

#3.
from collections import Counter
import countries
#i.
language_counter = Counter()
unique_languages = set()

for country in countries:
    for language in country["languages"]:
        language_counter[language] += 1
        unique_languages.add(language)


total_languages = len(unique_languages)

# ii.
most_spoken_languages = language_counter.most_common(10)

most_populated_countries = sorted(
    countries_d, key=lambda x: x["population"], reverse=True
)[:10]

# iii.
top_10_populated = [(country["name"], country["population"]) for country in most_populated_countries]
print(f"Total number of unique languages: {total_languages}")
print("\nTen most spoken languages:")
for lang, count in most_spoken_languages:
    print(f"{lang}: {count} countries")

print("\nTen most populated countries:")
for country, population in top_10_populated:
    print(f"{country}: {population}")