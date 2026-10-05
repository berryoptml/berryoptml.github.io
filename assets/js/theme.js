(() => {
  const storageKey = 'anand-kumar-theme';
  const root = document.documentElement;
  const deviceTheme = window.matchMedia('(prefers-color-scheme: dark)');
  const preferred = deviceTheme.matches ? 'dark' : 'light';
  let savedTheme = (() => {
    try {
      return localStorage.getItem(storageKey);
    } catch {
      return null;
    }
  })();
  const initial = savedTheme || preferred;
  root.dataset.theme = initial;

  deviceTheme.addEventListener('change', (event) => {
    if (!savedTheme) root.dataset.theme = event.matches ? 'dark' : 'light';
  });

  const icon = (theme) => theme === 'dark'
    ? '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41M2 12h2M20 12h2M4.93 19.07l1.41-1.41M17.66 6.34l1.41-1.41"/></svg>'
    : '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20.6 15.8A8.5 8.5 0 0 1 8.2 3.4 8.5 8.5 0 1 0 20.6 15.8Z"/></svg>';

  const render = (button) => {
    const dark = root.dataset.theme === 'dark';
    button.innerHTML = icon(dark);
    button.setAttribute('aria-label', dark ? 'Switch to light mode' : 'Switch to dark mode');
    button.title = dark ? 'Light mode' : 'Dark mode';
  };

  document.addEventListener('DOMContentLoaded', () => {
    const header = document.querySelector('.site-header');
    if (!header) return;
    const button = document.createElement('button');
    button.className = 'theme-toggle';
    button.type = 'button';
    button.setAttribute('aria-pressed', String(root.dataset.theme === 'dark'));
    render(button);
    button.addEventListener('click', () => {
      const next = root.dataset.theme === 'dark' ? 'light' : 'dark';
      root.dataset.theme = next;
      savedTheme = next;
      try {
        localStorage.setItem(storageKey, next);
      } catch {
        // The selected theme still applies for this visit when storage is unavailable.
      }
      button.setAttribute('aria-pressed', String(next === 'dark'));
      render(button);
    });
    header.append(button);
  });
})();
