function open_greeting(){
    var inputEl = document.getElementById('name');
    var name = inputEl.value;

    var bt = document.getElementById('name_submit');

    window.open('hello-world/'+name, '_blank');
}

function toggleButton(){
    var bt = document.getElementById('name_submit');
    var inputEl = document.getElementById('name');
    var name = inputEl.value;
    bt.setAttribute("disabled", "disabled");
    
    if (name.length > 0){
        bt.removeAttribute("disabled")
    }

    else{
        bt.setAttribute("disabled", "disabled")
    }
}