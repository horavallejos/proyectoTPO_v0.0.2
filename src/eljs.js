document.addEventListener('DOMContentLoaded', function () {
    fetchData();

    var form = document.getElementById('crud-form');
    form.addEventListener('submit', function (e) {
        e.preventDefault();
        saveData();
    });
});

function fetchData() {
    fetch('http://127.0.0.1:5000/api/data')
        .then(response => response.json())
        .then(data => {
            var tableBody = document.querySelector('#data-table tbody');
            tableBody.innerHTML = '';

            data.forEach(function (row) {
                var newRow = document.createElement('tr');
                newRow.innerHTML = `
                    <td>${row.id}</td>
                    <td>${row.name}</td>
                    <td>${row.email}</td>
                    <td class="actions">
                        <button onclick="editData(${row.id})">Editar</button>
                        <button onclick="deleteData(${row.id})">Eliminar</button>
                    </td>
                `;

                tableBody.appendChild(newRow);
            });
        });
}

function saveData() {
    var form = document.getElementById('crud-form');
    var id = form.querySelector('#id').value;
    var name = form.querySelector('#name').value;
    var email = form.querySelector('#email').value;

    var data = {
        id: id,
        name: name,
        email: email
    };

    var url = 'http://127.0.0.1:5000/api/data';
    var method = 'POST';

    if (id) {
        url += `/${id}`;
        method = 'PUT';
    }

    fetch(url, {
        method: method,
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
        .then(response => response.json())
        .then(data => {
            form.reset();
            fetchData();
        });
}

function editData(id) {
    fetch(`http://127.0.0.1:5000/api/data/${id}`)
        .then(response => response.json())
        .then(data => {
            var form = document.getElementById('crud-form');
            form.querySelector('#id').value = data.id;
            form.querySelector('#name').value = data.name;
            form.querySelector('#email').value = data.email;
        });
}

function deleteData(id) {
    if (confirm('¿Estás seguro de que quieres eliminar este registro?')) {
        fetch(`http://127.0.0.1:5000/api/data/${id}`, {
            method: 'DELETE'
        })
            .then(response => response.json())
            .then(data => {
                fetchData();
            });
    }
}
