# multiple methods in the oop python 
class SmartAc:
    def __init__(self,room_name,tempurature=24,is_on=False):
        self.room_name=room_name
        self.tempurature=tempurature
        self.is_on=is_on
    def turn_on(self):
        self.is_on=True
    def turn_off(self):
        self.is_on=False
    def change_tempuratue(self,new_tempurature):
        if self.is_on:
            self.tempurature=new_tempurature
        else:
            print("Please turn on the AC first to change the tempurature")
Room1=SmartAc("khubaib room",)
print(Room1.tempurature)
print(Room1.is_on)
print(Room1.room_name)
print("turning on the AC")
Room1.turn_on()
print(Room1.is_on)
print("changing tempurature to 18")
Room1.change_tempuratue(18)
print(Room1.tempurature)
Room1.turn_off()
print(Room1.is_on)
print("changing tempurature to 30")
Room1.change_tempuratue(30)
print(Room1.tempurature)
Room1.turn_on()
print(Room1.is_on)
print("changing tempurature to 30")
Room1.change_tempuratue(30)
print(Room1.tempurature)


            