from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton


def alerta(text='erro', condicao=1):
    dialog = MDDialog(title='Erro',
                      text=f'{text}',
                      buttons=[MDFlatButton(text='Ok',
                                            on_release=liberar_alerta)])
    dialog.open()

def liberar_alerta(obj):
    alerta()

