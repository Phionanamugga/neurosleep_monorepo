# NeuroSleep
## About:
This is a sleep tracking app that helps users calculate their sleep debt, advises them on how to compensate it by calculating time spent on their past, current & future activities.

## File strucutre:
- **vanilla-pwa/** — Original app (index.html, manifest.json, service-worker.js).
- **react-app/** — minimal React + TypeScript app scaffold.
- **angular-app/** — minimal Angular app scaffold.
- **backend-django/** — Django API with CORS enabled (mock endpoints).

## Technologies & getting started:
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

## API endpoints:
- `GET /api/v1/metrics/last-night`
- `GET /api/v1/metrics/nights`
- `GET /api/v1/journal`

Website `https://phionanamugga.github.io/neurosleep_monorepo/` (CORS is allowed).

## Contributing
This is an open source project and contributuions are welcome:
1. Fork the project
2. Create your feature branch(git checkout -b feature1)
3. Commit your changes(git commit -m 'Creates readme')
4. Push to branch(git push origin feature1)
5. Open a pull request

## License
MIT License

## Contact
Your Name - @phionanamugga23@gmail.com  