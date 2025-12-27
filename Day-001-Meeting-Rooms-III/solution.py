import heapq

class Solution:
    def mostBooked(self, n, meetings):
        count = [0] * n
        meetings.sort()

        occupied = []  # (endTime, roomId)
        available_rooms = list(range(n))
        heapq.heapify(available_rooms)

        for start, end in meetings:
            while occupied and occupied[0][0] <= start:
                _, room_id = heapq.heappop(occupied)
                heapq.heappush(available_rooms, room_id)

            if available_rooms:
                room_id = heapq.heappop(available_rooms)
                count[room_id] += 1
                heapq.heappush(occupied, (end, room_id))
            else:
                prev_end, room_id = heapq.heappop(occupied)
                count[room_id] += 1
                duration = end - start
                heapq.heappush(occupied, (prev_end + duration, room_id))

        return count.index(max(count))
