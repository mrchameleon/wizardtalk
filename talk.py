import markovify
import random
from rune import encode_rune


with open("wizardtalk.txt", "r", encoding="utf-8") as f:
    text = f.read()

# train a markov model from the text
# Tune state_size: Try 1, 2, or 3. Higher = more coherence, lower = more weirdness.
model_one = markovify.NewlineText(text, state_size=1) # weird
model_two = markovify.NewlineText(text, state_size=2) # more-readable / less grammar issues?

# Generate and print new comments
print("Generated Comments:\n")
for i in range(30):
    num = random.randint(1,2)
    if num == 1:
        sentence = model_one.make_sentence(tries=100)  # tries=100 gives better chance of a good sentence
    else:
        sentence = model_two.make_sentence(tries=100)  # tries=100 gives better chance of a good sentence

    if sentence:
        chance_for_runic = random.randint(1,25)
        if chance_for_runic == 1:
            sentence = encode_rune(sentence)
            print(sentence)
        else:
            print(sentence)


# ideas to go further
# Train on separate categories (e.g. positive, sarcastic, emoji-heavy).
# save and re-use the model - model.to_json() / from_json()
