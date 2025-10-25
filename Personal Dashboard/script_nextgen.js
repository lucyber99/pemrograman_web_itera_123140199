const taskItems = [];
const RENDER_EVENT = 'render-task';
const STORAGE_KEY = 'TASKLIST';
const SAVED_EVENT = 'saved-task';

// Generate ID unik
function generateId() {
  return +new Date();
}

// implementasi Literal default parameter
function greet(name = "Revo", greetings = "Hello") {
    const message = `${greetings}, ${name}!`;
    document.getElementById('greeting').innerText = message;
    return message;
  }
  

// Buat objek tugas <Old way>
// function generateTaskObject(id, task_name, subject, date_deadline, time_deadline, isCompleted) {
//   return {
//     id,
//     task_name,
//     subject,
//     date_deadline,
//     time_deadline,
//     isCompleted
//   };
// }

// Buat object menggunakan arrow function 
const generateTaskObject = (id, task_name, subject, date_deadline, time_deadline, isCompleted) => ({
    id,
    task_name,
    subject,
    date_deadline,
    time_deadline,
    isCompleted
  });
// Cari tugas berdasarkan ID <old way>
// function findTask(taskId) {
//   return taskItems.find(task => task.id === taskId) || null;
// }

// cari tugas berdasarkan ID dengan arrow function
const findTask = (taskId) => {
    return taskItems.find(task => task.id === taskId) || null;
}

// Cari index tugas <oldway>
// function findTaskIndex(taskId) {
    //   return taskItems.findIndex(task => task.id === taskId);
    
    
// Cari index tugas dengan arrow function
const findTaskIndex =(taskId) => {
  return taskItems.findIndex(task => task.id === taskId);
}

// Cek dukungan localStorage <oldway>
// function isStorageExist() {
//   if (typeof Storage === 'undefined') {
//     alert('Browser tidak mendukung localStorage');
//     return false;
//   }
//   return true;
// }

// Cek dukungan localStorage dengan arrow function
const isStorageExist = () => {
  if (typeof Storage === 'undefined') {
    alert('Browser tidak mendukung localStorage');
    return false;
  }
  return true;
}

// Simpan data ke localStorage
function saveData() {
  if (isStorageExist()) {
    const parsed = JSON.stringify(taskItems);
    localStorage.setItem(STORAGE_KEY, parsed);
    document.dispatchEvent(new Event(SAVED_EVENT));
  }
}

// Ambil data dari localStorage
function loadDataFromStorage() {
  const serializedData = localStorage.getItem(STORAGE_KEY);
  const data = JSON.parse(serializedData);

  if (data !== null) {
    for (const task of data) {
      taskItems.push(task);
    }
  }
  document.dispatchEvent(new Event(RENDER_EVENT));
}

// Tambah tugas baru
function addTask() {
  const id = generateId();
  const task_name = document.getElementById('task_name').value;
  const subject = document.getElementById('task_subject').value;
  const date_deadline = document.getElementById('task_date_deadline').value;
  const time_deadline = document.getElementById('task_time_deadline').value;

  const newTask = generateTaskObject(id, task_name, subject, date_deadline, time_deadline, false);
  taskItems.push(newTask);

  document.dispatchEvent(new Event(RENDER_EVENT));
  saveData();
}

// Render tampilan tugas
document.addEventListener(RENDER_EVENT, function () {
    //menggunakan destructure
    greet("Revo", "Halo");
  const uncompletedTaskList = document.getElementById('uncomplete_task_list');
  const completedTaskList = document.getElementById('completed_task_list');

  uncompletedTaskList.innerHTML = '';
  completedTaskList.innerHTML = '';

  for (const task of taskItems) {
    const taskElement = createTaskElement(task);
    if (task.isCompleted) {
      completedTaskList.append(taskElement);
    } else {
      uncompletedTaskList.append(taskElement);
    }
  }
});

// Buat elemen HTML untuk setiap tugas <oldway>
// function createTaskElement(task) {
//   const title = document.createElement('h2');
//   title.innerText = task.task_name;

//   const subject = document.createElement('p');
//   subject.innerText = `Matkul: ${task.subject}`;

//   const deadline = document.createElement('p');
//   deadline.innerText = `Deadline: ${task.date_deadline} ${task.time_deadline}`;

//   const container = document.createElement('div');
//   container.classList.add('task_item');
//   container.append(title, subject, deadline);

//   // tombol aksi
//   const buttonContainer = document.createElement('div');
//   buttonContainer.classList.add('button_group');

