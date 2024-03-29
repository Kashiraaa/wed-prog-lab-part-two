function fillCourseList() {
    fetch('/lab8/api/courses/')
    .then (function (data){
        return data.json();
    })
    .then(function(courses) {
        let tbody =  document.getElementById('course-list');
        tbody.innerHTML = '';
        for(let i = 0; i<courses.lenght; i++) {
            tr = document.createElement('tr');

            let tdName = document.createElement('td');
            tdName.innerText = courses[i].name;

            let tdVideos = document.createElement('td');
            tdVideos.innerText = courses[i].videos;
            
            let tdPrice = document.createElement('td');
            tdPrice.innerText = courses[i].price ||',бесплатно';

            let editButton = document.createElement('button')
            editButton.innerText = 'Редактировать';
            editButton.onclick = function() {
                editCourse(i, courses[i]);
            };

            let delButton = document.createElement('button')
            delButton.innerText = 'Удалить';
            delButton.onclick = function(){
                deleteCourse(i);
            };

            let tdActions = document.createElement('td');
            tdActions.append(editButton);
            tdActions.append(delButton);

            tr.append(tdVideos);
            tr.append(tdName);
            tr.append(tdPrice);
            tr.append(tdActions);

            tbody.append(tr);
        }
    });
}

function deleteCourse(sum) {
    if(! confirm('Вы точно хотите удалить курс ?'))
        return;

    fetch('/lab8/api/courses/${sum}',{method: 'DELETE'})
    .then(function() {
        fillCourseList();
    });
}

function showModal() {
    document.querySelector('div.modal').style.display = 'block';
}
function hideModal() {
    document.querySelector('div.modal').style.display = 'none';
}

function cancel() {
    hideModal();
}

function addCourse() {
    document.getElementById('num').value = '';
    document.getElementById('name').value = '';
    document.getElementById('videos').value = '';
    document.getElementById('price').value = '';
    showModal();
}

function sendCourse(){
    const num = document.getElementById('num').value;
    const course = {
        name: document.getElementById('name').value,
        videos: document.getElementById('videos').value,
        price: document.getElementById('price').value,
    }

    const url = '/lab8/api/courses/${num}';
    const method = num ? "PUT": 'POST';
    fetch(url, {
        method: method,
        headres: {"Content - Type":  "application/json"},
        body: JSON.stringify(course)
    })
    .then (function() {
        fillCourseList();
        hideModal();
    })
}