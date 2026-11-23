import heapq
from puzzle.base_search import BaseSearch
from puzzle.state import State
from puzzle.state import GOAL_STATE
from puzzle.result import SearchResult

DEFAULT_DEPTH_LIMIT = 50

class AStar(BaseSearch):

    def __init__(self, depth_limit: int = DEFAULT_DEPTH_LIMIT):
        self.depth_limit = depth_limit


    def heuristic(self, state: State) -> int:
        
        total = 0

        for index, tile in enumerate(state.tiles):
                if tile == 0:
                        continue
                
                row, col = divmod(index, 3)
                goal_index = GOAL_STATE.index(tile)
                goal_row, goal_col = divmod(goal_index, 3)
                total += abs(row - goal_row) + abs(col - goal_col)
        
        return total


    def search(self, initial: State) -> SearchResult:

        queue = []
        best_cost = {initial: 0}

        nodes_expanded = 0
        nodes_generated = 0
        max_frontier_size = 1


        queue.append(initial)

        while queue:

                new_current = queue[0]

                for state in queue:
                        if (self.heuristic(state) + state.cost) < (self.heuristic(new_current) + new_current.cost):
                                new_current = state

                current = new_current
                queue.remove(current)

                if current.is_goal:
                        return SearchResult(current, nodes_expanded, nodes_generated, max_frontier_size, current.cost)
                
                if current.cost >= self.depth_limit:
                        continue

                nodes_expanded += 1

                for neighbor in current.neighbors():
                        nodes_generated += 1
                        if neighbor not in best_cost or neighbor.cost < best_cost[neighbor]:
                                if neighbor in queue:
                                        queue.remove(neighbor)
                                
                                best_cost[neighbor] = neighbor.cost
                                queue.append(neighbor)
                                
                max_frontier_size = max(max_frontier_size, len(queue))

        return SearchResult(None, nodes_expanded, nodes_generated, max_frontier_size)
