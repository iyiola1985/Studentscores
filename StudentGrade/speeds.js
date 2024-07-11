const prompt =require('prompt-sync')();

const  limit = 70;
let speed = Number(prompt('enter your vechile speed'))
function vehicle_speed(speed){
//     if (isNaN(speed )|| speed <= 0){
//         console.log('invalid');
// } 

let demerit_point = (speed - limit)/5;
if (speed <= 70){
    console.log('OK')
}else if (speed > 70) {
    console.log(`your point: ${demerit_point}`);
}if(demerit_point > 12){
        console.log('licence suspended')

 //} else {
       // console.log('Invalid')
    }
    }
    


vehicle_speed(speed)