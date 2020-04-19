class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        # P order numbers from 1 to m
        # just replace each querie to the correct key as a dict
        d = dict()
        res = []
        for position in queries:
            # test
            if position in d.keys():
                # use the value on dict to add value on res
                res.append(d[position])
            else:
                val = position - 1
                # add on dict
                d[position] = val
                d[val] = position
                # add position - 1 on res
                res.append(val)
        print(d)
        return res