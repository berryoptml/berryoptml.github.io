// Mobile navigation toggle and greedy nav handler
document.addEventListener('DOMContentLoaded', function() {
  const toggleBtn = document.querySelector('.greedy-nav__toggle');
  const navList = document.querySelector('.greedy-nav .visible-links');
  
  if (toggleBtn && navList) {
    toggleBtn.addEventListener('click', function(e) {
      e.stopPropagation();
      navList.classList.toggle('nav-expanded');
      toggleBtn.classList.toggle('close');
    });
    
    document.addEventListener('click', function(e) {
      if (!e.target.closest('.greedy-nav')) {
        navList.classList.remove('nav-expanded');
        toggleBtn.classList.remove('close');
      }
    });
  }
});
