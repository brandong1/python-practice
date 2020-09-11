numbers = [1,2,3,4,5,6]

evens = [num for num in numbers if num % 2 == 0]
odds = [num for num in numbers if num % 2 != 0]

# if the number is even, multiply it by 2, otherwise divide by 2
[num*2 if num % 2 == 0 else num/2 for num in numbers] #[0.5,4,1.5,8,2.5,12]

######################

with_vowels = "This is so much fun!"

" ".join(char for char in with_vowels if char not in "aeiou") # "Ths s s mch fn!"