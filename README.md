# Password Security Rater 🔐

A comprehensive password rating application built with Angular, Python, and Gherkin BDD testing. The app evaluates password strength in real-time and provides visual feedback with color-coded security levels.

## Features

✅ **Real-time Password Validation**
- Instant feedback as user types
- Debounced API calls for performance

✅ **Color-Coded Security Levels**
- 🟢 **Green (Secure)**: 12+ characters with all requirements
- 🟠 **Amber (Half-Secure)**: 7-11 characters with all requirements
- 🔴 **Red (Unsafe)**: Less than 7 characters or missing requirements

✅ **Comprehensive Validation**
- Password length requirements
- Mixed case letters (uppercase & lowercase)
- Numbers (0-9)
- Special symbols (!@#$%^&*...)
- Obvious pattern detection (qwerty, password, 123, etc.)

✅ **Detailed Feedback**
- Shows each requirement and its status
- Helpful hints for improvement
- Real-time strength analysis

## Requirements

- **Backend**: Python 3.7+
- **Frontend**: Node.js 16+, Angular 16+
- **Testing**: Behave (Gherkin for Python)

## Project Structure

```
clave segura/
├── Python Backend
│   ├── app.py                    # Flask application
│   ├── password_validator.py     # Core validation logic
│   ├── requirements.txt          # Python dependencies
│   └── features/                 # Gherkin tests
│       ├── password_rating.feature
│       └── steps/
│           └── password_steps.py
│
├── Angular Frontend
│   ├── app.component.ts          # Root component
│   ├── app.module.ts             # App module
│   ├── main.ts                   # Bootstrap
│   ├── index.html                # HTML template
│   ├── password-rater.component.ts
│   ├── password-rater.component.html
│   ├── password-rater.component.css
│   ├── password-validator.service.ts
│   └── package.json              # NPM dependencies
```

## Installation

### Backend Setup

```bash
# Install Python dependencies
pip install -r requirements.txt

# Run the Flask backend
python app.py
```

The backend will start on `http://localhost:5000`

### Frontend Setup

```bash
# Install Node dependencies
npm install

# Start Angular development server
npm start
```

The frontend will open on `http://localhost:4200`

## API Endpoints

### POST /api/validate-password
Validates a password and returns its security level.

**Request:**
```json
{
  "password": "MyP@ssw0rd123"
}
```

**Response:**
```json
{
  "security_level": "secure",
  "message": "Password is secure",
  "details": {
    "length": 13,
    "has_uppercase": true,
    "has_lowercase": true,
    "has_numbers": true,
    "has_symbols": true,
    "has_obvious_patterns": false,
    "complexity_met": true
  }
}
```

### GET /api/health
Health check endpoint.

**Response:**
```json
{
  "status": "ok"
}
```

## Password Security Levels

### 🟢 Secure
- **Length**: 12+ characters
- **Requirements**: Must have uppercase, lowercase, numbers, AND symbols
- **Patterns**: No obvious patterns (qwerty, password, 123, etc.)

### 🟠 Half-Secure
- **Length**: 7-11 characters
- **Requirements**: Must have uppercase, lowercase, numbers, AND symbols
- **Patterns**: No obvious patterns

### 🔴 Unsafe
- **Length**: Less than 7 characters
- **OR** Missing any of the complexity requirements

## Testing with Gherkin

Run the BDD tests using Behave:

```bash
# Run all tests
behave

# Run specific feature file
behave features/password_rating.feature

# Run with detailed output
behave --no-capture
```

### Test Coverage

The test suite includes 12 scenarios covering:
- Secure password validation
- Half-secure password validation
- Unsafe passwords (too short, missing requirements)
- Obvious pattern detection
- Edge cases (empty password, special cases)

Example test scenario:
```gherkin
Scenario: Password is secure with 12+ characters and all requirements
  Given I enter a password "MyP@ssw0rd123"
  When I submit the password
  Then the password should be rated as "secure"
  And the textbox should be colored "green"
  And the feedback should show all requirements met
```

## Common Password Patterns Detected

The validator detects common patterns to prevent weak passwords:

- Sequential patterns: `123`, `abc`
- Dictionary words: `password`, `admin`, `letmein`, `welcome`, `master`
- Pop culture references: `princess`, `dragons`, `monkey`, `sunshine`, `shadow`
- Repeated numbers: `111111`, `000000`
- Keyboard patterns: `qwerty`

## Usage Example

### Angular Component

```typescript
// In your component
import { PasswordValidatorService } from './password-validator.service';

export class MyComponent {
  constructor(private validatorService: PasswordValidatorService) {}

  checkPassword(pwd: string) {
    this.validatorService.validatePassword(pwd).subscribe(result => {
      console.log(result.security_level); // 'secure', 'half-secure', or 'unsafe'
      console.log(result.details);
    });
  }
}
```

### Python Validation

```python
from password_validator import PasswordValidator

level, details = PasswordValidator.validate("MyP@ssw0rd123")
print(level)  # 'secure'
print(details)  # Dictionary with validation details
```

## Security Notes

⚠️ **Important**: This application is for **educational purposes**. For production use:

1. **Never send passwords over unencrypted connections** - Always use HTTPS
2. **Hash passwords on the backend** - Never store plain text
3. **Implement rate limiting** - Prevent brute force attacks
4. **Add server-side validation** - Never trust client-side validation alone
5. **Use established libraries** - Consider using libraries like `zxcvbn` for production

## Browser Compatibility

- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)

## Performance

- **Debounce delay**: 300ms (prevents excessive API calls)
- **Response time**: < 10ms per password validation
- **Bundle size**: ~200KB (Angular + dependencies)

## Development Tips

### Adding New Validation Rules

1. Add the rule to `PasswordValidator` class in `password_validator.py`
2. Add corresponding Gherkin scenario in `features/password_rating.feature`
3. Implement step definition in `features/steps/password_steps.py`
4. Test with `behave`

### Styling Customization

Edit `password-rater.component.css` to customize:
- Colors (secure: #4caf50, half-secure: #ff9800, unsafe: #f44336)
- Border radius and shadows
- Font sizes and spacing

## Troubleshooting

### Backend won't start
```bash
# Check if port 5000 is in use
# Change port in app.py: app.run(port=5001)
```

### Frontend can't reach backend
```bash
# Ensure backend is running on http://localhost:5000
# Check CORS settings in app.py (Flask-CORS is enabled)
```

### Tests failing
```bash
# Make sure password_validator.py is in the same directory as features/
# Run: behave --no-capture for detailed output
```

## License

MIT License - Feel free to use this project for educational purposes.

## Contributing

Feel free to submit issues and enhancement requests!

---

Created with ❤️ for secure password practices
