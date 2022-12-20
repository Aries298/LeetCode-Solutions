class Solution:
    def visitAll(self, rooms, index, visited):
        if index not in visited:
            visited.add(index)
            for found_key in rooms[index]:
                self.visitAll(rooms, found_key, visited)

    def canVisitAllRooms(self, rooms) -> bool:
        visited = set()
        self.visitAll(rooms, 0, visited)
        return len(visited) == len(rooms)