#Python ile kriptoloji

sifrelenecek = ['1','2','3','4','5','6','7','8','9','0','A','B','C','Ç','D','E','F','G','Ğ','H','I','İ','J','K',
            'L','M','N','O','Ö','P','Q','R','S','Ş','T','U','Ü','V','W','X',
           'Y','Z','a','b','c','ç','d','e','f','g','ğ','h','ı','i',
            'j','k','l','m','n','o','ö','p','q','r','s','ş','t','u','ü','v','w','x','y','z',' ']

sifrelenmis = ['Q%#u5','19j/(','h=7su','P4uP*','m*5y4','ü+7lş','çö0s3','qwe/>','ğpmop','<asup','#™!9e',';s7R-',
            '+ğZxç','V#sde','@:O∟@','L&r<^',':(S6+','b1Öu£','?@Jsü',',|ĞA7','*V|\/','´5`Ç=','8;uFr','<:/->',
            '}S½sw','i[Iu4','♫☻$a8','a4m83','4☼aİ','◄q9S4','*~+C8','← →ô¬','Ù☺♦ê8','µ¢ÕË~','?%r£╚','+dŞ,*','♠○•♦◘',
           'Y7ğs9','öp12U','éd&f?','АКнЭЪ','A\c-|','asb6w','+s4op','=sl-s','dsp-3','Çhs9Y',':D8d<','>suEn',',fn86',
            'ç:S7D','dm-?2','*dc87','┬sy<*','sa^£2','4€+Sf','7s94ö','iğüra','ksdm2','2bs8A','Bc3x)','dsop7','dsl5Ü',
            'H5(:2','55{/t','As0Üs','+Ğ]=ç','{isad','7s}hK','0SmO=','lOl?s','BO|_2','a?-Üi','y!saı','|*\/i']


while True:
    istek = input("\nŞifre oluşturmak için '1', Şifre çözmek için '2' , Programı kapatmak için '0' yazın :")
    if istek=="0":
        print("Program sonlandırılıyor...")
        break

    elif istek=="1":
            veri = input("Şifrelemek istediğiniz veriyi giriniz :")
            for i in range(0, len(veri)):
                for x in range(0, len(sifrelenecek)):
                    if sifrelenecek[x] == veri[i]:
                     print(sifrelenmis[x], end="")

    elif istek=="2":
        giris = input("Şifresini çözmek istediğiniz veriyi giriniz :")
        uzunluk = len(giris)+1
        a=5
        b=0
        for i in range(0, uzunluk):
            for x in range(0, len(sifrelenmis)):
                if a < uzunluk and b < uzunluk:
                    if sifrelenmis[x] == giris[b:a]:
                        b += 5
                        a += 5
                        print(sifrelenecek[x], end="")

    elif istek!= "1" or "2" or "0":
        print("Lütfen '1','2' veya '0' tuşlayın...")
