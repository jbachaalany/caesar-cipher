from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  new_text = ""
  if cipher_direction == 'decode':
        shift_amount *= -1 
  for letter in start_text:
    if letter in alphabet:     
      new_text += alphabet[(alphabet.index(letter) + shift_amount) % 26]
    else:
      new_text += letter
  print(f"The {cipher_direction}d text is: {new_text}")


print(logo)
 
choice = 'yes'
while choice == 'yes':
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  choice = input("Do you wish to continue? enter 'yes' or 'no'\n").lower()
  print('------------------------------------------------')