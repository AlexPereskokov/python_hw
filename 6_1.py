from time import sleep


class TrafficLight:
    __color = ['Red', 'Yellow', 'Green']

    def running(self):
        cnt = 0
        while cnt < 3:
            print(f'TrafficLight actually is: {TrafficLight.__color[cnt]} , wait a moment')
            if cnt == 0:
                sleep(7)
            elif cnt == 1:
                sleep(5)
            elif cnt == 2:
                sleep(3)
            cnt += 1


tl = TrafficLight()
tl.running()
