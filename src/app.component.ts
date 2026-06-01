import { Component } from '@angular/core';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { PasswordRaterComponent } from './password-rater.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [PasswordRaterComponent],
  template: '<app-password-rater></app-password-rater>',
  styles: []
})
export class AppComponent { }
