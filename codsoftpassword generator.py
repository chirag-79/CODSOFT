# @codsoft##codsoft#intrenship of python programming
"""pass -word generator"""
# password generator by chirag miglani #codsoft
import random
alphabets=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J",
           "K","L","M","N","O","P","Q","R","S","T","U","V","X","Y","Z"]
numbers=["0","1","2","3","4","5","6","7","8","9"]
specialsymbols=["!","@","#","$","%","&","*","+","(',')"]
print("welcome users! to the password generator by chirag miglani")
m_alphabets=int(input("how many alphabets that you want in your password:"))
m_specialsymbols=int(input("how many specialsymbols that you want in your password:"))
m_numbers=int(input("how many numbers that you want in your password:"))
# here we have to use def function for defining a function
def generate_password(m_alphabets, m_specialsymbols, m_numbers):
    password_list = []
    #firstly we have created a empty list
    #then we are adding alphabets
    for _ in range(m_alphabets):
        password_list.append(random.choice(alphabets))
        """now we are adding specialsymbols in our password"""

    for _ in range(m_specialsymbols):
        password_list.append(random.choice(specialsymbols))
        """now we are adding numbers in our password"""
    for _ in range(m_numbers):
        password_list.append(random.choice(numbers))
    random.shuffle(password_list)
    ## now converted the list to string
    password = ''.join(password_list)
    return password

password = generate_password(m_alphabets, m_specialsymbols, m_numbers)
print("The generated password is shown as:", password)

