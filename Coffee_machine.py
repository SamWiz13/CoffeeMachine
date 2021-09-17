coffee={
    'shakar': 3000,
    'shokolad': 3000,
    'sut': 5000,
    'suv': 5000,
    'Tangalar' : {
        '5000':  200,
        '1000':  500,
        '500' :  1000
    },
    'Qahvalar': {
        'Americano': 3000,
        'Latte' : 4000,
        'Cappucino' : 4000,
        'Espresso' : 3000
    },
    'Americano':{
        'shokolad' : 30,
        'qahva': 30,
        'suv' : 150,
        'shakar': 10,
        'narxi' : 8500
    },
    'Latte': {
        'shokolad' : 30,
        'qahva' : 20,
        'suv' : 50,
        'sut': 100,
        'shakar': 10,
        'narxi': 7000
    },
    'Cappucino' :{
        'shokolad' : 50,
        'qahva' : 40,
        'suv' : 20,
        'sut': 100,
        'shakar': 10,
        'narxi': 14500
    },
    'Espresso' :{
        'qahva' : 30,
        'shokolad' : 50,
        'sut': 100,
        'shakar': 15,
        'narxi' : 11000
    }
}

# Pulni hisoblash va qaytim yoki kofe
def money(S,dicti,satr):
    qaytim =""
    while True:
          if S==coffee[satr]['narxi']:
              for i in coffee['Tangalar'].keys():
                  coffee['Tangalar'][i] +=dicti[i]
              return 0

          if S >coffee[satr]['narxi']:
               S -=coffee[satr]["narxi"]
               for i in coffee['Tangalar'].keys():
                   coffee['Tangalar'][i] +=dicti[i]
               for i in dicti.keys():
                   count =0
                   while S >=int(i) and coffee['Tangalar'][i] >=1:
                       coffee['Tangalar'][i] -=1
                       count +=1
                       S -=int(i)
                       
                   qaytim +=str(count) + " " + i + "-so'mlik \n"

                   if S ==0:
                       break
               return qaytim

          if S <coffee[satr]['narxi']:
              print(f"{satr} uchun {coffee[satr]['narxi'] -S} so'm yetmayabdi.")
              for i in coffee['Tangalar'].keys():
                  if coffee[satr]['narxi']- S>=int(i):
                      kirim =int(input(f"{i} so'mlik ---->"))
                      dicti[i] +=kirim
                      S +=kirim*int(i)
# Menyu va qahva tanlash
print("Menyu : ")
for j,i in zip(range(1,len(coffee['Qahvalar'].keys())+1),coffee['Qahvalar'].keys()):
    print(j,i,"-",coffee[i]['narxi'])

t = int(input('Kerakli qahvani tanlang ----> '))
if  t<len(coffee['Qahvalar'].keys())+1:
    satr =list(coffee['Qahvalar'].keys())[t-1]
    print(f"Siz {satr} tanladingiz - Narxi : {coffee[satr]['narxi']}")
    dicti={}; S=0

    for i in coffee['Tangalar'].keys():
            dicti[i] = int(input(f"{i} - so'mlik:---->"))
            S+=dicti[i]*int(i)
    qaytim =money(S,dicti,satr)

    if qaytim ==0:
        print(f"Siz uchun {satr}")
    else:
        print("Sizni qaytimingiz :\n"  + qaytim)
        print(f"Siz uchun {satr}")







