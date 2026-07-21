class Solution(object):
    def hasCycle(self, head):
        temp=head
        my_set=set()
        while temp is not None:
            if temp in my_set:
                return True
            my_set.add(temp)  
            temp=temp.next
        return False   