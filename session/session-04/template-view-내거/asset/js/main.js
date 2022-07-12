import { fetchGET, fetchPOST } from "./dataFetching.js";

const SERVER_HOST =
  "https://asia-northeast3-likelion-js-practice.cloudfunctions.net/api";

const NAME = "김민규";

async function getProfileData(name) {
  const path = "/member";

  const res = await fetchGET(SERVER_HOST,path,{ name : name });  //host : 서버 주소 , path : endpoint 

  const myName = res.data.profile.name;
  const myMbti = res.data.profile.mbti;
  const myGithub = res.data.profile.github;

  document.querySelector('.NAME').innerHTML = myName;
  document.querySelector('.MBTI').innerHTML = myMbti;
  document.querySelector('.GITHUB').innerHTML = myGithub;
}

async function getFootprint(name) {
  const path = "/footprint";

  const res = await fetchGET(SERVER_HOST,path,{ name : name });  //host : 서버 주소 , path : endpoint 

  const messages = res.data.messages;

  for(let i = 0; i< messages.length; i++){
  const messageFormat = `
  <div class="board-row">
  ${messages[i]} 
  </div>`

  document.querySelector(".board").innerHTML += messageFormat;
  }
  document.querySelector('.NAME').innerHTML = myName;
  document.querySelector('.MBTI').innerHTML = myMbti;
  document.querySelector('.GITHUB').innerHTML = myGithub;
}

async function sendFootprint() {
  const path = '/footprint';
  
  const messageObj = {
    content : document.querySelector(".message-content").value,
    receiverName: document.querySelector(".message-sender").value,
  }; //request body의 역할을 할 거임

  const res = await fetchPOST(SERVER_HOST, path, messageObj); // 에러에 대비해서 res변수에 대입
  if (res.status === 200){
    alert("메세지를 성공적으로 전송하였습니다!");
  }
}

window.onload = function () // 웹페이지가 렌더링이 된 다음에 수행할 코드들 ... window.onload
{

  const sendButton = document.querySelector(".send-btn");
  sendButton.addEventListener("click", () => {
    sendFootprint();
  });
  getProfileData(NAME);
  getFootprint(NAME);
  // document.querySelector('.NAME').innerHTML = "NAME : 킹민규";
  // document.querySelector('.NAME').style.color = 'brown';

  // document.querySelector('.MAJOR').innerHTML = "MAJOR : 컴공과";
  // document.querySelector('.IG').innerHTML = "IG : IMTHEKING";  


};
