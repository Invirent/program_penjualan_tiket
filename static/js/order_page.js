function hide_return(flight_type){
    var return_date = document.getElementById('return_date_form')
    if (flight_type == 'one_way'){
        return_date.style.display = 'none'
        document.getElementById('date-8f51').setAttribute('type','hidden')
    }
    else{
        return_date.style.display = 'block'
        document.getElementById('date-8f51').setAttribute('type','date')
        document.getElementById('date-8f51').setAttribute('required',true)
    }
}

