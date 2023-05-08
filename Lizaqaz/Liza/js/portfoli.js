function calculateSum (x, y) {
    let result = x+y;
    console.log(result);
    return result;
}

let answer = calculateSum(5,10);
console.log(answer);

const petr = {
    name: 'Petr',
    age: 36,
    speciality: 'html coder',
    city: 'Krakov',
    sayHi: function(name, age){
        console.log('Hi! My name is '+name+ ' I am from ' + city);
    },
};

console.log(petr);


console.log(petr.sayHi);