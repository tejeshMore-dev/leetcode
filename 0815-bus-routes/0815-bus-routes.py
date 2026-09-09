class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        SOURCE = source
        TARGET = target

        if SOURCE == TARGET:
            return 0
            
        bus_map = defaultdict(list) # stop : [ buses... ]
        queue = deque([])
        visited_buses = set()
        visited_stops = set()

        for bus, stops in enumerate(routes):
            for stop in stops:
                bus_map[stop].append(bus)
                
                if stop == SOURCE:
                    queue.append(( stop, 0 )) # stop, bus, min_buses
                    visited_stops.add(stop)
                
        while queue:
            stop, min_buses = queue.popleft()

            if stop == TARGET:
                return min_buses
            
            for new_bus in bus_map[stop]:
                if new_bus in visited_buses:
                    continue
                
                visited_buses.add(new_bus)

                for new_stop in routes[new_bus]:
                    if new_stop in visited_stops:
                        continue
                    
                    visited_stops.add(new_stop)
                    queue.append(( new_stop, min_buses + 1 ))
        
        return -1

        '''
        Requirements:
        intially not in bus
        source --> target

        return least number of buses
        
        thought:
        - create a graph
            - everynode belong to multiple buses
            stop : [bus 0 , bus 1]

        - explore all buses with that has source stop (queue (stop, buses) )
        - try finding target
        - queue new unique buses available, buses + 1
        - skip if visited
        - return buses if reached target, BFS ensures minimum

        spent ~ 12 min
        starting coding now
        '''


