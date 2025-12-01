"""Flask server for the Stack Overflow replica entity."""

from __future__ import annotations

from pathlib import Path
from typing import Dict, List

from flask import Flask, jsonify, send_from_directory

try:
  from agenticverse_entities.base.server_base import start_server as start_base_server  # type: ignore
except ImportError:  # pragma: no cover - dev fallback
  start_base_server = None  # type: ignore

BASE_DIR = Path(__file__).parent
STATIC_DIR = BASE_DIR

InjectedItem = Dict[str, str]

injected_questions: List[InjectedItem] = []


def build_question_card(item: InjectedItem) -> str:
  """Generate Stack Overflow style markup for an injected question."""
  tags_html = ''.join(
      f'<span class="tag-pill">{tag}</span>' for tag in item.get('tags', [])
  )
  badge_html = (
      f"<span class='ml-2 rounded-full bg-orange-100 text-so-sunrise text-xs px-2 py-0.5'>{item['badge']}</span>"
      if item.get('badge') else ''
  )
  answered = item.get('answered', False)
  answer_class = 'stat answer' if answered else 'stat'
  return f"""
    <!-- injected question -->
    <article class="question-row injected-card">
      <div class="question-stats">
        <div class="stat"><strong>{item.get('votes', 0)}</strong><span>votes</span></div>
        <div class="{answer_class}"><strong>{item.get('answers', 0)}</strong><span>answers</span></div>
        <div class="stat"><strong>{item.get('views', 0)}</strong><span>views</span></div>
      </div>
      <div>
        <div class="flex items-center">
          <a href="{item.get('url', '#')}" class="question-title">{item.get('title', 'Untitled question')}</a>
          {badge_html}
        </div>
        <p class="text-sm text-so-muted mb-3">{item.get('excerpt', item.get('description', ''))}</p>
        <div class="question-meta">
          <div class="flex flex-wrap gap-2">{tags_html}</div>
          <span class="ml-auto text-xs text-so-muted">asked {item.get('date', 'just now')} by <strong>{item.get('user', item.get('author', 'anonymous'))}</strong></span>
        </div>
      </div>
    </article>
  """


def inject_into_html(html_content: str, section: str | None) -> str:
  """Insert injected questions above the client-rendered list."""
  if not injected_questions:
    return html_content

  marker = '<section id="question-list" class="space-y-4">'
  marker_index = html_content.find(marker)
  if marker_index == -1:
    return html_content

  insert_index = marker_index + len(marker)
  cards: List[str] = []
  for item in injected_questions:
    item_section = item.get('section')
    if item_section in (None, 'all') or section in (None, 'index') or item_section == section:
      cards.append(build_question_card(item))

  if not cards:
    return html_content

  return html_content[:insert_index] + ''.join(cards) + html_content[insert_index:]


def create_app() -> Flask:
  app = Flask(__name__, static_folder=None)

  @app.route('/')
  def home():
    return render_page('index.html', section='interesting')

  @app.route('/<path:page>.html')
  def section_page(page: str):
    file_path = STATIC_DIR / f'{page}.html'
    if not file_path.exists():
      return ('Page not found', 404)
    return render_page(f'{page}.html', section=page)

  @app.route('/css/<path:filename>')
  def serve_css(filename: str):
    return send_from_directory(STATIC_DIR / 'css', filename)

  @app.route('/js/<path:filename>')
  def serve_js(filename: str):
    return send_from_directory(STATIC_DIR / 'js', filename)

  @app.route('/images/<path:filename>')
  def serve_images(filename: str):
    return send_from_directory(STATIC_DIR / 'images', filename)

  @app.route('/api/content')
  def content_api():
    return jsonify({'content': injected_questions, 'count': len(injected_questions)})

  return app


def render_page(filename: str, section: str | None = None):
  html_path = STATIC_DIR / filename
  with html_path.open('r', encoding='utf-8') as file:
    html_content = file.read()
  if section:
    html_content = inject_into_html(html_content, section)
  return html_content


def start_server(port: int = 5000, threaded: bool = False, content_data: Dict | None = None):
  """Start the Flask dev server and optionally inject starter content."""
  if content_data and content_data.get('title'):
    question = dict(content_data)
    question.setdefault('section', 'interesting')
    injected_questions.append(question)

  app = create_app()

  if start_base_server:
    return start_base_server(app, port=port, threaded=threaded)

  return app.run(port=port, threaded=threaded)


if __name__ == '__main__':
  start_server()
