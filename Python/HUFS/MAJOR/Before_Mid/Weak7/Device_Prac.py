from abc import ABC, abstractmethod

class Device(ABC):
    def __init__(self, name):
        self.name = name
        self.__status = False

    @abstractmethod
    def turn_on(self):
        self.__status = True

    @abstractmethod
    def turn_off(self):
        self.__status = False

    # getter
    @property
    def status(self):
        return self.__status

class Light(Device):
    def __init__(self, name, brightness=0):
        super().__init__(name)
        self.__brightness = brightness

    @property
    def brightness(self):
        return self.__brightness
    
    @brightness.setter
    def brightness(self, brightness):
        if brightness >= 0: 
            self.__brightness = brightness
            print(f"[{self.name}] 밝기 설정 : {self.__brightness}%")
        else:
            print("밝기는 0 미만으로 설정할 수 없습니다.")

    def turn_on(self):
        super().turn_on()
        print(f"[{self.name}] 조명이 켜졌습니다 (밝기 {self.__brightness})")

    def turn_off(self):
        super().turn_off()
        print(f"[{self.name}] 조명이 꺼졌습니다.")

    def __str__(self):
        self_str = "ON" if self.status else "OFF"
        return f"Light('{self.name}', status = {self_str}"

    

devices = [Light("거실등", brightness= 70), 
           Light("침실등", brightness= 30)]

print("=== 초기 상태 ===")
for d in devices:
    print(d, "| status =", d.status)

print("\n=== 일괄 점등 ===")
for d in devices:
    d.turn_on()

print("\n=== 밝기 변경 ===")
devices[0].brightness = 90

print("\n=== 일괄 소등 ===")
for d in devices:
    d.turn_off()

print("\n=== 최종 상태 ===")
for d in devices:
    print(d, "| status =", d.status)