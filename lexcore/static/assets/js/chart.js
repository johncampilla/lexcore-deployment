console.log('hello for the new dashboard')

const dashboardbox = document.getElementById('dashboard-box')

$.ajax({
    type: 'GET',
    url:'chart-data',
    success: (resp) =>{
        const { msg }= resp
        console.log(msg)
        dashboardbox.innerHTML = `<b>${msg}</b>`
    },
    error: (err) => console.log(err)
})