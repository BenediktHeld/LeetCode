class Solution(object):
    def CheckDuplicatesTriplets(self, ListAll, new_triplet):
        # Konvertiere jede Triplet-Liste in ein Set, um die Reihenfolge zu ignorieren
        unique_triplets = {tuple(sorted(triplet)) for triplet in ListAll}

        # Erstelle ein sortiertes Tuple für das neue Triplet
        new_triplet_sorted = tuple(sorted(new_triplet))

        # Überprüfe, ob das neue Triplet bereits vorhanden ist
        if new_triplet_sorted in unique_triplets:
            return False  # Triplet ist bereits vorhanden
        else:
            return True  # Triplet ist neu und kann hinzugefügt werden

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # List for all
        ListAll = []

        for z1 in range(len(nums)):
            for z2 in range(z1 + 1, len(nums)):
                for z3 in range(z2 + 1, len(nums)):
                    array = []
                    if (nums[z1] + nums[z2] + nums[z3] == 0):
                        array.append(nums[z1])
                        array.append(nums[z2])
                        array.append(nums[z3])
                        if self.CheckDuplicatesTriplets(ListAll, array):
                            ListAll.append(array)
        return ListAll

# Beispielverwendung
nums = [-1, 0, 1, 2, -1, -4]
solution = Solution()
print(solution.threeSum(nums))
