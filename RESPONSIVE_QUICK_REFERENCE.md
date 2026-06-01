# Responsive Design Quick Reference

## Breakpoint Quick Guide

| Device | Width | Container | Grid | Font | Use Case |
|--------|-------|-----------|------|------|----------|
| **Desktop XL** | 1400px+ | 900px | 3col | 40px | Large monitors, 4K |
| **Desktop** | 1024-1399px | 800px | 3col | 36px | Standard desktop/laptop |
| **Tablet** | 768-1023px | 100% | 2col | 28px | iPad, Android tablets |
| **Large Phone** | 640-767px | 100% | 2col | 24px | iPhone 12/13 Plus |
| **Phone** | 480-639px | 100% | 2col | 22px | Most modern phones |
| **Small Phone** | <480px | 100% | 2col | 18px | iPhone SE, older phones |

## Container Sizing

```css
/* By screen size */
1400px+  → max-width: 900px, padding: 50px
1024px   → max-width: 800px, padding: 45px
768px    → padding: 32px
640px    → padding: 24px
480px    → padding: 18px
<480px   → padding: 14px
```

## Typography Scaling

```
Desktop:  h1 = 40px,  body = 15px
Tablet:   h1 = 28px,  body = 13px
Phone:    h1 = 22px,  body = 12px
Small:    h1 = 18px,  body = 10px
```

## Grid Evolution

### Requirements Grid
```
Desktop (1400px)  → 3 columns (repeat(3, 1fr))
Large (1024px)    → 3 columns
Tablet (768px)    → 2 columns (repeat(2, 1fr))
Phone (640px)     → 2 columns
Small (480px)     → 2 columns (tight)
Tiny (<480px)     → 2 columns (minimal)
```

### Legend Grid
```
Desktop (1400px)  → 3 columns
Tablet (768px)    → 2 columns
Phone (640px)     → 1 column (stacked)
Small (480px)     → 1 column
```

## Touch Optimization

```css
/* Minimum tap target size */
48px height/width

/* Mobile input (prevents zoom) */
font-size: 16px+

/* Active states for touch */
.requirement:active { background: #f0f0f0; }
```

## Media Query Template

```css
/* Large Desktop (1400px+) */
@media (min-width: 1400px) {
  .container { max-width: 900px; padding: 50px; }
}

/* Desktop (1024px-1399px) */
@media (min-width: 1024px) and (max-width: 1399px) {
  .container { max-width: 800px; padding: 45px; }
}

/* Tablet (768px-1023px) */
@media (min-width: 768px) and (max-width: 1023px) {
  .container { padding: 32px; }
}

/* Phone (640px-767px) */
@media (min-width: 640px) and (max-width: 767px) {
  .container { padding: 24px; }
}

/* Small Phone (480px-639px) */
@media (min-width: 480px) and (max-width: 639px) {
  .container { padding: 18px; }
}

/* Tiny Phone (<480px) */
@media (max-width: 479px) {
  .container { padding: 14px; }
}

/* Landscape (<600px height) */
@media (orientation: landscape) and (max-height: 600px) {
  .container { max-height: 90vh; overflow-y: auto; }
}

/* High DPI (2x+ pixel ratio) */
@media (-webkit-min-device-pixel-ratio: 2), (min-resolution: 192dpi) {
  .element { border-width: 1.5px; }
}

/* Touch devices (no hover) */
@media (hover: none) and (pointer: coarse) {
  .button { min-height: 48px; }
}
```

## Component Responsive Properties

### Header Icon
```
Desktop:  48px
Tablet:   40px
Phone:    32px
Small:    28px
```

### Header H1
```
Desktop:  32px → 40px (1400px+)
Tablet:   28px
Phone:    24px → 22px (480px)
Small:    18px
```

### Input Field
```
Desktop:  14px padding, 18px height, 18px font
Tablet:   14px padding, 16px height, 15px font
Phone:    12px padding, 44px height, 13px font
Small:    10px padding, 40px height, 12px font
```

### Requirements Grid
```
Gap: 12px → 11px → 10px → 8px → 6px
Padding: 16px → 14px → 12px → 10px → 8px
BorderRadius: 10px → 8px → 6px
```

