# pemrograman_web_itera_123140199
#**Pertemuan 2 (Impelementasi JS Next Gen**
berikut adalah tampilan dari dashboard pengaturan tugas (todo list tugas)
<img width="964" height="976" alt="image" src="https://github.com/user-attachments/assets/a9f0e68e-cbd7-4a2b-9fc0-9786f2ec7b44" />
fitur utamanya adalah dapat melakukan input, edit, dan hapus pada data tugas
<img width="665" height="932" alt="image" src="https://github.com/user-attachments/assets/6c57e86b-2d9d-4c73-a282-e9b867bc5b90" />

# Implementasi arrow function:
const findTask = (taskId) => {
    return taskItems.find(task => task.id === taskId) || null;
}

# Implementasi Literal default parameter:
function greet(name = "Revo", greetings = "Hello") {
    const message = `${greetings}, ${name}!`;
    document.getElementById('greeting').innerText = message;
    return message;
  }

# Implementasi Async & Promise: (pengaturan error jika localStorage tidak terdefinisi)
  const isStorageExist = async () => {
  return new Promise((resolve) => {
    if (typeof Storage === 'undefined') {
      alert('Browser tidak mendukung localStorage');
      resolve(false);
    } else {
      resolve(true);
    }
  });
};

pertemuan 1 (membuat aplikasi manajemen tugas sederhana)
