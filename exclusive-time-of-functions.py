class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        functions = [0]*n
        current = []
        for log in logs:
            log = log.split(':')
            f_id, start, time = int(log[0]), log[1]=='start', int(log[2]) #TODO int id
            if start:
                if current==[]:
                    current.append((f_id,time,0)) #id, start, previous total
                else:
                    p_id, p_time, p_total = current.pop()
                    current.append( (p_id, '', p_total+(time-p_time)) )
                    current.append( (f_id, time, 0) )
            else:
                _, p_time, p_total = current.pop()
                functions[f_id] += time-p_time+1+p_total
                if len(current)>0:
                    p_id, p_time, p_total = current.pop()
                    current.append( (p_id, time+1, p_total) )
        return functions
#### O(n), O(n); 52, 100 Python3
#### Very tedious -- not thinking clearly! 