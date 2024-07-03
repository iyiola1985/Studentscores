


const prompt =require('prompt-sync')();





let marks = Number(prompt('enter your marks'));

if( marks > 79 && marks <= 100){
    console.log('You Got A')
} else if (marks> 59 && marks<= 79){
    console.log('YOU GOT B')
} else if ( marks > 50 && marks <=59){
    le.log('YOU GOT C')

}else if(marks > 40 && marks >=50){
    console.log('YOU GOT D')

} else if(marks <=40 && marks>=0 ){
    console.log('YOU GOT E')
}
else {
    console.log('out of range');
    }



