from collections import deque


def bfs(start, end, neighbors):
    if start == end:
        return [start]

    visited = {start}
    queue = deque([(start, [])])

    while queue:
        current, path = queue.popleft()
        visited.add(current)

        for neighbor in neighbors(current):
            if neighbor == end:
                return path + [current, neighbor]

            if neighbor in visited:
                continue

            queue.append((neighbor, path + [current]))
            visited.add(neighbor)

    return None
