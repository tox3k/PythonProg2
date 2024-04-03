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

function saveOperation(){
    var date = document.getElementById("date").value;
    var money = document.getElementById("money").value;
    
    fetch('/add/'+date.toString()+'/'+money.toString());
}

function toggleButtonOperation(){
    var money = document.getElementById("money").value;
    var date = document.getElementById("date").value
    var bt = document.getElementById("submit_operation")

    if (money && date){
        bt.removeAttribute("disabled", "")
    }

    else{
        bt.setAttribute("disabled", "disabled")
    }
}

function calculateYear(){
    var year = document.getElementById("year_to_calculate").value.toString().slice(0, 4)
    window.open('/calculate/'+year, '_blank')
}

function calculateYearMonth(){
    element = document.getElementById("year_to_calculate").value.toString()
    var year = element.slice(0, 4)
    var month = element.slice(5, 7)
    if(month[0] == '0')
        month = month[1]
    window.open('/calculate/'+year+'/'+month, '_blank')
}