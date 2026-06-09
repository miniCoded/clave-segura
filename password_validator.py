import re
import random
import string
from typing import Tuple

class PasswordValidator:
    """Validates passwords and returns security level."""
    
    OBVIOUS_PATTERNS = [
        r'123',
        r'abc',
        r'password',
        r'admin',
        r'qwerty',
        r'letmein',
        r'welcome',
        r'master',
        r'princess',
        r'dragons',
        r'sunshine',
        r'shadow',
        r'monkey',
        r'12345',
        r'111111',
        r'000000',
    ]
    
    @staticmethod
    def has_uppercase(password: str) -> bool:
        """Check if password contains uppercase letters."""
        return bool(re.search(r'[A-Z]', password))
    
    @staticmethod
    def has_lowercase(password: str) -> bool:
        """Check if password contains lowercase letters."""
        return bool(re.search(r'[a-z]', password))
    
    @staticmethod
    def has_numbers(password: str) -> bool:
        """Check if password contains numbers."""
        return bool(re.search(r'[0-9]', password))
    
    @staticmethod
    def has_symbols(password: str) -> bool:
        """Check if password contains special symbols."""
        return bool(re.search(r'[!@#$%^&*()_+\-=\[\]{};:\'",.<>?/\\|`~]', password))
    
    @staticmethod
    def has_obvious_patterns(password: str) -> bool:
        """Check if password contains obvious patterns."""
        password_lower = password.lower()
        for pattern in PasswordValidator.OBVIOUS_PATTERNS:
            if re.search(pattern, password_lower):
                return True
        return False
    
    @staticmethod
    def generate_from_word(word: str) -> Tuple[str, dict]:
        """
        Generate a secure password from a user-provided word.
        
        Args:
            word: The base word to generate password from
            
        Returns:
            Tuple of (password, details_dict)
        """
        # Clean the word
        clean_word = word.strip()
        
        if not clean_word:
            return '', {
                'length': 0,
                'has_uppercase': False,
                'has_lowercase': False,
                'has_numbers': False,
                'has_symbols': False,
                'has_obvious_patterns': True,
                'complexity_met': False,
            }
        
        # Get base word in different cases
        word_lower = clean_word.lower()
        word_upper = clean_word.upper()
        
        # Generate random components
        numbers = ''.join(random.choices(string.digits, k=3))
        symbols = ''.join(random.choices('!@#$%^&*()', k=2))
        extra_chars = ''.join(random.choices(string.ascii_letters, k=4))
        
        # Combine parts - use both lower and upper case versions of the word
        password_parts = [
            word_lower,
            word_upper,
            extra_chars,
            numbers,
            symbols
        ]
        
        # Shuffle the parts order
        random.shuffle(password_parts)
        password = ''.join(password_parts)
        
        # Ensure we have all requirements met
        # If the word itself has patterns, we need to mask them
        # Add more complexity if needed
        if len(password) < 12:
            password += ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=12 - len(password)))
        
        # Validate the generated password
        security_level, details = PasswordValidator.validate(password)
        
        return password, details
    
    @staticmethod
    def validate(password: str) -> Tuple[str, dict]:
        """
        Validate password and return security level and details.
        
        Returns:
            Tuple of (security_level, details_dict)
            security_level: 'secure', 'half-secure', or 'unsafe'
        """
        length = len(password)
        has_upper = PasswordValidator.has_uppercase(password)
        has_lower = PasswordValidator.has_lowercase(password)
        has_nums = PasswordValidator.has_numbers(password)
        has_syms = PasswordValidator.has_symbols(password)
        has_patterns = PasswordValidator.has_obvious_patterns(password)
        
        complexity_met = has_upper and has_lower and has_nums and has_syms
        no_obvious_patterns = not has_patterns
        
        details = {
            'length': length,
            'has_uppercase': has_upper,
            'has_lowercase': has_lower,
            'has_numbers': has_nums,
            'has_symbols': has_syms,
            'has_obvious_patterns': has_patterns,
            'complexity_met': complexity_met,
        }
        
        # Secure: 12-16 characters, all complexity requirements, no obvious patterns
        if 12 <= length <= 16 and complexity_met and no_obvious_patterns:
            return 'secure', details
        
        # Half-secure: 7-11 characters, all complexity requirements, no obvious patterns
        if 7 <= length <= 11 and complexity_met and no_obvious_patterns:
            return 'half-secure', details
        
        # Unsafe: less than 7 characters or doesn't meet complexity requirements
        return 'unsafe', details
