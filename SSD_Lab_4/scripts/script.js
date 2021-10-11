para = document.getElementById("para");
function insert(){
  var x = document.getElementById("inp").value;
  para.innerHTML = x;
}

i=0;
function add(){
  var item = document.createElement("li");
  i = para.innerHTML;
  var x = String(i);
  x = x+" ";
  date =  new Date();
  date = date.toTimeString();
  res = x.concat(date);
  item.textContent = res;
//   item.id="id"+i;
//   i=i+1;
  document.getElementById("list").appendChild(item);
  item.addEventListener(onmouseover, highlight,true);
}

function remove(){
  var list = document.getElementById('list');
  if (list.lastChild) {
     list.removeChild(list.lastChild);
  }
}

function highlight() {
  y=document.getElementsByTagName("li");
  y.style.color = "blue";
  // listItem = document.getElementById("lis");
  console.log(y);
  // listItem[0].style.color = "red";
}
flag=true;
s = 'Times New Roman';
function changeFont(){
  var items = document.getElementsByTagName("li");
 
  if(flag){
      for (let i = 0; i < items.length; i++) {
        items[i].style.fontFamily = "sans-serif";
      }
    flag = false;
  } else if (!flag) {
    for (let i = 0; i < items.length; i++) {
      items[i].style.fontFamily = s;
    }
    flag=true;
  }
}
