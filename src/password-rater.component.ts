import { Component, OnInit } from '@angular/core';
import { FormControl, ReactiveFormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { trigger, transition, style, animate } from '@angular/animations';
import { PasswordValidatorService, PasswordValidationResponse, PasswordGenerationResponse } from './password-validator.service';
import { debounceTime, distinctUntilChanged, switchMap, startWith } from 'rxjs/operators';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-password-rater',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule],
  templateUrl: './password-rater.component.html',
  styleUrls: ['./password-rater.component.css'],
  animations: [
    trigger('fadeIn', [
      transition(':enter', [
        style({ opacity: 0, transform: 'translateY(10px)' }),
        animate('400ms 100ms ease-out', style({ opacity: 1, transform: 'translateY(0)' }))
      ])
    ])
  ]
})
export class PasswordRaterComponent implements OnInit {
  passwordControl = new FormControl('');
  wordControl = new FormControl('');
  validationResult: PasswordValidationResponse | null = null;
  isLoading = false;
  generatedPassword: string | null = null;
  isGenerating = false;

  constructor(private passwordValidatorService: PasswordValidatorService) { }

  ngOnInit() {
    this.passwordControl.valueChanges.pipe(
      debounceTime(300),
      distinctUntilChanged(),
      switchMap((password: any) => {
        this.isLoading = true;
        return this.passwordValidatorService.validatePassword(password || '');
      })
    ).subscribe(
      result => {
        this.validationResult = result;
        this.generatedPassword = null;
        this.isLoading = false;
      },
      error => {
        console.error('Error validating password', error);
        this.isLoading = false;
      }
    );

    this.wordControl.valueChanges.pipe(
      debounceTime(300),
      distinctUntilChanged(),
      switchMap((word: string | null) => {
        if (word && word.trim()) {
          this.isGenerating = true;
          return this.passwordValidatorService.generatePassword(word.trim());
        }
        return new Observable<PasswordGenerationResponse>(() => {});
      })
    ).subscribe(
      result => {
        this.generatedPassword = result.message.split('Generated password: ')[1] || null;
        this.isGenerating = false;
      },
      error => {
        console.error('Error generating password', error);
        this.isGenerating = false;
      }
    );
  }

  getSecurityClass(): string {
    if (!this.validationResult) return '';
    switch (this.validationResult.security_level) {
      case 'secure':
        return 'secure';
      case 'half-secure':
        return 'half-secure';
      case 'unsafe':
      default:
        return 'unsafe';
    }
  }

  getSecurityMessage(): string {
    if (!this.validationResult) return '';
    const level = this.validationResult.security_level;
    switch (level) {
      case 'secure':
        return 'Excellent! Your password is secure';
      case 'half-secure':
        return 'Good. Consider adding more characters';
      case 'unsafe':
        return 'Weak password. Please strengthen it';
      default:
        return '';
    }
  }

  generatePasswordFromWord(): void {
    const word = this.wordControl.value;
    if (word && word.trim()) {
      this.passwordValidatorService.generatePassword(word.trim()).subscribe(
        result => {
          this.generatedPassword = result.message.split('Generated password: ')[1] || null;
        },
        error => {
          console.error('Error generating password', error);
        }
      );
    }
  }

  copyGeneratedPassword(): void {
    if (this.generatedPassword) {
      navigator.clipboard.writeText(this.generatedPassword);
      alert('Password copied to clipboard!');
    }
  }
}

