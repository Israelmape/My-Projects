const inputTD = document.getElementById("inputTD");
const myUl = document.getElementById("myUl");

function submit () {

     let task = inputTD.value.trim();

     const li = document.createElement("li");
     li.innerHTML = `<span id="tsk" style="color: red;">${task}</span>
                     <input  type="button" style="color: cream;"  value="done" id="done" ondblclick="undo()"  onclick="completed()">`;

     myUl.appendChild(li);
     

};

function undo () {
     const tsk = document.getElementById("tsk");
     tsk.style.color= "red";

     return
};


function completed () {
     const tsk = document.getElementById("tsk");
     tsk.style.color= "green";

     return
};
