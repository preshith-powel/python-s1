class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.__hour = hour
        self.__minute = minute
        self.__second = second
    
    def __add__(self,other):
        sumoftime=Time()
        sumoftime.__hour=self.__hour+other.__hour
        sumoftime.__minute=self.__minute+other.__minute
        sumoftime.__second=self.__second+other.__second
        return sumoftime

    def getTime(self):
        return f"Sum of times is: ' {self.__hour}:{self.__minute}:{self.__second} '"
    
if __name__=="__main__":
    time1=input("Enter 1st time in the format of \"hh:mm:ss\": ").split(":")
    time2=input("Enter 2nd time in the format of \"hh:mm:ss\": ").split(":")
    hour1=time1[0]
    minute1=int(time1[1])
    second1=int(time1[2])
    hour2=int(time2[0])
    minute2=int(time2[1])
    second2=int(time2[2])
    t1=Time(hour1,minute1,second1)
    t2=Time(hour2,minute2,second2)
    t3=t1+t2
    print(t3.getTime())