let books = [];
let users = [];
let id_edit = "";

const getUsers = () => {
  users = [];
  fetch("http://127.0.0.1:5000/user")
    .then((resp) => {
      return resp.json();
    })
    .then((data) => {
      users = data.data;
      const parent = document.getElementById("list_user");
      users.forEach((e, index) => {
        const div = document.createElement("div");
        div.style = "display: flex; gap: 12px;";
        const text = document.createElement("span");
        const btnEdit = document.createElement("button");
        const btnDelete = document.createElement("button");
        btnEdit.textContent = "edit";
        btnDelete.textContent = "delete";
        btnEdit.onclick = () => {
          clickEdit({ id: e._id, name: e.name, email: e.email });
        };
        btnDelete.onclick = () => {
          deleteUser(e._id);
        };
        text.textContent = index + 1 + ". " + e.name + " (" + e.email + ")";
        div.append(text, btnEdit, btnDelete);
        parent.append(div);
      });
    })
    .catch((error) => {
      console.error("Error:", error);
    });
};

const addUser = () => {
  const form_name = document.getElementById("nama").value;
  const form_email = document.getElementById("email").value;
  if (form_name != "" && form_email != "") {
    fetch("http://127.0.0.1:5000/user", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        name: form_name,
        email: form_email,
      }),
    })
      .then((response) => response.json())
      .catch((error) => {
        console.error("Error:", error);
      });

    const parent = document.getElementById("list_user");
    setTimeout(() => {
      while (parent.hasChildNodes()) {
        parent.removeChild(parent.firstChild);
      }
      clickCancel();
      getUsers();
    }, 1000);
  }
};

const editUser = () => {
  const form_name = document.getElementById("nama").value;
  const form_email = document.getElementById("email").value;
  if (form_name != "" && form_email != "") {
    fetch(`http://127.0.0.1:5000/user?id=${id_edit}`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        name: form_name,
        email: form_email,
      }),
    })
      .then((response) => response.json())
      .catch((error) => {
        console.error("Error:", error);
      });

    const parent = document.getElementById("list_user");
    setTimeout(() => {
      while (parent.hasChildNodes()) {
        parent.removeChild(parent.firstChild);
      }
      clickCancel();
      getUsers();
    }, 1000);
  }
};

const deleteUser = (e) => {
  fetch(`http://127.0.0.1:5000/user?id=${e}`, {
    method: "DELETE",
  })
    .then((response) => response.json())
    .catch((error) => {
      console.error("Error:", error);
    });

  const parent = document.getElementById("list_user");
  setTimeout(() => {
    while (parent.hasChildNodes()) {
      parent.removeChild(parent.firstChild);
    }
    getUsers();
  }, 1000);
};

const clickEdit = (e) => {
  id_edit = e.id;
  document.getElementById("add-btn").style = "display: none;";
  document.getElementById("edit-btn").style = "display: block;";
  document.getElementById("cancel-btn").style = "display: block;";
  document.getElementById("nama").value = e.name;
  document.getElementById("email").value = e.email;
};

const clickCancel = () => {
  id_edit = "";
  document.getElementById("add-btn").style = "display: block;";
  document.getElementById("edit-btn").style = "display: none;";
  document.getElementById("cancel-btn").style = "display: none;";
  document.getElementById("nama").value = "";
  document.getElementById("email").value = "";
};

document.addEventListener("DOMContentLoaded", () => {
  getUsers();
});
