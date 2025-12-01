const questionList = document.getElementById('question-list');
const tabLinks = document.querySelectorAll('.tab-link');
const pageTitleElement = document.getElementById('page-title');
const pageDatasetTitle = document.body.dataset.pageTitle;
const pageSection = document.body.dataset.page;

if (pageTitleElement && pageDatasetTitle) {
  pageTitleElement.textContent = pageDatasetTitle;
}

if (pageSection) {
  tabLinks.forEach((link) => {
    link.classList.toggle('active', link.dataset.section === pageSection);
  });
}

const mockQuestions = [
  {
    id: 'q1',
    votes: 12,
    answers: 2,
    views: '34',
    answered: false,
    title: 'GraphQL – list projects which have at least one branch',
    excerpt:
      'Using GitHub GraphQL, I need to filter projects by branches. I can filter on default branch but need to ensure at least one branch exists.',
    tags: ['graphql', 'github', 'api'],
    user: 'Lenny',
    asked: '1 min ago',
    badge: 'Best practices',
  },
  {
    id: 'q2',
    votes: 0,
    answers: 0,
    views: '9',
    answered: false,
    title: 'How to connect to a Postgres accessible under a pathname via JDBC?',
    excerpt:
      'I have a Heroku database with a custom pathname. My connection string keeps timing out when the path includes /foo. Any ideas?',
    tags: ['postgresql', 'jdbc', 'heroku'],
    user: 'Kaiten Poodles',
    asked: '3 mins ago',
  },
  {
    id: 'q3',
    votes: 5,
    answers: 1,
    views: '17',
    answered: true,
    title: 'Terminal freezing when using flutter run',
    excerpt:
      'Flutter process works fine until hot reload when the terminal becomes frozen. Happens with zsh + oh-my-zsh, macOS Sonoma.',
    tags: ['flutter', 'dart', 'terminal'],
    user: 'Marek Tenere',
    asked: '4 mins ago',
  },
  {
    id: 'q4',
    votes: 1,
    answers: 0,
    views: '15',
    answered: false,
    title: 'How to cause a linker error when an externally-defined macro is inconsistent across translation units?',
    excerpt:
      'Need to guarantee all TUs agree on macro features. Looking for compile-time diagnostics that fail the build.',
    tags: ['c++', 'linker', 'macros'],
    user: 'phils',
    asked: '6 mins ago',
  },
  {
    id: 'q5',
    votes: 2,
    answers: 2,
    views: '19',
    answered: true,
    title: 'How should I pass user secrets from my frontend to my backend with Tauri?',
    excerpt:
      'Need guidance on storing secrets securely when using Rust backend with Tauri front-end messaging.',
    tags: ['tauri', 'security', 'rust'],
    user: 'darwin',
    asked: '8 mins ago',
  },
];

const formatTag = (tag) => `<span class="tag-pill">${tag}</span>`;

function buildStats(question) {
  const answerClass = question.answered ? 'stat answer' : 'stat';
  return `
    <div class="question-stats">
      <div class="stat">
        <strong>${question.votes}</strong>
        <span>votes</span>
      </div>
      <div class="${answerClass}">
        <strong>${question.answers}</strong>
        <span>answers</span>
      </div>
      <div class="stat">
        <strong>${question.views}</strong>
        <span>views</span>
      </div>
    </div>
  `;
}

function buildQuestionRow(question) {
  const injectedClass = question.injected ? ' injected-card' : '';
  const badge = question.badge
    ? `<span class="ml-2 rounded-full bg-orange-100 text-so-sunrise text-xs px-2 py-0.5">${question.badge}</span>`
    : '';

  return `
    <article class="question-row${injectedClass}" data-id="${question.id}">
      ${buildStats(question)}
      <div>
        <div class="flex items-center">
          <a href="#" class="question-title">${question.title}</a>
          ${badge}
        </div>
        <p class="text-sm text-so-muted mb-3">${question.excerpt}</p>
        <div class="question-meta">
          <div class="flex flex-wrap gap-2">
            ${question.tags.map(formatTag).join('')}
          </div>
          <span class="ml-auto text-xs text-so-muted">asked ${question.asked} by <strong>${question.user}</strong></span>
        </div>
      </div>
    </article>
  `;
}

function renderQuestions(list = mockQuestions) {
  const preservedInjection = Array.from(
    questionList.querySelectorAll('.injected-card')
  )
    .map((node) => node.outerHTML)
    .join('');

  const generated = list.map((question) => buildQuestionRow(question)).join('');
  questionList.innerHTML = preservedInjection + generated;
}

renderQuestions();

// Tab interactions (visual only for replica)
tabLinks.forEach((tab) => {
  tab.addEventListener('click', (event) => {
    event.preventDefault();
    tabLinks.forEach((link) => link.classList.remove('active'));
    tab.classList.add('active');
  });
});

// Expose injection hook for backend agents
window.SOReplica = {
  injectQuestion(payload) {
    const question = {
      id: payload.id || `q-${Date.now()}`,
      votes: payload.votes ?? 0,
      answers: payload.answers ?? 0,
      views: payload.views ?? '0',
      answered: payload.answered ?? false,
      title: payload.title || 'Untitled question',
      excerpt: payload.excerpt || payload.description || '',
      tags: payload.tags || ['stack-overflow'],
      user: payload.user || payload.author || 'anonymous',
      asked: payload.date || 'just now',
      badge: payload.badge,
      injected: true,
    };

    questionList.insertAdjacentHTML('afterbegin', buildQuestionRow(question));
    return question;
  },
};
