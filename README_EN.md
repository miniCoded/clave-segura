# Password Security Rater

A password strength checker built with Angular and Python. It evaluates passwords in real time and can generate stronger passwords from a base word.

## Features

- Real-time password validation
- Password generation with randomization and character substitution
- Three security levels:
  - **Secure**: 12+ characters and all requirements met
  - **Medium**: 7–11 characters and all requirements met
  - **Unsafe**: Missing requirements or too short
- Detection of common patterns (`password`, `123`, `qwerty`, etc.)
- Detailed requirement checklist
- BDD tests with Behave

## Tech Stack

- Frontend: Angular
- Backend: Flask
- Testing: Gherkin + Behave

## Setup

### Backend

```bash
pip install -r requirements.txt
python app.py
```

Runs on:

```text
http://localhost:5000
```

### Frontend

```bash
npm install
npm start
```

Runs on:

```text
http://localhost:4200
```

## Testing

Run all tests:

```bash
python -m behave
```

## Project Structure

```text
src/                  Angular application
app.py                Flask API
password_validator.py Validation logic
features/             BDD scenarios and steps
requirements.txt      Python dependencies
```

## Production Notes

For real deployments:

- Use HTTPS
- Hash passwords
- Add rate limiting
- Keep server-side validation
- Consider established libraries such as zxcvbn

## License

MIT
