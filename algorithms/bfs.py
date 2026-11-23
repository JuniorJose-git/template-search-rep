from collections import deque
from puzzle.base_search import BaseSearch
from puzzle.state import State
from puzzle.result import SearchResult

DEFAULT_DEPTH_LIMIT = 50

class BFS(BaseSearch):

    def __init__(self, depth_limit: int = DEFAULT_DEPTH_LIMIT):
        self.depth_limit = depth_limit

    def search(self, initial: State) -> SearchResult:

        visited = {initial: 0}
        queue = []

        queue.append(initial)

        current = queue[0]

        nodes_expanded = 0
        nodes_generated = 0
        max_frontier_size = 1

        while queue:

                current = queue.pop(0)

                if current.is_goal:
                        return SearchResult(current, nodes_expanded, nodes_generated, max_frontier_size, current.cost)
                
                if current.cost >= self.depth_limit:
                        continue

                nodes_expanded += 1

                for neighbor in current.neighbors():
                        nodes_generated += 1
                        if neighbor not in visited or neighbor.cost < visited[neighbor]:
                                visited[neighbor] = neighbor.cost
                                queue.append(neighbor)

                max_frontier_size = max(max_frontier_size, len(queue))
        
        return SearchResult(None, nodes_expanded, nodes_generated, max_frontier_size)