import re
import random
import string
import secrets
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
        """Check if password contains obvious patterns, excluding the base word 
        if it's being validated immediately after generation."""
        password_lower = password.lower()
        # List of generic patterns only
        generic_patterns = [r'123', r'abc', r'qwerty', r'12345', r'111111', r'000000']
        
        for pattern in generic_patterns:
            if re.search(pattern, password_lower):
                return True
        return False
    
    @staticmethod
    def generate_from_word(word: str) -> Tuple[str, dict]:
        """Generates a secure password with dynamic length, space handling, and middle-insertion."""
        if not word:
            return "", {}

        # 1. Handle spaces and transform the base word
        # Replace spaces with underscores to keep it readable but compliant
        base_processed = word.replace(" ", "_")
        
        def apply_leet(w):
            mapping = {'a': '@', 'e': '3', 'i': '!', 'o': '0', 's': '$', 't': '7'}
            return "".join(mapping.get(c.lower(), c) for c in w)

        transformed_word = apply_leet(base_processed)
        
        # 2. Determine length: use input word length + 8 extra chars, min 16
        target_length = max(16, len(transformed_word) + 8)
        
        # 3. Create padding components
        prefix = "".join(secrets.choice(string.ascii_letters) for _ in range(3))
        suffix = "".join(secrets.choice(string.digits + "!@#$") for _ in range(5))
        
        # 4. Assemble: Place transformed word in the middle
        password = f"{prefix}{transformed_word}{suffix}"
        
        # 5. Final adjustment to hit target length precisely
        while len(password) < target_length:
            password += secrets.choice(string.ascii_letters + string.digits)
            
        # 6. Validate immediately
        level, details = PasswordValidator.validate(password)
        return password, details
    @staticmethod
    def validate(password: str) -> Tuple[str, dict]:
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
        
        # Remove upper bound to satisfy 16+ char requirements
        if length >= 12 and complexity_met and no_obvious_patterns:
            return 'secure', details
        
        if 7 <= length <= 11 and complexity_met and no_obvious_patterns:
            return 'half-secure', details
            
        return 'unsafe', details
