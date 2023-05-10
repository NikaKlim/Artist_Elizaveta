const elem = document.querySelectorAll('.portfolio');
let currentClassIndex = 1;

for(let i = 0; i < elem.length; i++){
  elem[i].onclick = funcShow;
}

function funcShow(){
  // Удаляем все классы work-examples-N
  for(let i = 1; i <= 5; i++) {
    this.classList.remove(`work-examples-${i}`);
  }

  // Добавляем следующий класс work-examples-N
  this.classList.add(`work-examples-${currentClassIndex}`);

  // Увеличиваем currentClassIndex на 1
  currentClassIndex++;

  // Если currentClassIndex превышает 5, то сбрасываем его на 1
  if (currentClassIndex > 4) {
    currentClassIndex = 1;
  }
}