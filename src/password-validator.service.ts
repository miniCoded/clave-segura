import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface PasswordValidationResponse {
  security_level: 'secure' | 'half-secure' | 'unsafe';
  message: string;
  details: {
    length: number;
    has_uppercase: boolean;
    has_lowercase: boolean;
    has_numbers: boolean;
    has_symbols: boolean;
    has_obvious_patterns: boolean;
    complexity_met: boolean;
  };
}

@Injectable({
  providedIn: 'root'
})
export class PasswordValidatorService {
  private apiUrl = 'https://clave-segura.onrender.com/api/validate-password';

  constructor(private http: HttpClient) { }

  validatePassword(password: string): Observable<PasswordValidationResponse> {
    return this.http.post<PasswordValidationResponse>(this.apiUrl, { password });
  }
}
