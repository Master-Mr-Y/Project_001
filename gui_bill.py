""" from datetime import datetime

now = datetime.now()

date = now.strftime("%d-%m-%Y")
time = now.strftime("%I:%M:%S %p")

name = input("Enter name:")
address = input("Address:")
persons = input("N.Persons:")
room_type = input("AC/Non-AC:")

no_of_rooms = 0
rooms = ["A","B","C","D","E","F"]
def room_cound():
    global no_of_rooms
    no_of_rooms+=1
for i in rooms:
    add = input(f"Do you wanna room {i} y/n:")
    if add == "y":
        room_cound()
    else:
        break 
selected_rooms =""
for i in range(0,no_of_rooms):
    print(f"Select room {rooms[i]}")
    selected_rooms += rooms[i]+" "
print("room selected over done next \n")           

days_live = float(input("How many days:"))

discound = 0

w_discound = input("do you wanna add any discound y/n:")
if w_discound == "y":
    disc_amd = int(input("Amound:"))
    discound += disc_amd
print(f"\n\tGenerate a custome bill\n___________________________________\nName:{name}\nAddress:{address}\nNo.of persons:{persons}\nrooms:{selected_rooms}\nTotal rooms:{no_of_rooms}\nRoomTye:{room_type}\ndscound:{discound}\ndays:{days_live}") 

if room_type == "AC":
    roomch = float(812.90*days_live)
    gst=2.5
    gst_amd = roomch*gst/100
    
    grand_ttl = roomch+gst_amd*2
    
    print("____________________\nroom charge:",roomch)
    print("GST 5% :",gst_amd*2)
    print("Total :",round(grand_ttl,2),"\n___________________")
    print(f"Discount:{discound}-{grand_ttl}")
    print(f"Grand total:{round(grand_ttl,2)-discound}")
else:
    roomch = float(761.90*days_live)
    gst=2.5
    gst_amd = roomch*gst/100
    
    grand_ttl = roomch+gst_amd*2
    
    print("\n room charge:",roomch)
    print("GST 5% :",gst_amd*2)
    print("\nGrand Total :",round(grand_ttl,2)) """
    

class Main:
    def __init__(self):
        self.name = str(input("Enter Name:"))
        self.address = str(input("Enter the Address:"))
        self.aadhar = int(input("Enter Aaadhar/Gstin:"))
        self.days = int(input("How many days:"))
        self.prsons = int(input("How Many members:"))
        self.arr_date =str(input("Arr date:"))
        self.arr_time =str(input("Arr time"))
        self.dep_date =str(input("dep date:"))
        self.dep_time =str(input("dep time"))
        self.room_type =str(input("AC/Non-AC type(AC/NC):"))
        self.rooms = ["A","B","C","D","E","F"]
        self.room_count = 0
        self.choice_roms = str("")
        self.ch_rm_cunt =0
        for self.i in self.rooms:
            self.room_count+=1
            self.choice = str(input(f"Do you wanna room {self.i} type(y/n):"))
            if self.choice == "y":
                self.ch_rm_cunt+=1
                self.choice_roms += str(self.rooms[self.room_count-1]+" ")
        
        self.total_rooms = self.ch_rm_cunt
        print(f"Selected rooms:{self.choice_roms}")
        print(f"Total rooms:{self.total_rooms}")
        
    def calculation(self):
        self.gst1 = 2.5
        self.gst2 = 2.5
        self.ac_room_amd = 800.00
        self.nc_room_amd = 761.90
        if self.room_type == "AC" or self.room_type == "ac":
            self.roomcharge_cound_amd_per_day = (self.days * self.ac_room_amd) * self.ch_rm_cunt
            self.gst_count1 = self.roomcharge_cound_amd_per_day * self.gst1 /100
            self.gst_count2 = self.roomcharge_cound_amd_per_day * self.gst2 /100
            self.gst_final_amd = self.gst_count1 + self.gst_count2
            self.grand_total = round(self.roomcharge_cound_amd_per_day + self.gst_final_amd,2)
            return self.roomcharge_cound_amd_per_day,self.grand_total,self.gst_count1,self.gst_count2
                                  
        elif self.room_type == "NC" or self.room_type == "nc":
            self.roomcharge_cound_amd_per_day = (self.days * self.nc_room_amd) * self.ch_rm_cunt
            self.gst_count1 = self.roomcharge_cound_amd_per_day * self.gst1 /100
            self.gst_count2 = self.roomcharge_cound_amd_per_day * self.gst2 /100
            self.gst_final_amd = self.gst_count1 + self.gst_count2
            self.grand_total = round(self.roomcharge_cound_amd_per_day + self.gst_final_amd,2)
            return self.roomcharge_cound_amd_per_day,self.grand_total,self.gst_count1,self.gst_count2
        else:
            print("Room type error")
    def display(self):
        print("\n\n \t Generated bill preview\n\t--------------------------\n\n")
        print(f"Name:{self.name}\naddress:{self.address}\nAadhar:{self.aadhar}\nNo.of days:{self.days}\n")
        self.total,self.grand_ttl,self.gst1,self.gst2 = self.calculation()
        print("-----------------------------\nTotal room charge:",self.total)
        print("GST 2.5%:",self.gst1,"\nGST 2.5%:",self.gst2)
        print("Grand total:",self.grand_ttl,"\n------------------------------")
        
if __name__ == "__main__":
    print("Bill genetrator terminal prototype\n") 
    
    obj = Main()
    obj.display()
    
    
    
        
        

   