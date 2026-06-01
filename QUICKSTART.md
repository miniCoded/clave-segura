# 🚀 Quick Start Guide - Password Security Rater

## ✅ Project Created Successfully!

This folder now contains a complete **Password Security Rater** application with:
- **Backend**: Python Flask API with password validation
- **Frontend**: Angular component with real-time feedback
- **Testing**: 12 Gherkin BDD test scenarios (all passing ✅)

## 📁 File Structure

```
clave segura/
├── Python Backend
│   ├── app.py                      # Flask server
│   ├── password_validator.py       # Core validation logic
│   ├── requirements.txt            # Python dependencies
│   ├── behave.ini                  # Gherkin test configuration
│   └── features/
│       ├── password_rating.feature # 12 test scenarios
│       └── steps/
│           └── password_steps.py   # Test step definitions
│
├── Angular Frontend
│   ├── package.json                # NPM dependencies
│   ├── main.ts                     # Angular bootstrap
│   ├── app.component.ts            # Root component
│   ├── password-rater.component.ts # Main component
│   ├── password-rater.component.html
│   ├── password-rater.component.css
│   ├── password-validator.service.ts
│   ├── index.html
│   └── app.module.ts
│
├── README.md                        # Full documentation
└── QUICKSTART.md                    # This file
```

## 🎯 Quick Start (5 minutes)

### Step 1: Start the Python Backend

```bash
# Install Python dependencies (if not already done)
pip install -r requirements.txt

# Start the Flask server
python app.py
```

**Expected output:**
```
 * Running on http://127.0.0.1:5000
```

The API will be available at: `http://localhost:5000`

### Step 2: Start the Angular Frontend

**In a new terminal/command prompt:**

```bash
# Install Node dependencies
npm install

# Start the Angular development server
npm start
```

**Expected output:**
```
✔ Compiled successfully.
Application bundle generated successfully.
```

The app will automatically open in your browser at: `http://localhost:4200`

### Step 3: Test It Out

1. Open the app in your browser (should be automatic with `npm start`)
2. Type a password in the textbox
3. Watch the textbox color change:
   - 🟢 **Green**: Secure (12+ chars, uppercase, lowercase, numbers, symbols)
   - 🟠 **Amber**: Half-secure (7-11 chars, all complexity requirements)
   - 🔴 **Red**: Unsafe (too short or missing complexity requirements)

## 🧪 Run the Tests

### Gherkin/Behave Tests (Backend Validation)

```bash
# Run all tests
python -m behave

# Run with detailed output
python -m behave --no-capture

# Run specific feature
python -m behave features/password_rating.feature
```

**Expected output:**
```
1 feature passed, 0 failed, 0 skipped
12 scenarios passed, 0 failed, 0 skipped
53 steps passed, 0 failed, 0 skipped, 0 undefined
```

## 🔐 Security Level Rules

### 🟢 SECURE
✅ 12+ characters
✅ Uppercase letters (A-Z)
✅ Lowercase letters (a-z)
✅ Numbers (0-9)
✅ Symbols (!@#$%^&*...)
✅ No obvious patterns

**Example:** `MyStr0ng@Pwd99`

### 🟠 HALF-SECURE
✅ 7-11 characters
✅ Uppercase letters (A-Z)
✅ Lowercase letters (a-z)
✅ Numbers (0-9)
✅ Symbols (!@#$%^&*...)
✅ No obvious patterns

**Example:** `MyP@ss99`

### 🔴 UNSAFE
❌ Less than 7 characters, OR
❌ Missing any complexity requirement

**Examples:**
- `short` (too short)
- `password123` (no uppercase or symbols)
- `Pass123` (no symbols)
- `password@123` (contains obvious pattern)

## 📊 Test Coverage

12 comprehensive Gherkin scenarios test:
- ✅ Secure passwords
- ✅ Half-secure passwords
- ✅ Unsafe passwords (various reasons)
- ✅ Obvious pattern detection
- ✅ Empty passwords
- ✅ Missing complexity requirements
- ✅ Edge cases

## 🛠️ Available Commands

### Backend
```bash
python app.py              # Start Flask server on port 5000
python -m behave          # Run all Gherkin tests
python -m pytest          # Run unit tests (if added)
```

### Frontend
```bash
npm start                 # Start dev server on port 4200
npm run build            # Production build
npm test                 # Run Angular tests
npm run lint             # Run linter
```

## 🌐 API Endpoints

### Validate Password
**POST** `http://localhost:5000/api/validate-password`

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

### Health Check
**GET** `http://localhost:5000/api/health`

**Response:**
```json
{
  "status": "ok"
}
```

## 🐛 Troubleshooting

### Port Already in Use
```bash
# Change backend port (edit app.py, line ~26)
app.run(debug=True, port=5001)  # Use 5001 instead

# Change frontend port
ng serve --port 4201
```

### CORS Error
Make sure Flask-CORS is installed:
```bash
pip install flask-cors
```

### Backend not starting
```bash
# Check if port 5000 is available
lsof -i :5000  # On Mac/Linux
netstat -ano | findstr :5000  # On Windows
```

### Frontend can't find backend
- Ensure backend is running on `http://localhost:5000`
- Check network tab in browser DevTools
- Verify CORS is enabled in Flask

## 📚 Project Architecture

```
User Types Password
        ↓
    Angular Component
        ↓
    HTTP POST Request
        ↓
    Flask Backend
        ↓
    PasswordValidator Class
        ↓
    Validation Logic
        ↓
    Return Security Level
        ↓
    Update UI Color & Feedback
```

## 🎨 Customization

### Change Colors
Edit `password-rater.component.css`:
```css
.input-secure {
  border-color: #4caf50;      /* Green */
  background-color: #f1f8f4;
}

.input-half-secure {
  border-color: #ff9800;      /* Amber */
  background-color: #fff8f0;
}

.input-unsafe {
  border-color: #f44336;      /* Red */
  background-color: #fef5f5;
}
```

### Add Obvious Patterns
Edit `password_validator.py`, add to `OBVIOUS_PATTERNS` list:
```python
OBVIOUS_PATTERNS = [
    # ... existing patterns ...
    r'newpattern',  # Add your pattern
]
```

### Adjust Security Rules
Edit `password_validator.py` in the `validate()` method to change:
- Length requirements
- Complexity requirements
- Pattern detection logic

## 🚀 Next Steps

1. **Integrate into your app**: Use the `PasswordValidatorService` in other components
2. **Add database**: Store password history (encrypted) using SQLite/PostgreSQL
3. **Add user accounts**: Create login/registration system
4. **Add notifications**: Email warnings for weak passwords
5. **Mobile app**: Convert to mobile app with Ionic
6. **Advanced patterns**: Use `zxcvbn` library for machine learning-based password strength

## 📖 Resources

- **Angular**: https://angular.io/
- **Flask**: https://flask.palletsprojects.com/
- **Behave (Gherkin)**: https://behave.readthedocs.io/
- **Password Security**: https://owasp.org/www-community/password

## 📝 License

MIT License - Free to use and modify

---

**Need help?** Check the full README.md or review the test scenarios in `features/password_rating.feature`

**All tests passing:** ✅ 12/12 scenarios ✅ 53/53 steps
