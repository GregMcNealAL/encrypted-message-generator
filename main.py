import random
import stories as st
from ciphers import caesar_cipher, atbash_cipher, reverse_cipher

template = st.stories[0]

complete_story = template.format(
    location_adjectives = random.choice(st.location_adjectives),
    location = random.choice(st.location),
    people = random.choice(st.people),
    items = random.choice(st.items),
    items2 = random.choice(st.items2)
)

cipher_selection = [caesar_cipher, atbash_cipher, reverse_cipher]
cipher_choice = random.choice(cipher_selection)
hints = {
    caesar_cipher: "March 3 steps backward",
    atbash_cipher: "Letters march to their opposite ranks",
    reverse_cipher: "This story starts at its end"
}

cipher_choice = random.choice(cipher_selection)
print(f"Hint: {hints[cipher_choice]}")
print()
ciphertext = cipher_choice(complete_story)
print(ciphertext)