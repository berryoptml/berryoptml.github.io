// Edit assets/data/news.json; both pages use the same entries, newest first.
(async () => {
  const containers = document.querySelectorAll('[data-news-limit]');
  if (!containers.length) return;
  try {
    const response = await fetch('assets/data/news.json', { cache: 'no-store' });
    if (!response.ok) throw new Error('News unavailable');
    const entries = await response.json();
    if (!Array.isArray(entries) || entries.some(entry => !['date', 'duration', 'lead', 'title', 'event', 'link', 'suffix'].every(key => typeof entry[key] === 'string'))) throw new Error('Invalid news entries');
    for (const container of containers) {
      const list = document.createElement('ul');
      list.className = 'news-list';
      const limit = container.dataset.newsLimit === 'all' ? entries.length : Number(container.dataset.newsLimit);
      for (const entry of entries.slice(0, limit)) {
        const row = document.createElement('li');
        const date = document.createElement('span');
        date.className = 'news-date';
        date.textContent = entry.date;
        const description = document.createElement('span');
        const title = document.createElement('strong');
        const duration = document.createElement('strong');
        duration.className = 'news-duration';
        const link = document.createElement('a');
        const url = new URL(entry.link, location.href);
        if (!['http:', 'https:'].includes(url.protocol)) throw new Error('Unsupported news link');
        title.textContent = entry.title;
        duration.textContent = entry.duration;
        link.href = entry.link;
        link.textContent = entry.event;
        description.append(duration, ' — ', entry.lead, title, ' at the ', link, entry.suffix);
        row.append(date, description);
        list.append(row);
      }
      container.replaceChildren(list);
    }
  } catch (error) {
    // Keep the readable HTML fallback if loading fails or JavaScript is disabled.
    console.warn('Showing saved news entries:', error.message);
  }
})();
