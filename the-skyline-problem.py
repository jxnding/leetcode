class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # # return i, where target is strictly before i. -1 = after end
        # def findBar(target):
        #     nonlocal skyline
        #     if target < skyline[0][0]: return 0
        #     for i in range(0, len(skyline)-1):
        #         n1, n2 = skyline[i], skyline[i+1]
        #         if n1[0] <= target < n2[0]: #do we want to <= both?
        #             return i
        #     return -1 #be careful because -1 is a legal index 
        # Edge: empty input
        if buildings == None or buildings == []: return [[]]
        
        # Add first building
        skyline = [[buildings[0][0],buildings[0][2]], [buildings[0][1],0]]

        ## Add other buildings
        for i in range(1, len(buildings)):
            L, R, H = buildings[i]
            # 3 states: find L, eat, find R
            # state = 0
            addL, addR, delete = None, None, []
            # Find L
            curr_ind = 0
            for j, [x, curr_height] in enumerate(skyline):
                curr_ind = j
                if L <= x: #NOTE: needs to be sorted to find first one
                    if H > curr_height:
                        n1 = [L, H]
                        addL = (curr_ind, n1)
                    break
            else: # L is at the end
                addL = (curr_ind, [L, H])
                addR = (curr_ind, [R, 0])

            # Eat
            for j in range(curr_ind, len(skyline)-1):
                curr_ind = j
                x, curr_height = skyline[j]
                if H >= curr_height:
                    delete.append(curr_ind)
                # Find R
                if R >= x: #NOTE: what if it is the end?, -1
                    if H >= curr_height: #we might have deleted the current
                        addR = (curr_ind, [R, H])
                    break
            else: # R is at the end
                addR = (curr_ind, [R, 0])
            
            # Do the operations
            if addR: skyline.insert(addR[0], addR[1])
            delete.reverse() #delete from back to preserve indices
            for d in delete:
                del skyline[d]
            if addL: skyline.insert(addL[0], addL[1])

        return skyline















        # Other buildings
        for i in range(1, len(buildings)):
            l, r, h = buildings[i]
            # Left
            location = findBar(l)
            # Edge: building at end
            if location == -1:
                skyline += [[l,h], [r,0]]
                continue
            curr_height = skyline[location][1]
            ## Now the building will affect skyline
            # Edge: building too short ???
            if h <= curr_height:
                n1 = None
            else:
                n1 = [l, h]
            ###### location_end = findBar(r) doesn't matter
            # Edge: building ends before next
            if r < skyline[location][0]:
                n2 = [r, curr_height]
                if not n1:
                    print("ERROR")
                else:
                    skyline.insert(location, n2)
                    skyline.insert(location, n1)
                continue
            delete = []
            # find endpoint, loop through 
            for j in range(location+1, len(skyline)):
                curr_x, curr_height = skyline[j][0], skyline[j][1]
                if r < curr_x: #we ended
                    if h > curr_height: n2 = [r, curr_height]
                    else: n2 = None
                    break
                if h >= curr_height: #delete current
                    delete.append(j)
                # else: #keep goingx
            else: #beyond the end
                n2 = [r, 0]
            # Delete
            for j in range(len(skyline)-1, -1, -1):
                if j in delete: del skyline[j]
            # Add n1, n2
            if n1:
                skyline.insert(location, n1)
            location_post_delete = findBar(r)
            if n2:
                if location_post_delete == -1: skyline.append(n2)
                else: skyline.insert(location_post_delete, n2)
            
        return skyline