//   if (task.isCompleted) {
//     const undoButton = document.createElement('button');
//     undoButton.innerText = 'Belum Selesai';
//     undoButton.classList.add('styleBack');
//     undoButton.addEventListener('click', function () {
//       undoTaskFromCompleted(task.id);
//     });

//     const deleteButton = document.createElement('button');
//     deleteButton.innerText = 'Hapus';
//     deleteButton.classList.add('styleDelete');
//     deleteButton.addEventListener('click', function () {
//       removeTask(task.id);
//     });

//     buttonContainer.append(undoButton, deleteButton);
//   } else {
//     const completeButton = document.createElement('button');
//     completeButton.innerText = 'Selesai';
//     completeButton.classList.add('styleNext');
//     completeButton.addEventListener('click', function () {
//       addTaskToCompleted(task.id);
//     });

//     const deleteButton = document.createElement('button');
//     deleteButton.innerText = 'Hapus';
//     deleteButton.classList.add('styleDelete');
//     deleteButton.addEventListener('click', function () {
//       removeTask(task.id);
//     });

//     buttonContainer.append(completeButton, deleteButton);
//   }

//   container.append(buttonContainer);
//   return container;
// }

// manipulasi tugas selesai atau tidak menggunakan destructure
const createTaskElement = ({ id, task_name, subject, date_deadline, time_deadline, isCompleted }) => {
    const title = document.createElement('h2');
    title.innerText = task_name;
  
    const subjectEl = document.createElement('p');
    subjectEl.innerText = `Matkul: ${subject}`;
  
    const deadline = document.createElement('p');
    deadline.innerText = `Deadline: ${date_deadline} ${time_deadline}`;
  
    const container = document.createElement('div');
    container.classList.add('task_item');
    container.append(title, subjectEl, deadline);
  
    const buttonContainer = document.createElement('div');
    buttonContainer.classList.add('button_group');
  
    if (isCompleted) {
      const undoButton = document.createElement('button');
      undoButton.innerText = 'Belum Selesai';
      undoButton.classList.add('styleBack');
      undoButton.addEventListener('click', () => undoTaskFromCompleted(id));
  
      const deleteButton = document.createElement('button');
      deleteButton.innerText = 'Hapus';
      deleteButton.classList.add('styleDelete');
      deleteButton.addEventListener('click', () => removeTask(id));
  
      buttonContainer.append(undoButton, deleteButton);
    } else {
      const completeButton = document.createElement('button');
      completeButton.innerText = 'Selesai';
      completeButton.classList.add('styleNext');
      completeButton.addEventListener('click', () => addTaskToCompleted(id));
  
      const deleteButton = document.createElement('button');
      deleteButton.innerText = 'Hapus';
      deleteButton.classList.add('styleDelete');
      deleteButton.addEventListener('click', () => removeTask(id));
  
      buttonContainer.append(completeButton, deleteButton);
    }
  
    container.append(buttonContainer);
    return container;
  };
  

// Pindahkan ke daftar selesai
function addTaskToCompleted(taskId) {
  const task = findTask(taskId);
  if (task == null) return;
  task.isCompleted = true;
  document.dispatchEvent(new Event(RENDER_EVENT));
  saveData();
}

// Kembalikan ke daftar belum selesai
function undoTaskFromCompleted(taskId) {
  const task = findTask(taskId);
  if (task == null) return;
  task.isCompleted = false;
  document.dispatchEvent(new Event(RENDER_EVENT));
  saveData();
}

function showDay() {
  const dateInput = document.getElementById("task_date").value;
  if (!dateInput) return;
  
  const days = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"];
  const dayIndex = new Date(dateInput).getDay();
  
  document.getElementById("day_result").innerText = `Hari: ${days[dayIndex]}`;
}

// Hapus satu tugas
function removeTask(taskId) {
  const taskIndex = findTaskIndex(taskId);
  if (taskIndex === -1) return;

  const confirmDelete = confirm('Yakin ingin menghapus tugas ini?');
  if (confirmDelete) {
    taskItems.splice(taskIndex, 1);
    document.dispatchEvent(new Event(RENDER_EVENT));
    saveData();
  }
}

// Saat DOM siap
document.addEventListener('DOMContentLoaded', function () {
  const submitForm = document.getElementById('inputTask');
  submitForm.addEventListener('submit', function (event) {
    event.preventDefault();
    addTask();
    submitForm.reset();
  });

  if (isStorageExist()) {
    loadDataFromStorage();
  }
});

// Event penyimpanan
document.addEventListener(SAVED_EVENT, function () {
  console.log('Data tersimpan ke localStorage:', localStorage.getItem(STORAGE_KEY));
});
