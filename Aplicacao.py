# Aplicacao.py
from ProjBra import *
import Back

app = None
selected = None

def view_command():
    rows = Back.view()  # Alterado
    app.listClientes.delete(0, END)
    for r in rows:
        app.listClientes.insert(END, r)

def search_command():
    app.listClientes.delete(0, END)
    rows = Back.search(app.txtNome.get(), app.txtSobrenome.get(), app.txtEmail.get(), app.txtCPF.get())  # Alterado
    for r in rows:
        app.listClientes.insert(END, r)

def insert_command():
    Back.insert(app.txtNome.get(), app.txtSobrenome.get(), app.txtEmail.get(), app.txtCPF.get())  # Alterado
    view_command()

def update_command():
    global selected
    if selected:
        Back.update(selected[0], app.txtNome.get(), app.txtSobrenome.get(), app.txtEmail.get(), app.txtCPF.get())  # Alterado
        view_command()
    else:
        print("Selecione um cliente para atualizar.")

def del_command():
    global selected
    selected_row = app.listClientes.curselection()
    if selected_row:
        index = selected_row[0]
        selected = app.listClientes.get(index)
        id = selected[0]
        Back.delete(id)  # Alterado
        view_command()
    else:
        print("Selecione um cliente para excluir.")

def getSelectRow(event):
    global selected
    if event.widget.curselection():
        index = event.widget.curselection()[0]
        selected = app.listClientes.get(index)
        app.entNome.delete(0, END)
        app.entNome.insert(END, selected[1])
        app.entSobrenome.delete(0, END)
        app.entSobrenome.insert(END, selected[2])
        app.entEmail.delete(0, END)
        app.entEmail.insert(END, selected[3])
        app.entCPF.delete(0, END)
        app.entCPF.insert(END, selected[4])

if __name__ == "__main__":
    app = Gui()
    app.listClientes.bind('<<ListboxSelect>>', getSelectRow)
    app.btnViewAll.config(command=view_command)
    app.btnBuscas.config(command=search_command)
    app.btnInserir.config(command=insert_command)
    app.btnUpdate.config(command=update_command)
    app.btnDel.config(command=del_command)
    app.btnClose.configure(command=app.window.destroy)
    app.run()
