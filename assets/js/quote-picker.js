// Add or remove .quote blocks in index.html to curate the homepage quote list.
(() => {
  const picker = document.querySelector('[data-quote-picker]');
  if (!picker) return;

  const quotes = [...picker.querySelectorAll('.quote')];
  const dice = picker.querySelector('.quote-dice');
  if (!dice || quotes.length < 2) return;

  let activeIndex = quotes.findIndex((quote) => !quote.hidden);
  if (activeIndex < 0) activeIndex = 0;

  const show = (nextIndex) => {
    quotes.forEach((quote, index) => {
      const active = index === nextIndex;
      quote.hidden = !active;
      quote.inert = !active;
      quote.toggleAttribute('aria-hidden', !active);
    });
    activeIndex = nextIndex;
  };

  dice.addEventListener('click', () => {
    const offset = 1 + Math.floor(Math.random() * (quotes.length - 1));
    show((activeIndex + offset) % quotes.length);
  });
})();
