what_he_does = ' plays '
his_instrument = ' guitar '
his_name = 'he huan huan'
artist_intro = his_name + what_he_does + his_instrument

print (artist_intro)

word = 'word' * 3
print (word)

word = 'a looooooog word'
num = 12
string = 'bang!'
total = string * (len(word) - num)
print (total)

phone_number = '1386-666-0006'
hiding_number = phone_number.replace(phone_number[:9], '*' * 9)
print (hiding_number)

def fahrenheit_converter(C):
    fahrenheit_converter = C * 9/5 + 32
    return (str(fahrenheit)) + 'F'
C2F = fahrenheit_converter(35)
print (C2F)