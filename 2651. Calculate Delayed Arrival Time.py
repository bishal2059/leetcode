class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        output_time = (arrivalTime + delayedTime) % 24
        return output_time
        
def __main__():
    arrivalTime = 13
    delayedTime = 11
    delayed_arrival_time = Solution().findDelayedArrivalTime(arrivalTime, delayedTime)
    print(delayed_arrival_time)