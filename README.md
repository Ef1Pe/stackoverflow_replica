# Stack Overflow Replica

Pixel-perfect recreation of the Stack Overflow questions landing page with Tailwind-driven UI, multi-section static pages, and a Flask backend that supports runtime content injection.

## Features
- ✅ High-fidelity clone of the `/questions` experience (header, filters, feed, sidebar, footer)
- ✅ Five additional section pages (`featured.html`, `hot.html`, `week.html`, `month.html`, `bountied.html`) generated from the same template for seamless navigation
- ✅ Tailwind CSS + custom tokens for exact typography, spacing, and Stack Overflow branding
- ✅ Vanilla JS renderer with reusable question card builder and global `SOReplica.injectQuestion()` hook
- ✅ Flask server with Agenticverse-compatible `entity.py` + `metadata.py` for scripted content injection
- ✅ API endpoint (`/api/content`) to inspect injected items at runtime

## Project Structure
```
/workspace
├── index.html               # Newest/Interesting questions
├── featured.html            # Featured tab view
├── hot.html                 # Hot tab view
├── week.html                # Week tab view
├── month.html               # Month tab view
├── bountied.html            # Bountied filter view
├── css/
│   └── styles.css           # Custom overrides + utility classes
├── js/
│   └── main.js              # Question renderer + injection helper
├── images/                  # Placeholder for static assets
├── server.py                # Flask app + injection helpers
├── entity.py                # Agenticverse entity definition
├── metadata.py              # Metadata schema
├── requirements.txt         # Python dependencies
└── docs/
    └── site_analysis.md     # Color, layout, and component specs
```

## Tech Stack
- HTML5 + Tailwind CSS (via CDN) for markup/styling
- Vanilla JavaScript for rendering and interaction
- Flask for backend routing and content injection
- Agenticverse entity + metadata contracts for orchestration

## Getting Started
```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Start the replica server (default port 5000)
python server.py

# 3. Open the site
open http://localhost:5000
```

### Injecting Custom Content
```python
from server import start_server

start_server(
    port=5000,
    content_data={
        'section': 'featured',
        'title': 'Why does my socket keep disconnecting?',
        'excerpt': 'Troubleshooting TCP disconnects when mixing IPv4 + IPv6 listeners.',
        'user': 'netguru',
        'votes': 4,
        'answers': 1,
        'views': 120,
        'tags': ['sockets', 'python'],
        'badge': 'Featured',
    },
)
```
Injected rows receive the `injected-card` class, making them visually stand out with a gold dashed outline.

### JavaScript Injection Helper
```js
window.SOReplica.injectQuestion({
  title: 'Custom runtime question',
  excerpt: 'Injected directly from the console.',
  tags: ['stack-overflow'],
  user: 'agentic-bot',
  badge: 'Live',
});
```

## Metadata Contract
`metadata.py` exposes the Agenticverse schema with fields for section targeting, stats (votes/answers/views), author attribution, tags, and badges so automations can reason about the UI.

## Known Limitations
- The dataset is mocked; no live Stack Overflow API calls are made.
- Authentication, search, and pagination are static replicas.
- Fonts are loaded from Google Fonts rather than Stack Overflow’s CDN for portability.

Feel free to adapt the layout or metadata schema for additional Stack Exchange-style properties.
