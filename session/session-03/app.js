// 사용자의 선택 = event
// console.log('화이팅!');

// checkbox 라는 아이디를 가진 애를 가져와줘! 라는 뜻
// const checkbox = document.getElementById('checkbox');

// console.log 는 자바스크립트가 잘 먹혔는지 확인하는 것!
// console.log(checkbox);

const checkbox = document.querySelector('.checkbox');
console.log(checkbox);

checkbox.addEventListener('click',toggleClick);

// click이라는 이름의 함수 생성
// document = html , body = body, classlist = 
// function click(){
//     if(document.body.classList.contains('dark')){
//         document.body.classList.remove('dark');
//         console.log('convert into Light Mode');
//     } else {
//         document.body.classList.add('dark');
//         console.log('convert into Dark Mode');
//     }
// }

function toggleClick(){
    document.body.classList.toggle('dark');
    console.log('Working...!');
}

