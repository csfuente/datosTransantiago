import json
import urllib2

letras = ['A','B','C','D','E','F','G','H','I','J']
url = 'http://dev.adderou.cl/transanpbl/busdata.php?paradero=P'


print "Recolectando informacion para comenzar"
web = urllib2.urlopen('http://dev.adderou.cl/transanpbl/busdata.php?paradero=PZ000')
campo_vacio = json.load(web)
web.close()

contador = 1
loop = True


print 'Listando Paraderos:'
for i in letras:
	loop = True
	while (loop):
		try:
			web = urllib2.urlopen(url + i + str(contador),timeout=5)
			data = json.load(web)
			web.close()
			if (data == campo_vacio):
				loop = False
				contador = 1
		except:
			print "Reintentando"
		else:
			print 'P' + i + str(contador) + '   ' + data['descripcion'].encode('utf-8') + '   ' + data['horaConsulta']
			for servicio in data['servicios']:
				if(servicio['valido']):
					print 'Servicio ' + servicio['servicio'] + ' Patente: ' + servicio['patente'] + ' tiempo: ' + servicio['tiempo'] + ' distancia: ' + servicio['distancia']
			contador += 1
