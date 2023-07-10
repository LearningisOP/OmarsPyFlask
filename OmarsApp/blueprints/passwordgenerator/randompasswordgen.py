from flask import Blueprint, render_template, request, redirect, url_for
import string
import random

randompasswordgen_bp = Blueprint('randompasswordgen', __name__, template_folder="templates")

@randompasswordgen_bp.route("/")
def generatepw():
    return render_template("passwordgen.html")

@randompasswordgen_bp.route("/passwordgenerated", methods=['POST'])
def generate():
    # Retrieve password requirements from the form
    length = int(request.form.get('length'))
    include_uppercase = 'uppercase' in request.form
    include_lowercase = 'lowercase' in request.form
    include_numbers = 'numbers' in request.form
    include_symbols = 'symbols' in request.form

    # Generate the password
    password = generate_password(length, include_uppercase, include_lowercase, include_numbers, include_symbols)

    return render_template("passwordgen.html", password=password)


def generate_password(length, include_uppercase, include_lowercase, include_numbers, include_symbols):
    # Define the character sets based on the requirements
    character_sets = []
    if not (include_uppercase or include_lowercase):
        character_sets.append(string.ascii_uppercase + string.ascii_lowercase)
    else:
        if include_uppercase:
            character_sets.append(string.ascii_uppercase)
        if include_lowercase:
            character_sets.append(string.ascii_lowercase)
    if include_numbers:
        character_sets.append(string.digits)
    if include_symbols:
        character_sets.append(string.punctuation)

    # Calculate the minimum required characters from each character set
    required_chars = sum(bool(char_set) for char_set in character_sets)

    # Check if the required length is greater than or equal to the minimum characters
    if length >= required_chars:
        # Generate the password by selecting random characters from the character sets
        password_characters = []
        
        # Ensure at least one character from each enabled character set
        for char_set in character_sets:
            if char_set:
                password_characters.append(random.choice(char_set))

        # If the generated password is shorter than the required length, add random characters from any character set
        while len(password_characters) < length:
            char_set = random.choice(character_sets)
            password_characters.append(random.choice(char_set))
    else:
        # If the required length is less than the minimum characters, return an empty string
        return ""

    # Shuffle the password characters to make it more random
    random.shuffle(password_characters)

    # Join the password characters to form the final password
    password = ''.join(password_characters[:length])

    return password
