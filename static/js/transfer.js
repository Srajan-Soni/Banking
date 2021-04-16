
const users = document.getElementById('users')
var money = document.getElementById('money')
const form = document.forms
const confirm = document.querySelector('.confirm')

// alert(form[0])


form[0].addEventListener('submit',(e)=>{
    // alert('Money'+money.value)
    e.preventDefault()
    u = verifyUser()
    p = verifyPay()
    confirm.onclick = ()=>{
    if(u && p){
        // alert('Sending........')
        form[0].submit()
    }else{
        e.preventDefault()
    }
}


})

const verifyUser = ()=>{
    if(users.value == 0){
        alert('Select User ')
        return false
    }
    else{
        return true
    }
}

const verifyPay = ()=>{
    if(money.value == null){
        alert('Enter Amount')
        return false
    }
    else if(money.value < 0){
        alert('Enter valid amount')
        return false
    }
    // else if(money.value != NaN){
    //     alert('Enter correct format')
    //     return false
    // }    
    else{
        // alert('correct')
        return true
    }
}