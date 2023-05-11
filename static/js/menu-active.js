// получаем все ссылки из списка
const navLinks = document.querySelectorAll('.nav-link');

// проверяем localStorage на наличие сохраненного значения
const activeLink = localStorage.getItem('activeLink');

// если значение найдено, устанавливаем класс "active" для соответствующей ссылки
if (activeLink) {
  navLinks.forEach(link => {
    if (link.getAttribute('href') === activeLink) {
      link.classList.add('active');
    }
  });
}

// добавляем обработчик события клика для каждой ссылки
navLinks.forEach(link => {
  link.addEventListener('click', e => {
    // удаляем класс "active" для всех ссылок
    navLinks.forEach(link => link.classList.remove('active'));

    // устанавливаем класс "active" для нажатой ссылки
    e.target.classList.add('active');

    // сохраняем значение нажатой ссылки в localStorage
    localStorage.setItem('activeLink', e.target.getAttribute('href'));
  });
});