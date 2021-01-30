import sys
sequence_0 = (14,10,35,45,60,70,90,0,105,150,10.0,45.0,70,0)
sequence_1 = (14,10,35,45,60,70,90,0,105,150,70)
sequence_2 = (14,10,35,45,60,70,90,0,105,150,10.0,45.0,70,0.0)
sequence_3 = (14,10,35,45,60,70,90,0,105,150,10.0,45.0,70)


a = sorted(sequence_0)
for i in range(int(len(sequence_0))-1):
	if a[i]==a[i+1]:
		print("Posledovatelnost' ne unikalna")
		break
	else:
		if (i+1) != int(len(sequence_0)-1):
			pass
		else:
			print("Posledovatelnost' unikalna")
	

a = sorted(sequence_1)
for i in range(int(len(sequence_1))-1):
	if a[i]==a[i+1]:
		print("Posledovatelnost' ne unikalna")
		break
	else:
		if (i+1) != int(len(sequence_1)-1):
			pass
		else:
			print("Posledovatelnost' unikalna")

a = sorted(sequence_2)
for i in range(int(len(sequence_2))-1):
	if a[i]==a[i+1]:
		print("Posledovatelnost' ne unikalna")
		break
	else:
		if (i+1) != int(len(sequence_2)-1):
			pass
		else:
			print("Posledovatelnost' unikalna")

a = sorted(sequence_3)
for i in range(int(len(sequence_3))-1):
	if a[i]==a[i+1]:
		print("Posledovatelnost' ne unikalna")
		break
	else:
		if (i+1) != int(len(sequence_3)-1):
			pass
		else:
			print("Posledovatelnost'  unikalna")