## Testing Checklist

- [ ] Desktop (1920x1080)
- [ ] Laptop (1366x768)
- [ ] Tablet Portrait (768x1024)
- [ ] Tablet Landscape (1024x768)
- [ ] Large Phone (640x960)
- [ ] Phone (375x667)
- [ ] Small Phone (320x568)
- [ ] Landscape Phone (667x375)
- [ ] Font Zoom (+200%)
- [ ] High DPI Display
- [ ] Touch Device
- [ ] Slow Network (3G)
- [ ] Low-End Device

## Common Issues & Fixes

### Text Too Small
```css
/* Solution: Increase minimum font size */
min-font-size: 11px;
/* Or use clamp for smooth scaling */
font-size: clamp(11px, 2vw, 40px);
```

### Layout Breaking
```css
/* Solution: Use max-width constraint */
.container { 
  width: 100%; 
  max-width: 900px; 
}
```

### Tap Targets Too Small
```css
/* Solution: Ensure 48px minimum */
.button {
  min-height: 48px;
  min-width: 48px;
  padding: 12px 16px;
}
```

### High DPI Blurry
```css
/* Solution: Adjust borders */
border-width: 1.5px; /* High DPI */
border-width: 1px;   /* Standard DPI */
```

### Touch Hover Issues
```css
/* Solution: Use media query */
@media (hover: none) and (pointer: coarse) {
  .element:hover { /* won't trigger on touch */ }
  .element:active { /* use active for touch */ }
}
```

## Performance Tips

1. **CSS Organization**: Mobile-first approach
2. **Media Query Count**: Keep under 20 for performance
3. **Selector Specificity**: Avoid overly specific selectors
4. **Animations**: Use transform and opacity (GPU-accelerated)
5. **Images**: Use responsive img tags
6. **Viewport Meta**: Always include viewport meta tag

## Debugging Responsive Issues

```javascript
// In browser DevTools console
// Get current breakpoint
const width = window.innerWidth;
console.log(`Current width: ${width}px`);

// Test media query
console.log(
  matchMedia('(max-width: 640px)').matches ? 
  'Mobile' : 'Desktop'
);

// Monitor resize events
window.addEventListener('resize', () => {
  console.log(`Resized to: ${window.innerWidth}x${window.innerHeight}`);
});
```

## CSS Budget Status

```
Component CSS:    12.38 kB
Warning Limit:    13 kB ✅
Error Limit:      25 kB ✅
Global CSS:       269 bytes
Total CSS:        ~12.65 kB
Gzipped:          ~5.06 kB (60% reduction)
```

## Browser Support

| Feature | Chrome | Firefox | Safari | Edge | Support |
|---------|--------|---------|--------|------|---------|
| CSS Grid | 90+ | 88+ | 14+ | 90+ | ✅ |
| Flexbox | 90+ | 88+ | 14+ | 90+ | ✅ |
| Media Queries | 90+ | 88+ | 14+ | 90+ | ✅ |
| CSS Variables | 90+ | 88+ | 14+ | 90+ | ✅ |
| Animations | 90+ | 88+ | 14+ | 90+ | ✅ |

## Responsive Testing Tools

- **Chrome DevTools**: Built-in responsive design mode
- **Firefox Responsive Design Mode**: Similar to Chrome
- **Safari Responsive Design**: Fewer features than Chrome
- **Am I Responsive**: Quick multi-device preview
- **Responsively App**: Native app for testing
- **BrowserStack**: Real device testing
- **Google Mobile-Friendly Test**: SEO testing
- **Lighthouse**: Performance & accessibility audit

## References & Resources

- [MDN: Responsive Design](https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Responsive_Design)
- [CSS-Tricks: A Complete Guide to Grid](https://css-tricks.com/snippets/css/complete-guide-grid/)
- [Can I Use: Browser Support Tables](https://caniuse.com/)
- [Web.dev: Responsive Web Design Basics](https://web.dev/responsive-web-design-basics/)

---

**Quick Start**: Use this guide to quickly understand and maintain responsive design across different screen sizes. For detailed information, refer to `RESPONSIVE_DESIGN.md`.
