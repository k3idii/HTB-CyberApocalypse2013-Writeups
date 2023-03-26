# misc :: The Chasm's Crossing Conundrum

## The problem statement

After connecting to the socket given in the challenge and engering game mode, we were given the following information:
```
Person 1 will take 93 minutes to cross the bridge.
Person 2 will take 50 minutes to cross the bridge.
Person 3 will take 87 minutes to cross the bridge.
Person 4 will take 6 minutes to cross the bridge.
Person 5 will take 64 minutes to cross the bridge.
Person 6 will take 20 minutes to cross the bridge.
Person 7 will take 77 minutes to cross the bridge.
The flashlight has charge for 338 minutes.
```

So there were information about the number of people and how long does the flashlight last until the batteries go down. The goal was to move everyone accross the bridge, but:
- the flashlight had to be carried out each time - noone can travel in darkness --> someone had to go back with the flashlight each time
- only 2 people could pass at the same time

The challenge was timing out quickly, so the goal was to implement an algorigtm that will solve the problem (give the correct sequence of people passing the bridge).

Additional obstacles:
- the challenge times out quickly, so the answer has to be computed
- the challenge gives different number of people and different times on each run

## The solution

This is a variant of [Bridge and Torch problem](https://en.wikipedia.org/wiki/Bridge_and_torch_problem) which had an easy solution describe on the linked page. The general idea was to use 2 fastest people to carry on the flashlight back and forth.

The solution is presented in [solver.py](solver.py)

## Example
```shell
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
```

output will give:
```pre
[*] Person #4 crossing
[*] Person #6 crossing
Crossing 2 people right. Time: 20
[*] STATE LEFT: 1,2,3,5,7    RIGHT: 4,6    FLASHLIGHT: 318 min, flashlight location right
[+] SEQUENCE:
[4,6]
===== ======= =======
[*] Person #4 crossing
Crossing 1 people left. Time: 6
[*] STATE LEFT: 1,2,3,5,7,4    RIGHT: 6    FLASHLIGHT: 312 min, flashlight location left
[+] SEQUENCE:
[4,6],[4]
===== ======= =======
[*] Person #1 crossing
[*] Person #3 crossing
Crossing 2 people right. Time: 93
[*] STATE LEFT: 2,5,7,4    RIGHT: 6,1,3    FLASHLIGHT: 219 min, flashlight location right
[+] SEQUENCE:
[4,6],[4],[1,3]
===== ======= =======
[*] Person #6 crossing
Crossing 1 people left. Time: 20
[*] STATE LEFT: 2,5,7,4,6    RIGHT: 1,3    FLASHLIGHT: 199 min, flashlight location left
[+] SEQUENCE:
[4,6],[4],[1,3],[6]
===== ======= =======
[*] Person #4 crossing
[*] Person #6 crossing
Crossing 2 people right. Time: 20
[*] STATE LEFT: 2,5,7    RIGHT: 1,3,4,6    FLASHLIGHT: 179 min, flashlight location right
[+] SEQUENCE:
[4,6],[4],[1,3],[6],[4,6]
===== ======= =======
[*] Person #4 crossing
Crossing 1 people left. Time: 6
[*] STATE LEFT: 2,5,7,4    RIGHT: 1,3,6    FLASHLIGHT: 173 min, flashlight location left
[+] SEQUENCE:
[4,6],[4],[1,3],[6],[4,6],[4]
===== ======= =======
[*] Person #7 crossing
[*] Person #5 crossing
Crossing 2 people right. Time: 77
[*] STATE LEFT: 2,4    RIGHT: 1,3,6,7,5    FLASHLIGHT: 96 min, flashlight location right
[+] SEQUENCE:
[4,6],[4],[1,3],[6],[4,6],[4],[7,5]
===== ======= =======
[*] Person #6 crossing
Crossing 1 people left. Time: 20
[*] STATE LEFT: 2,4,6    RIGHT: 1,3,7,5    FLASHLIGHT: 76 min, flashlight location left
[+] SEQUENCE:
[4,6],[4],[1,3],[6],[4,6],[4],[7,5],[6]
===== ======= =======
[*] Person #4 crossing
[*] Person #6 crossing
Crossing 2 people right. Time: 20
[*] STATE LEFT: 2    RIGHT: 1,3,7,5,4,6    FLASHLIGHT: 56 min, flashlight location right
[+] SEQUENCE:
[4,6],[4],[1,3],[6],[4,6],[4],[7,5],[6],[4,6]
===== ======= =======
[*] Person #4 crossing
Crossing 1 people left. Time: 6
[*] STATE LEFT: 2,4    RIGHT: 1,3,7,5,6    FLASHLIGHT: 50 min, flashlight location left
[+] SEQUENCE:
[4,6],[4],[1,3],[6],[4,6],[4],[7,5],[6],[4,6],[4]
===== ======= =======
[*] Person #2 crossing
[*] Person #4 crossing
Crossing 2 people right. Time: 50
[*] STATE LEFT:     RIGHT: 1,3,7,5,6,2,4    FLASHLIGHT: 0 min, flashlight location right
[+] SEQUENCE:
[4,6],[4],[1,3],[6],[4,6],[4],[7,5],[6],[4,6],[4],[2,4]
===== ======= =======
[+] FINAL SEQUENCE:
[4,6],[4],[1,3],[6],[4,6],[4],[7,5],[6],[4,6],[4],[2,4]
```