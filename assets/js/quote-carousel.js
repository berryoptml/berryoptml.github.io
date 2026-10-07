(() => {
  const carousel = document.querySelector('[data-quote-carousel]');
  if (!carousel || window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

  const slides = [...carousel.querySelectorAll('.quote')];
  const dots = [...carousel.querySelectorAll('.quote-dots button')];
  if (slides.length < 2) return;

  let activeIndex = 0;
  let timer;

  const show = (nextIndex) => {
    slides[activeIndex].classList.remove('is-active');
    slides[activeIndex].setAttribute('aria-hidden', 'true');
    slides[activeIndex].inert = true;
    activeIndex = nextIndex;
    slides[activeIndex].classList.add('is-active');
    slides[activeIndex].removeAttribute('aria-hidden');
    slides[activeIndex].inert = false;
    dots.forEach((dot, index) => {
      const active = index === activeIndex;
      dot.classList.toggle('is-active', active);
      dot.setAttribute('aria-pressed', String(active));
    });
  };

  const start = () => {
    window.clearInterval(timer);
    timer = window.setInterval(() => show((activeIndex + 1) % slides.length), 7000);
  };
  const stop = () => window.clearInterval(timer);

  carousel.addEventListener('mouseenter', stop);
  carousel.addEventListener('mouseleave', start);
  carousel.addEventListener('focusin', stop);
  carousel.addEventListener('focusout', start);
  dots.forEach((dot, index) => dot.addEventListener('click', () => {
    if (index !== activeIndex) show(index);
    start();
  }));
  start();
})();
