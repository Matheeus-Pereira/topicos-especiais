estudantes = {
"Alice": 85,
"Bob": 92,
"Charlie": 78,
"Diana": 88,
"Edward": 67,
"Fiona": 74,
"George": 53,
"Hannah": 59,
"Irene": 48,
"Jack": 95,
"Kelly": 84,
"Leo": 72,
"Mia": 64,
"Noah": 58,
"Olivia": 45
}

notas = {
'A': [],
'B': [],
'C': [],
'D': [],
'E': [],
'F': []
}
print(estudantes.values())

for estudante in estudantes:
   if 90<=estudantes[estudante]<100:
      notas["A"].append(estudante)
   elif 80<= estudantes[estudante] <90:
     notas["B"].append(estudante)
   elif 70<= estudantes[estudante] <80:
       notas["C"].append(estudante)
   elif 60<=estudantes[estudante] <70:
       notas["D"].append(estudante)
   elif 50<=estudantes[estudante] <60:
       notas["E"].append(estudante)
   else:
       notas["F"].append(estudante)

print(notas)