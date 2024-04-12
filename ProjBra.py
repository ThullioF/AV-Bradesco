""""Módulo para desenvolver interface gráfica"""
from tkinter import *

class Gui():
    """"Classe da interface gráfica"""
    x_pad = 5            #propriedade padding que estabelece o distanciamento entre o conteúdo de um elemento e a sua borda
    y_pad = 3            #propriedade padding que estabelece o distanciamento entre o conteúdo de um elemento e a sua borda
    width_entry = 30     #irá definir a largura da janela

    #para criar uma janela
    window = Tk()
    window.wm_title("PYSQL")

    #definição das variáveis que recebem os dados inseridos pelo user
    txtNome = StringVar()
    txtSobrenome = StringVar()
    txtEmail = StringVar()
    txtCPF = StringVar()

    #criando os objetos que farão parte das janelas
    lblNome = Label(window, text = "Nome")
    lblSobrenome = Label(window, text = "Sobrenome")
    lblEmail = Label(window, text = "Email")
    lblCPF = Label(window, text = "CPF")
    entNome = Entry(window, textvariable = txtNome, width=width_entry)
    entSobrenome = Entry(window, textvariable = txtSobrenome, width=width_entry)
    entEmail = Entry(window, textvariable = txtEmail, width=width_entry)
    entCPF = Entry(window, textvariable = txtCPF, width=width_entry)
    listClientes = Listbox(window, width=100)
    scrollClientes = Scrollbar(window)
    btnViewAll = Button(window, text="Ver todos")
    btnBuscas = Button(window, text="Buscar")
    btnInserir = Button(window, text="Inserir")
    btnUpdate = Button(window, text="Atualizar selecionados")
    btnDel = Button(window, text="Deletar selecionados")
    btnClose = Button(window, text="Fechar")

    #associar os objetos criados ao Grid da Janela
    lblNome.grid(row=0, column=0)
    lblSobrenome.grid(row=1, column=0)
    lblEmail.grid(row=2, column=0)
    lblCPF.grid(row=3, column=0)
    entNome.grid(row=0, column=1, padx=50, pady=50)
    entSobrenome.grid(row=1, column=1)
    entEmail.grid(row=2, column=1)
    entCPF.grid(row=3, column=1)
    listClientes.grid(row=0, column=2, rowspan=10)
    scrollClientes.grid(row=0, column=6, rowspan=10)
    btnViewAll.grid(row=4, column=0, columspan=2)
    btnBuscas.grid(row=5, column=0, columnspan=2)
    btnInserir.grid(row=6, column=0, columnspan=2)
    btnUpdate.grid(row=7, column=0, columnspan=2)
    btnDel.grid(row=8, column=0, columnspan=2)
    btnClose.grid(row=9, column=0, columnspan=2)

    #união do Scrollbar com a Listbox
    listClientes.configure(yscrollcommand=scrollClientes.set)
    scrollClientes.configure(command=listClientes.yview)

    #adicionar SWAG (aparência) à interface
    for child in window.winfo_children():
        widget_class = child.__class__.__name__
        if widget_class == "Button":
            child.grid_configure(sticky='WE', padx=x_pad, pady=y_pad)
        elif widget_class == "Listbox":
            child.grid_configure(padx=0, pady=0, sticky='NS')
        elif widget_class == "Scrollbar":
            child.grid_configure(padx=0, pady=0, sticky='NS')
        else:
            child.grid_configure(padx=x_pad, pady=y_pad, sticky='N')
    def run(self):
        Gui.window.mainloop()