const prompt =require('prompt-sync')();git

const  limit = 70;
let vechile_speed = Number(prompt('enter your vechile speed'))
function speed(speed){
    if (isNaN(speed )|| speed <= 0){
        console.log('invalid');
} else {
    let demerit_point = (speed - limit)/5;
    if(demerit_point > 12){
        console.log('licence suspended')

 } else{
        console.log('your point: ${demerit_point}');
    }
    }
    }
speed(speed)