#class
#aşağıda yaratacağın instance'lar için clas'a verilen h default namedir.
class Human:
    name="Hande"
    #built-in
    #constructor
    #initialize
    def __init__(self,name) -> None:
        self.name=name
        #yeni gelen isimleri yeni isim yap 
        print("Bir human instance'i üretildi")
    def __str__(self):
        return f"STR fonksiyonundan dönen değer: {self.name}"
    def talk(self,sentence):
        name="Cenk"
        print(f"{self.name}: {sentence}")
    def walk(self):
        print("human is walking..")
#self=>this
#instance
human1=Human()
human1.name="berk"
human1.talk('merhaba')
human1.walk()
print(human1)

human2=Human()
human2.name="cem"
human2.talk("hi")
human2.walk()
print(human2)