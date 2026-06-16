import { Component, OnInit } from '@angular/core';
import { FormControl, ReactiveFormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { PasswordValidatorService, PasswordValidationResponse } from './password-validator.service';
import { debounceTime, distinctUntilChanged, switchMap, tap, catchError } from 'rxjs/operators';
import { forkJoin, of } from 'rxjs';

@Component({
  selector: 'app-password-rater',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule],
  templateUrl: './password-rater.component.html',
  styleUrls: ['./password-rater.component.css']
})
export class PasswordRaterComponent implements OnInit {
  passwordControl = new FormControl('');
  wordControl = new FormControl('');

  // Main UI Data State Nodes
  generatedPasswords: string[] = [];
  activeMetrics: PasswordValidationResponse | null = null;
  activeInspectorSource: string = 'STANDBY';
  selectedGeneratedIndex: number | null = null;

  // Real-time Loading Status indicators
  isLoading = false;
  isGenerating = false;

  constructor(private passwordValidatorService: PasswordValidatorService) { }

  ngOnInit() {
    // Pipeline 1: Real-Time Input Testing Matrix (Character-by-character telemetry)
    this.passwordControl.valueChanges.pipe(
      debounceTime(150), // Ultra-fast bounce frame for native console response feel
      distinctUntilChanged(),
      tap((val) => {
        if (val) {
          this.isLoading = true;
          this.activeInspectorSource = 'MANUAL INBOUND REGISTER';
          this.selectedGeneratedIndex = null; // Remove selections from batch box
        } else {
          this.activeMetrics = null;
          this.activeInspectorSource = 'STANDBY';
        }
      }),
      switchMap((password) => {
        if (!password) return of(null);
        return this.passwordValidatorService.validatePassword(password).pipe(
          catchError((err) => {
            console.error('CRIT_ERR: Target register inspection crash', err);
            return of(null);
          })
        );
      })
    ).subscribe(result => {
      if (this.activeInspectorSource === 'MANUAL INBOUND REGISTER') {
        this.activeMetrics = result;
      }
      this.isLoading = false;
    });

    // Pipeline 2: Reactive Real-Time 4-Channel Parallel Password Generation Matrix
    this.wordControl.valueChanges.pipe(
      debounceTime(250),
      distinctUntilChanged(),
      tap((word) => {
        if (word && word.trim()) {
          this.isGenerating = true;
        } else {
          this.generatedPasswords = [];
          if (this.activeInspectorSource.startsWith('BATCH_CH')) {
            this.activeMetrics = null;
            this.activeInspectorSource = 'STANDBY';
            this.selectedGeneratedIndex = null;
          }
        }
      }),
      switchMap((word) => {
        if (!word || !word.trim()) return of([]);
        const cleanWord = word.trim();

        // ForkJoin calls the service 4 times concurrently to provide independent generation states
        return forkJoin([
          this.passwordValidatorService.generatePassword(cleanWord),
          this.passwordValidatorService.generatePassword(cleanWord),
          this.passwordValidatorService.generatePassword(cleanWord),
          this.passwordValidatorService.generatePassword(cleanWord)
        ]).pipe(
          catchError((err) => {
            console.error('CRIT_ERR: Parallel batch fork failure', err);
            return of([]);
          })
        );
      })
    ).subscribe(results => {
      this.isGenerating = false;
      if (results.length > 0) {
        // Parse the raw payload message blocks down to clean password strings
        this.generatedPasswords = results.map(res => res.message.split('Generated password: ')[1] || '');
        
        // Auto-select the first channel (CH-01) upon reactive update to make telemetry interactive instantly
        if (this.generatedPasswords.length > 0 && this.activeInspectorSource !== 'MANUAL INBOUND REGISTER') {
          this.selectGeneratedPassword(this.generatedPasswords[0], 0);
        }
      }
    });
  }

  // Routes metrics tracking to examine one of the specific 4 batch generated channels
  selectGeneratedPassword(password: string, index: number): void {
    if (!password) return;
    this.selectedGeneratedIndex = index;
    this.activeInspectorSource = `BATCH_CH-0${index + 1} ACTIVE RUN`;
    this.isLoading = true;

    // Reactively calls validation stats on the generated string to fill the sidebar console
    this.passwordValidatorService.validatePassword(password).subscribe({
      next: (res) => {
        this.activeMetrics = res;
        this.isLoading = false;
      },
      error: () => { this.isLoading = false; }
    });
  }

  getSecurityClass(): string {
    if (this.activeInspectorSource === 'MANUAL INBOUND REGISTER' && this.activeMetrics) {
      return this.activeMetrics.security_level;
    }
    return '';
  }

  getSecurityMessage(): string {
    if (!this.activeMetrics) return '';
    switch (this.activeMetrics.security_level) {
      case 'secure': return 'Status Secure. Core array characteristics verified.';
      case 'half-secure': return 'Status Warning. Recommended structural depth unfulfilled.';
      case 'unsafe': return 'Status Unsafe. Weak verification validation footprint.';
      default: return '';
    }
  }

  copyPassword(password: string, event: Event): void {
    event.stopPropagation(); // Avoid triggering selection mechanics during clipboard executions
    if (password) {
      navigator.clipboard.writeText(password);
    }
  }
}