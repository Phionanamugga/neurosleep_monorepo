import { bootstrapApplication } from '@angular/platform-browser'
import { Component } from '@angular/core'

@Component({
  selector: 'app-root',
  template: `
    <main style="font-family: system-ui, Arial; padding: 24px">
      <h1>NeuroSleep — Angular</h1>
      <p>This is a minimal Angular scaffold.</p>
      <p>Your original PWA remains untouched in <code>../vanilla-pwa</code>.</p>
    </main>
  `
})
class AppComponent {}

bootstrapApplication(AppComponent)