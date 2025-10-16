# NeuroSleep
This archive includes:
- **vanilla-pwa/** — your original app **unchanged** (index.html, manifest.json, service-worker.js).
- **react-app/** — minimal React + TypeScript app scaffold.
- **angular-app/** — minimal Angular app scaffold.
- **backend-django/** — Django API with CORS enabled (mock endpoints).

## Quick Start

### Vanilla PWA (no build step)
1. Serve `vanilla-pwa/` with any static server (or open `index.html`).
2. Make sure to serve over HTTP(s) for service worker to work (localhost is fine).

### React
```bash
cd react-app
npm install
npm run dev
```

### Angular
```bash
cd angular-app
npm install
npm start
```

### Django API
```bash
cd backend-django
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py runserver 0.0.0.0:8000
```

API endpoints:
- `GET /api/v1/metrics/last-night`
- `GET /api/v1/metrics/nights`
- `GET /api/v1/journal`

Website `https://phionanamugga.github.io/neurosleep_monorepo/` (CORS is allowed).

## Notes
- Your original app is preserved in **vanilla-pwa/**; nothing is changed.
- The React and Angular apps are simple starting points. You can integrate the PWA UI later if you wish.
- The Django backend returns mock JSON compatible with your UI's data model.