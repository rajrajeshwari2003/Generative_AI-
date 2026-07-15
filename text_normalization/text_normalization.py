import string
import emoji
import contractions
from textblob import TextBlob


class TextNormalization:

    def __init__(self, data):
        self.data = data
        self.start()

    def start(self):

        print("Original Text:")
        print(self.data)

        print("""
1. Convert to Lowercase
2. Remove Punctuations
3. Remove Special Characters
4. Handle Emojis
5. Remove Extra Spaces
6. Expand Contractions & Abbreviations
7. Correct Spelling
""")

        # 1
        self.string_lowercase()
        print("\nAfter Lowercase:")
        print(self.data)

        # 2
        option = input("\nRemove punctuations? (yes/no): ").lower()

        if option == "yes":
            self.remove_punctuation()

        print("\nAfter Removing Punctuation:")
        print(self.data)

        # 3
        self.remove_special_character()

        print("\nAfter Removing Special Characters:")
        print(self.data)

        # 4
        emoji_option = input(
            "\nEmoji Handling (remove/demojize/skip): ").lower()

        if emoji_option == "remove":
            self.remove_emoji()

        elif emoji_option == "demojize":
            self.demojize_emoji()

        print("\nAfter Emoji Handling:")
        print(self.data)

        # 5
        self.remove_spaces()

        print("\nAfter Removing Extra Spaces:")
        print(self.data)

        # 6
        self.expand_words()

        print("\nAfter Expanding Words:")
        print(self.data)

        # 7
        self.correct_words()

        print("\nAfter Correcting Words:")
        print(self.data)

        print("\n========== FINAL CLEAN TEXT ==========")
        print(self.data)

    # -----------------------------------------

    def string_lowercase(self):
        self.data = self.data.lower()

    # -----------------------------------------

    def remove_punctuation(self):
        chars = self.data

        for char in string.punctuation:
            chars = chars.replace(char, "")

        self.data = chars

    # -----------------------------------------

    def remove_special_character(self):

        chars = self.data

        for char in chars:
            if not char.isalnum() and not ord(char) == 32:
                chars = chars.replace(char, "")

        self.data = chars

    # -----------------------------------------

    def remove_emoji(self):
        self.data = emoji.replace_emoji(self.data, "")

    def demojize_emoji(self):
        self.data = emoji.demojize(self.data)

    # -----------------------------------------

    def remove_spaces(self):

        words = self.data.split()

        self.data = " ".join(words)

    # -----------------------------------------

    def expand_words(self):

        # Expand contractions
        self.data = contractions.fix(self.data)

        # Expand abbreviations
        abbreviations = {
            "asap": "as soon as possible",
            "btw": "by the way",
            "idk": "I do not know",
            "lol": "laughing out loud",
            "omg": "oh my god",
            "msg": "message",
            "txt": "text",
            "bcz": "because",
            "pls": "please",
            "plz": "please",
            "u": "you",
            "ur": "your",
            "thx": "thanks"
        }

        words = self.data.split()

        result = []

        for word in words:
            result.append(abbreviations.get(word.lower(), word))

        self.data = " ".join(result)

    # -----------------------------------------

    def correct_words(self):

        self.data = str(TextBlob(self.data).correct())


# ---------------- Driver Code ----------------

text = input("Enter Text: ")

obj = TextNormalization(text)