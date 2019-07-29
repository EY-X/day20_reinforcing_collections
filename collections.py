digits = ['1','2','3','4','5','6','7','8','9']
en = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
fr = ['un','deux','trois','quatre','cinq','six','sept','huit','neuf']
hb = ['ehad', 'shtayim', 'shalosh', 'arba', 'chamesh', 'shesh', 'sheva', 'shmoneh', 'tesha']

def dictionary_translate(digits, english, french, hebrew):
    new_dictionary = {}

    for counter, digit in enumerate(digits, 1):
        new_dictionary[digit] = {
            'english': en[counter - 1],
            'french': fr[counter - 1],
            'hebrew': hb[counter - 1],
        } 
    return new_dictionary


x = dictionary_translate(digits, en, fr, hb)
print(x)




