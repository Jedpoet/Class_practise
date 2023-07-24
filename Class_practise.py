import random

def rand_name() -> str:
    t = random.randint(3, 4)
    name = ""
    for i in range(t):
        name = name + chr(random.randint(0x4e00, 0x9fbf))
    print(name)
    return name    

ans_lib = [
    [["謝謝你，放那邊就行了"], ["謝謝你～"], ["你對我最好了～"]],
    [["阿，不用了謝謝"], ["真不好意思讓你破費了"], [""]],
    [["（摔）滾，你這隻肥豬"], ["謝啦（搶）"], ["哼，我就勉為其難的接受吧"]],
]
#ans_lib[個性值0（乖巧）～2（毒舌）][好感度階段0（討厭）～2（交往）]

class NPC():
    def __init__(self, age, name = None) -> None:
        self.age = age          #年齡
        self.favorability = 0   #好感度
        if name == None:
            self.name = rand_name()
        else:
            self.name = name
    def send_gift()->str:
        ans = "something"
        return ans
    
class Group():
    def __init__(self, number:int=None, leader:NPC=None) -> None:
        self.group_number = number
        self.group_members = []
        if leader==None:
            self.leader = NPC(random.randint(30, 60))
        elif type(leader).__name__ == "NPC":
            self.leader = leader

    def add_new_number(self, new_number:NPC):
        self.group_members.append(new_number)

    def random_chose_member(self):
        return self.group_members[random.randint(0, self.group_number)]

class Class(Group):
    def __init__(self, grade:int) -> None:
        self.grade = grade
        self.leader = NPC(random.randint(30, 60))

    def generate_classmate(self):
        if self.group_number == None:
            self.group_number = random.randint(25, 40)
        for i in range(self.group_number):
            self.group_members.append(NPC(self.grade+15))

if __name__ == "__main__":
    rand_name()

