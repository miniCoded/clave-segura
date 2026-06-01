from behave import given, when, then
from password_validator import PasswordValidator

@given('I enter a password "{password}"')
def step_enter_password(context, password):
    # Handle empty password (Gherkin interprets "" as empty string)
    context.password = password if password else ""

@given('I enter an empty password')
def step_enter_empty_password(context):
    context.password = ""

@when('I submit the password')
def step_submit_password(context):
    context.security_level, context.details = PasswordValidator.validate(context.password)

@then('the password should be rated as "{expected_level}"')
def step_check_security_level(context, expected_level):
    assert context.security_level == expected_level, \
        f"Expected {expected_level}, got {context.security_level}"

@then('the textbox should be colored "{color}"')
def step_check_color(context, color):
    color_map = {
        'green': 'secure',
        'amber': 'half-secure',
        'red': 'unsafe'
    }
    expected_level = color_map[color]
    assert context.security_level == expected_level, \
        f"Expected color {color} ({expected_level}), got {context.security_level}"

@then('the feedback should show all requirements met')
def step_check_all_requirements(context):
    details = context.details
    assert details['has_uppercase'], "Missing uppercase"
    assert details['has_lowercase'], "Missing lowercase"
    assert details['has_numbers'], "Missing numbers"
    assert details['has_symbols'], "Missing symbols"
    assert not details['has_obvious_patterns'], "Contains obvious patterns"
    assert details['length'] >= 12, "Too short for secure"

@then('the feedback should indicate 7-11 characters')
def step_check_half_secure_length(context):
    assert 7 <= context.details['length'] <= 11, \
        f"Expected 7-11 characters, got {context.details['length']}"

@then('the feedback should indicate too short')
def step_check_too_short(context):
    assert context.details['length'] < 7, \
        f"Expected less than 7 characters, got {context.details['length']}"

@then('the feedback should indicate obvious patterns detected')
def step_check_obvious_patterns(context):
    assert context.details['has_obvious_patterns'], \
        "Expected obvious patterns to be detected"
