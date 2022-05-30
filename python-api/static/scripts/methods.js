URL_RESPONSE_SEND = "http://localhost:8000"

function sendDelete(id) {
    fetch(`http://127.0.0.1:8000/delete/${id}`, {
        method: "DELETE",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(id)
    }).then((response) => {
        if (response.ok) {
            window.alert("Deleted with success")
            window.location.reload()
        }
    })
}

function sendPost(user) {
    fetch("http://127.0.0.1:8000/register", {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(user)
    }).then((response) => {
        if (response.ok) {
            window.alert("Insert success")
            window.location.href = URL_RESPONSE_SEND
        }
    })
}

function sendUpdate(user, id) {
    fetch(`http://127.0.0.1:8000/update/${id}`, {
        method: "PUT",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(user)
    }).then((response) => {
        if (response.ok) {
            window.alert("Update success")
            window.location.href = URL_RESPONSE_SEND
        }
    })
}