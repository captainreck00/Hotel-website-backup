document.addEventListener("DOMContentLoaded", function () {
    tableData=JSON.parse(JSON.stringify(custData))
    TableEntry("current")

    const selectButtons = document.querySelectorAll(".booking_btn");
    let selectedRoom = null;

    selectButtons.forEach(function (button) {
        button.addEventListener("click", handleSelectButtonClick);
    });
    
    const pay_btn = document.getElementById('payDisplay_btn')
    const selectButton = document.getElementsByClassName('selected-button')
    pay_btn.addEventListener('click',function (){
        if (selectButton.length > 0){
            document.getElementById('payement').classList.remove('hide-pay')
            selected_cust = document.getElementsByClassName("selected-button")
            const cust_id = selected_cust[0].getAttribute('id-select');
            if (selected_cust){
                pay_Data=payData[cust_id]

                document.getElementById('roomCharges').innerHTML ='₹' + pay_Data['roomCharges']
                document.getElementById('roomService').innerHTML ='₹' + pay_Data['roomService']
                document.getElementById('service').innerHTML ='₹' + pay_Data['service']
                document.getElementById('vat').innerHTML ='₹' + pay_Data['vat']
                document.getElementById('prefCharges').innerHTML ='₹' + pay_Data['preference']
                document.getElementById('gym').innerHTML ='₹' + pay_Data['gym']
                document.getElementById('bar').innerHTML ='₹' + pay_Data['bar']
                document.getElementById('bed').innerHTML = '₹' +pay_Data['bed']
                document.getElementById('breakfast').innerHTML = '₹' + pay_Data['breakfast']
                document.getElementById('discount').innerHTML = '₹' + pay_Data['discount']
                document.getElementById('total').innerHTML = '₹' + pay_Data['total']
        }}
        else{
            alert('Please Select a customer first')
        }

    })

    const paid_btn=document.getElementById('paid')
    paid_btn.addEventListener('click', function(){

        selected_cust = document.getElementsByClassName("selected-button")
        const cust_id = selected_cust[0].getAttribute('id-select');
        const idJSON = {'id':cust_id};

        const requestOptions = {
            method: "POST",
            headers: {
            'Content-Type': 'application/json'
            },
            body: JSON.stringify(idJSON)
        };
        
        const serverURL = "http://127.0.0.1:5000/customer_info";
        
        fetch(serverURL, requestOptions)
        .then(response => {
            if (response.status !== 200) {
            throw new Error(`Login failed. Status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            // Add the message when successfully paid
            window.location.reload()
        })
        .catch(error => {
            console.error('Error:', error.message);
        });
    })
});



function showTable(tableId) {
    document.getElementById('currentTable').classList.add('hidden-table');
    document.getElementById('pastTable').classList.add('hidden-table');
    document.getElementById('advanceTable').classList.add('hidden-table');

    document.getElementById(tableId + 'Table').classList.remove('hidden-table');
    TableEntry(tableId)

    if(tableId != 'current'){
        document.getElementById('payDisplay_btn').classList.add('hide-pay');
        document.getElementById('payement').classList.add('hide-pay');
    }
    if (tableId =='current'){
        attachButtonListeners()
        document.getElementById('payDisplay_btn').classList.remove('hide-pay');
        document.getElementById('payement').classList.add('hide-pay');
    }
}

function TableEntry(TableId) {
    var tableBody = document.querySelector("#"+TableId+"Table table tbody");
    tableBody.innerHTML = "";

    if (TableId=="current"){
        if (tableData[0].length>0){
            (tableData[0]).forEach(function (booking) {
                var row = document.createElement("tr");
                row.innerHTML = `
                <td><button class="booking_btn" \id-select=${booking.id}></button></td>
                <td>${booking.id}</td>
                <td>${booking.name}</td>
                <td>${booking.phone_no}</td>
                <td>${booking.email_id}</td>
                <td>${booking.guests}</td>
                <td>${booking.room_no}</td>
                <td>${booking.room_type}</td>
                <td>${booking.preference}</td>
                <td>${(Boolean(booking.addons[0])).toString().charAt(0).toUpperCase()+(Boolean(booking.addons[0])).toString().slice(1)}</td>
                <td>${(Boolean(booking.addons[1])).toString().charAt(0).toUpperCase()+(Boolean(booking.addons[0])).toString().slice(1)}</td>
                <td>${(Boolean(booking.addons[2])).toString().charAt(0).toUpperCase()+(Boolean(booking.addons[0])).toString().slice(1)}</td>
                <td>${(Boolean(booking.addons[3])).toString().charAt(0).toUpperCase()+(Boolean(booking.addons[0])).toString().slice(1)}</td>
                <td>${booking.check_in}</td>
                <td>${booking.check_out}</td>`;
                tableBody.appendChild(row);
                }
            )
            document.getElementById("container").classList.remove("hide")
        }
        else{
            document.getElementById("container").classList.add("hide")
            var mess=document.getElementById("message");
            mess.classList.remove("hide-pay");
            mess.innerHTML="No Current Bookings found"
        }    
    }
        
    else if (TableId=="advance"){
        if (tableData[1].length>0){
            (tableData[1]).forEach(function (booking) {
           
                var row = document.createElement("tr");
                row.innerHTML = `
                <td>${booking.id}</td>
                <td>${booking.name}</td>
                <td>${booking.phone_no}</td>
                <td>${booking.email_id}</td>
                <td>${booking.guests}</td>
                <td>${booking.room_no}</td>
                <td>${booking.room_type}</td>
                <td>${booking.preference}</td>
                <td>${Boolean(booking.addons[0])}</td>
                <td>${Boolean(booking.addons[1])}</td>
                <td>${Boolean(booking.addons[2])}</td>
                <td>${Boolean(booking.addons[3])}</td>
                <td>${booking.check_in}</td>`;
                tableBody.appendChild(row);
                }
            )
            document.getElementById("container").classList.remove("hide")
        }
        else{
            var mess=document.getElementById("message");
            mess.classList.remove("hide-pay");
            mess.innerHTML="No Advanced Bookings found"
            document.getElementById("container").classList.add("hide")
        }
        }
    else if (TableId=="past"){
        if (tableData[2].length>0){
        (tableData[2]).forEach(function (booking) {
          
            var row = document.createElement("tr");
            row.innerHTML = `
            <td>${booking.id}</td>
            <td>${booking.name}</td>
            <td>${booking.phone_no}</td>
            <td>${booking.email_id}</td>
            <td>${booking.guests}</td>
            <td>${booking.room_no}</td>
            <td>${booking.room_type}</td>
            <td>${booking.preference}</td>
            <td>${Boolean(booking.addons[0])}</td>
            <td>${Boolean(booking.addons[1])}</td>
            <td>${Boolean(booking.addons[2])}</td>
            <td>${Boolean(booking.addons[3])}</td>
            <td>${booking.check_in}</td>
            <td>${booking.check_out}</td>
            <td>${booking.amount}</td>`;
            tableBody.appendChild(row);
            }
        )
        document.getElementById("container").classList.remove("hide")
    }
        else{
            var mess=document.getElementById("message")
            mess.classList.remove("hide");
            mess.innerHTML="No Past Bookings found"
            document.getElementById("container").classList.add("hide")
        }
    }
    
    
}

function handleSelectButtonClick() {
    const roomType = this.getAttribute("room-select");
    const isAlreadySelected = this.classList.contains("selected-button");
    if (isAlreadySelected) {
        this.classList.remove("selected-button");
        selectedRoom = null;
    } else {
        const previouslySelectedButton = document.querySelector(".booking_btn.selected-button");
        if (previouslySelectedButton) {
            previouslySelectedButton.classList.remove("selected-button");
        }
        this.classList.add("selected-button");
        selectedRoom = roomType;
    }
}
function attachButtonListeners() {
    const selectButtons = document.querySelectorAll(".booking_btn");
    let selectedRoom = null;

    selectButtons.forEach(function (button) {
        button.addEventListener("click", handleSelectButtonClick);
    });
}

function display_pay() {
    document.getElementById('payDisplay_btn').style.display=none
}