import hangman
import reversegam
import tictactoeModificado
import json
import PySimpleGUI as sg

def cargar_datos():

	import os

	if os.path.exists('juegos-datos.json'):
		archivo = open('juegos-datos.json','r')
		dic = json.load(archivo)
		archivo.close()
	else:
		dic = {}

	return dic

def obtener_fecha():

	import datetime

	fecha = datetime.datetime.now()
	fecha = fecha.strftime('%x')+'-'+fecha.strftime('%X') 

	return fecha

def datos_del_jugador(datos,fecha):

	layout_jugador = [
    	[sg.Text('Ingrese sus datos a continuación:',background_color='#EAE7C8',text_color='#000000',pad=((0,0),(5,15)))],
    	[sg.Text('Nombre:',background_color='#EAE7C8',text_color='#000000'),sg.InputText(key='_nombre_')],
    	[sg.Text('Apellido:',background_color='#EAE7C8',text_color='#000000'),sg.InputText(key='_apellido_')],
    	[sg.Text('Edad:',background_color='#EAE7C8',text_color='#000000'),sg.InputText(key='_edad_')],
    	[sg.Text('¿A qué juego jugaste?',background_color='#EAE7C8',text_color='#000000'),sg.InputText(key='_juego_')],
    	[sg.Button('Aceptar',pad=((155,0),(15,0))),sg.Text(fecha,background_color='#EAE7C8',text_color='#000000',pad=((100,0),(25,0)))]
	]
	window_jugador = sg.Window('Datos del Jugador',layout_jugador,size=(400,200),background_color='#EAE7C8')

	while True:
		event,values = window_jugador.read()
		if event is None:
			break
		if event == 'Aceptar':
			if (values['_nombre_'] != '') and (values['_apellido_'] != '') and (values['_edad_'] != '') and (values['_juego_'] != ''):
				sg.popup('Gracias por jugar!',title='Gracias!')
				break
			else:
				sg.popup('Asegurate de completar todos los datos antes de seguir!',title='Ohoh')
	window_jugador.close()

	if event is not None:
		datos[fecha] ={
			'nombre' : values['_nombre_'],
			'apellido' : values['_apellido_'],
			'edad' : values['_edad_'],
			'juego' : values['_juego_']
		}
	
		archivo = open('juegos-datos.json','w')
		json.dump(datos,archivo)
		archivo.close()

def main(args):

	datos = cargar_datos()

	layout_columna1 = [
    	[sg.Text('Seleccione un juego:',background_color='#EAE7C8',text_color='#000000')],
    	[sg.Listbox([' AHORCADO',' TA-TE-TI',' OTELLO'],key='_JUEGOS_',pad=((10,10),(10,10)),size=(18,3),font=10)]
	]

	layout_columna2 = [
    	[sg.Button('JUGAR',key='_JUGAR_',auto_size_button=True,font=10,button_color=('#000000','#D5D2B3'))],
    	[sg.Button('SALIR',key='_SALIR_',auto_size_button=True,font=10,button_color=('#000000','#D5D2B3'))]
	]

	layout_menu = [
		[sg.Text('BIENVENIDO A JUEGOS.PY',justification='center',size=(100,1),font=['Fixedsys',20],text_color='#F74646',background_color='#EAE7C8')],
    	[sg.Column(layout_columna1,background_color='#EAE7C8'), sg.Column(layout_columna2,background_color='#EAE7C8',pad=((10,10),(33,10)))]
	]

	window_menu = sg.Window('Menú de Juegos',layout_menu,size=(400,200),background_color='#EAE7C8')

	while True:
		event,values = window_menu.read()
		if event in (None,'_SALIR_'):
			break
		if event == '_JUGAR_':
			if values['_JUEGOS_'] != []:
				if values['_JUEGOS_'][0] == ' AHORCADO':
					window_menu.hide()
					hangman.main()
				elif values['_JUEGOS_'][0] == ' TA-TE-TI':
					window_menu.hide()
					tictactoeModificado.main()
				elif values['_JUEGOS_'][0] == ' OTELLO':
					window_menu.hide()
					reversegam.main()

				fecha = obtener_fecha()
				datos_del_jugador(datos,fecha)

				window_menu.un_hide()
			else:
				sg.popup('Debes elegir un juego antes!',title='Ohoh')

	window_menu.close()
		
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
