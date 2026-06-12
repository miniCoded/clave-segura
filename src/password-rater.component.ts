import { Component, OnInit } from '@angular/core';
import { FormControl, ReactiveFormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { PasswordValidatorService, PasswordValidationResponse, PasswordGenerationResponse } from './password-validator.service';
import { debounceTime, distinctUntilChanged, switchMap } from 'rxjs/operators';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-password-rater',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule],
  templateUrl: './password-rater.component.html',
  styleUrls: ['./password-rater.component.css'],
  animations: [] // Removed complex triggers to support modern console snapping
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
        console.error('CRIT_ERR: Failed payload check', error);
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
        console.error('CRIT_ERR: Failed generator run', error);
        this.isGenerating = false;
      }
    );
  }

  getSecurityClass(): string {
    if (!this.validationResult) return '';
    return this.validationResult.security_level;
  }

  getSecurityMessage(): string {
    if (!this.validationResult) return '';
    const level = this.validationResult.security_level;
    switch (level) {
      case 'secure':
        return 'Status Secure. Complexity requirements met.';
      case 'half-secure':
        return 'Status Warning. Recommended structure depth unfulfilled.';
      case 'unsafe':
        return 'Status Unsafe. Insecure entry schema detected.';
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
          console.error('CRIT_ERR: Thread compilation crash', error);
        }
      );
    }
  }

  copyGeneratedPassword(): void {
    if (this.generatedPassword) {
      navigator.clipboard.writeText(this.generatedPassword);
    }
  }
}