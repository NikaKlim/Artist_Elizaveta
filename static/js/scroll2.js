// JavaScript
const portfolio = document.getElementById('portfolio');


function addActiveClass() {
  const elementTop = portfolio.getBoundingClientRect().top;
  const elementBottom = portfolio.getBoundingClientRect().bottom;
  const windowHeight = window.innerHeight;

  if (elementTop < windowHeight && elementBottom >= 0) {
    portfolio.classList.add('slide-in-2');
  } else {
    portfolio.classList.remove('slide-in-2');
  }
}

window.addEventListener('scroll', addActiveClass);