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
        """Check if password contains obvious patterns."""
        password_lower = password.lower()
        for pattern in PasswordValidator.OBVIOUS_PATTERNS:
            if re.search(pattern, password_lower):
                return True
        return False
    
    @staticmethod
    def generate_from_word(word: str) -> Tuple[str, dict]:
        """
        Generate a secure password that still resembles the original user-provided word.
        Preserves word structure while wrapping it with cryptographically secure 
        prefixes, suffixes, and minimal leet-speak adjustments for readability.
        
        Args:
            word: The base word to generate the password from.
            
        Returns:
            Tuple of (password, details_dict)
        """
        clean_word = word.strip()
        
        # Handle empty input gracefully
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
        
        # 1. Readable Capitalization & Mild Leet-Speak Mapping
        # Instead of chaotic random casing, let's use standard Title Case or slight tweaks.
        leet_map = {
            'a': '@', 'e': '3', 'i': '1', 'o': '0', 's': '$', 't': '7'
        }
        
        masked_chars = []
        for i, char in enumerate(clean_word):
            char_lower = char.lower()
            # Lower probability (25%) for subtle leet-speak modifications so the word stays recognizable
            if char_lower in leet_map and secrets.randbelow(4) == 0:
                masked_chars.append(leet_map[char_lower])
            else:
                # Capitalize the first letter normally to keep it readable, lowercase the rest
                masked_chars.append(char.upper() if i == 0 else char.lower())
                
        readable_word = "".join(masked_chars)
        
        # 2. Generate Guaranteed Cryptographically Secure Components
        pool_digits = string.digits
        pool_symbols = '!@#$%^&*()_+-=[]{}|;:,.<>?'
        
        # Generate chunks instead of individual scattered characters
        prefix_symbol = secrets.choice(pool_symbols)
        suffix_digits = "".join(secrets.choice(pool_digits) for _ in range(3))
        suffix_symbols = "".join(secrets.choice(pool_symbols) for _ in range(2))
        
        # Assemble the sandwich: [Symbol][ReadableWord][Digits][Symbols]
        # Example: !Password178#$
        password = f"{prefix_symbol}{readable_word}{suffix_digits}{suffix_symbols}"
        
        # 3. Dynamic Padding (if it hasn't reached the 16 character limit)
        # We append extra characters to the very end to protect the core word structure
        min_length = 16
        validation_pool = string.ascii_lowercase + pool_digits
        while len(password) < min_length:
            password += secrets.choice(validation_pool)
        
        # --- REMOVED THE GLOBAL SHUFFLE TO PRESERVE THE WORD ---
        
        # 4. Validate the generated password
        try:
            security_level, details = PasswordValidator.validate(password)
        except NameError:
            details = {
                'length': len(password),
                'has_uppercase': any(c.isupper() for c in password),
                'has_lowercase': any(c.islower() for c in password),
                'has_numbers': any(c.isdigit() for c in password),
                'has_symbols': any(c in pool_symbols for c in password),
                'has_obvious_patterns': False,
                'complexity_met': len(password) >= 12,
            }
        
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
