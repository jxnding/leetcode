import math
import statistics
import pdb

class Solution:
    def split(self, a):
        if len(a)%2==0:
            a0 = a[0:int(len(a)/2)]
            a1 = a[int(len(a)/2):len(a)]
            return a0, a1, []
        else:
            a0 = a[0:math.floor(len(a)/2)]
            a1 = a[math.ceil(len(a)/2):len(a)]
            ac = a[math.floor(len(a)/2)]
            return a0, a1, [ac]

    def findMedianSortedArrays(self, nums1, nums2):
        done = False
        a = nums1
        b = nums2
        while not done:
            if len(b)>len(a):
                c = b
                b = a
                a = c
            if len(b)==0:
                return float(statistics.median(a))
            if len(b)==1 and len(a)==1:
                # print('www')
                return float((b[0]+a[0])/2)
            if len(b)==1:
                a0,a1,ac = self.split(a)
                if a0[len(a0)-1]>=b[0]:
                    a = a0+ac+a1[0:len(a1)-1]
                    b = []
                elif a1[0]<=b[0]:
                    a = a0[1:len(a0)]+ac+a1
                    b = []
                else:
                    a = ac
                continue



            # Splitting
            a0,a1,ac = self.split(a)
            b0,b1,bc = self.split(b)

            # Comparing
            # pdb.set_trace()
            if a0[len(a0)-1]<=b0[len(b0)-1] and a1[0]<=b1[0]:
                a = a0[len(b0):]+ac+a1
                b = b0+bc
            elif a0[len(a0)-1]>=b0[len(b0)-1] and a1[0]>=b1[0]:
                a = a0+ac+a1[:-len(b1)]
                b = bc+b1
            elif a0[len(a0)-1]>=b0[len(b0)-1] and a1[0]<=b1[0]: #throw away b0, b1
                # a = a0+a1
                b = bc
            elif a0[len(a0)-1]<=b0[len(b0)-1] and a1[0]>=b1[0]: #throw away a0, a1
                a = ac
                # b = bc
            else:
                print("wtf")

a = [2,3]
b = [1,4,5]
bb = Solution()
ans = bb.findMedianSortedArrays(a,b)
print(ans)
