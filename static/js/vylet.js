// получаем элемент блока
const bioElement = document.querySelector('p');

const h1 = document.querySelector('h1');
const h2 = document.querySelector('h2');


// добавляем CSS класс при загрузке страницы
window.onload = function() {
  bioElement.classList.add('slide-in');

  h1.classList.add('slide-in-2');
  h2.classList.add('slide-in-2');


};

