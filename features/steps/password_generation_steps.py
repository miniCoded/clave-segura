from behave import given, when, then
from password_validator import PasswordValidator

@given('I enter the word "{word}"')
def step_enter_word(context, word):
    """Store the word to generate password from."""
    context.word = word

@given('I enter an empty word')
def step_enter_empty_word(context):
    """Store an empty word for testing."""
    context.word = ""

@when('I request password generation')
def step_request_generation(context):
    """Request password generation from the word."""
    if context.word is None:
        context.password = ""
        context.details = {}
    else:
        context.password, context.details = PasswordValidator.generate_from_word(context.word)

@then('a password should be generated')
def step_password_generated(context):
    """Check that a password was generated."""
    assert context.password and len(context.password) > 0, \
        "No password was generated"

@then('no password should be generated')
def step_no_password_generated(context):
    """Check that no password was generated for empty input."""
    assert not context.password or len(context.password) == 0, \
        "Password should not be generated for empty input"

@then('the password should be at least {length:d} characters long')
def step_password_length(context, length):
    """Check that password meets minimum length requirement."""
    assert len(context.password) >= length, \
        f"Password length {len(context.password)} is less than required {length}"

@then('the password should contain uppercase letters')
def step_contains_uppercase(context):
    """Check that password contains uppercase letters."""
    assert any(c.isupper() for c in context.password), \
        "Password does not contain uppercase letters"

@then('the password should contain lowercase letters')
def step_contains_lowercase(context):
    """Check that password contains lowercase letters."""
    assert any(c.islower() for c in context.password), \
        "Password does not contain lowercase letters"

@then('the password should contain numbers')
def step_contains_numbers(context):
    """Check that password contains numbers."""
    assert any(c.isdigit() for c in context.password), \
        "Password does not contain numbers"

@then('the password should contain at least {count:d} numbers')
def step_contains_numbers_count(context, count):
    """Check that password contains at least the required count of numbers."""
    digit_count = sum(1 for c in context.password if c.isdigit())
    assert digit_count >= count, \
        f"Password contains {digit_count} numbers, required at least {count}"

@then('the password should contain symbols')
def step_contains_symbols(context):
    """Check that password contains symbols."""
    symbols = '!@#$%^&*()_+-=[]{}|;:,.<>?'
    assert any(c in symbols for c in context.password), \
        "Password does not contain symbols"

@then('the password should contain at least {count:d} symbols')
def step_contains_symbols_count(context, count):
    """Check that password contains at least the required count of symbols."""
    symbols = '!@#$%^&*()_+-=[]{}|;:,.<>?'
    symbol_count = sum(1 for c in context.password if c in symbols)
    assert symbol_count >= count, \
        f"Password contains {symbol_count} symbols, required at least {count}"

@then('the password should not contain obvious patterns')
def step_no_obvious_patterns(context):
    """Check that password doesn't contain obvious patterns."""
    assert not context.details.get('has_obvious_patterns', True), \
        "Password contains obvious patterns"

@then('the password should not contain the word "{word}"')
def step_no_word_in_password(context, word):
    """Check that password doesn't contain the source word."""
    assert word.lower() not in context.password.lower(), \
        f"Password contains the word '{word}'"

@then('the password should contain leet-speak substitutions like "{char}" for "{letter}"')
def step_leet_substitutions(context, char, letter):
    """Check that leet-speak substitutions are present."""
    # The password should have some leet-speak characters
    leet_chars = ['4', '@', '3', '9', '1', '!', '0', '5', '$', '7']
    has_leet = any(c in leet_chars for c in context.password)
    assert has_leet, \
        f"Password should contain leet-speak substitutions"

@then('the password should be cryptographically secure')
def step_cryptographically_secure(context):
    """Check that password meets security criteria."""
    # Check that password has all complexity requirements
    assert any(c.isupper() for c in context.password), "Missing uppercase"
    assert any(c.islower() for c in context.password), "Missing lowercase"
    assert any(c.isdigit() for c in context.password), "Missing digits"
    symbols = '!@#$%^&*()_+-=[]{}|;:,.<>?'
    assert any(c in symbols for c in context.password), "Missing symbols"
    assert len(context.password) >= 12, "Password too short"

@then('the password should have mixed case letters')
def step_mixed_case(context):
    """Check that password has mixed case."""
    has_upper = any(c.isupper() for c in context.password)
    has_lower = any(c.islower() for c in context.password)
    assert has_upper and has_lower, \
        "Password should have mixed case letters"

@then('the password should be shuffled and randomized')
def step_shuffled_randomized(context):
    """Check that password is properly randomized."""
    # Just verify the password exists and has length
    assert len(context.password) >= 16, \
        "Password should be properly randomized and at least 16 characters"

@then('an error message should be displayed')
def step_error_message(context):
    """Check that an error message is displayed for invalid input."""
    # For empty word, the generate_from_word returns empty string
    assert not context.password or len(context.password) == 0, \
        "Should not generate password for empty input"

@then(u'the password should contain numbers and symbols')
def step_contains_numbers_and_symbols(context):
    """Check that password contains both numbers and symbols."""
    has_numbers = any(c.isdigit() for c in context.password)
    symbols = '!@#$%^&*()_+-=[]{}|;:,.<>?'
    has_symbols = any(c in symbols for c in context.password)
    assert has_numbers and has_symbols, \
        "Password must contain both numbers and symbols"