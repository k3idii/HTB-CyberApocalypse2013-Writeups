import re


'''
Solver for The Chasm's Crossing Conundrum from HackTheBox Cyber Apocalypse 2023 CTF

usage:
python3 solver.py
7
Person 1 will take 93 minutes to cross the bridge.
Person 2 will take 50 minutes to cross the bridge.
Person 3 will take 87 minutes to cross the bridge.
Person 4 will take 6 minutes to cross the bridge.
Person 5 will take 64 minutes to cross the bridge.
Person 6 will take 20 minutes to cross the bridge.
Person 7 will take 77 minutes to cross the bridge.
The flashlight has charge for 338 minutes.

Assuming the goal is to transport people from left to right.

'''



class Solver():
    people_left:list   
    people_right:list
    SEQUENCE:list
    flashlight_time:int
    flashlight_side:str
    solved:bool

    def __init__(self):
        self.people_left = []
        self.people_right = []
        self.SEQUENCE = []
        self.flashlight_time = 0
        self.solved = False

    def find_min(self,ppl_list:list, ret_num=2):
        sorted_ppl = sorted(ppl_list, key=lambda x: x.get("time"))
        return sorted_ppl[0:ret_num]

    def find_max(self,ppl_list:list, ret_num=2):
        sorted_ppl = sorted(ppl_list, key=lambda x: x.get("time"), reverse=True)
        return sorted_ppl[0:ret_num]

    def cross(self,ppl_list:list, direction:str, ):
        tmp_time = 0
        ppl_ids = []
        for x in ppl_list:
            if x.get("time") > tmp_time:
                tmp_time = x.get("time")
            print(f"[*] Person #{x.get('id')} crossing")
            ppl_ids.append(x.get('id'))

        print(f"Crossing {len(ppl_list)} people {direction}. Time: {tmp_time}")
        
        self.flashlight_time -= tmp_time
        ppl_ids_list = ",".join(ppl_ids)
        self.SEQUENCE.append(f"[{ppl_ids_list}]")

        if direction == "right":
            for x in ppl_list:
                if x in self.people_left:
                    self.people_left.remove(x)
                self.people_right.append(x)
                self.flashlight_side = "right"
        if direction == "left":
            for x in ppl_list:
                self.people_left.append(x)
                if x in self.people_right:
                    self.people_right.remove(x)
                self.flashlight_side = "left"

        self.solved = len(self.people_left) == 0
        

    def print_state(self):
        ppl_ids_left = []
        for x in self.people_left:
            ppl_ids_left.append(x.get("id"))
        
        ppl_ids_right = []
        for x in self.people_right:
            ppl_ids_right.append(x.get("id"))

        print(f"[*] STATE LEFT: {','.join(ppl_ids_left)}    RIGHT: {','.join(ppl_ids_right)}    FLASHLIGHT: {self.flashlight_time} min, flashlight location {self.flashlight_side}")
        print("[+] SEQUENCE:")
        print(",".join(self.SEQUENCE))
        print("===== ======= =======")

    def solve(self):
        # load data
        PEOPLE_NUM = int(input("Number of people: "))

        self.flashlight_time = 0

        person_pattern = re.compile(r"Person (\d) will take (\d?\d?\d) minutes to cross the bridge")
        flashlight_pattern = re.compile(r"The flashlight has charge for (\d?\d?\d) minutes")

        for x in range(0,PEOPLE_NUM):
            line_parse = input()
            x = person_pattern.findall(line_parse)
            person_id = x[0][0]
            time = x[0][1]
            self.people_left.append({
                "id": person_id,
                "time": int(time)
            })

        
        line_parse = input()
        x = flashlight_pattern.findall(line_parse)
        self.flashlight_time = int(x[0])

        while(not self.solved):

            # cross 2 fastest
            candidates = self.find_min(self.people_left, 2)
            self.cross(candidates, "right")
            self.print_state()

            if self.solved:
                break

            # return 1st fastest with flashlight
            candidates = self.find_min(self.people_right, 1)
            self.cross(candidates, "left")
            self.print_state()

            # cross 2 slowest
            candidates = self.find_max(self.people_left, 2)
            self.cross(candidates, "right")
            self.print_state()

            if self.solved:
                break

            # return 2nd with flashlights
            candidates = self.find_min(self.people_right, 1)
            self.cross(candidates, "left")
            self.print_state()

        
        print("[+] FINAL SEQUENCE:")
        print(",".join(self.SEQUENCE))


a = Solver()
a.solve()