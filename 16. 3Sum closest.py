class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()  # Sortiere das Array
        closest_sum = float('inf')  # Setze den nächstgelegenen Wert auf unendlich

        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1  # Setze die zwei Zeiger

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                # Überprüfe, ob der aktuelle Summe näher am Ziel ist
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum

                # Bewege die Zeiger basierend auf der Summe
                if current_sum < target:
                    left += 1  # Erhöhe den linken Zeiger
                elif current_sum > target:
                    right -= 1  # Verringere den rechten Zeiger
                else:
                    # Wenn die Summe genau dem Ziel entspricht, gib sie zurück
                    return current_sum

        return closest_sum
