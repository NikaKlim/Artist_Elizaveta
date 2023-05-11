// JavaScript
const biography = document.getElementById('biography');


function addActiveClass() {
  const elementTop = biography.getBoundingClientRect().top;
  const elementBottom = biography.getBoundingClientRect().bottom;
  const windowHeight = window.innerHeight;

  if (elementTop < windowHeight && elementBottom >= 0) {
    biography.classList.add('slide-in-2');
  } else {
    biography.classList.remove('slide-in-2');
  }
}

window.addEventListener('scroll', addActiveClass);

