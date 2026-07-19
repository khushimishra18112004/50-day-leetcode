class Solution(object):
    def middleNode(self, head):
        curr=head
        count=0
        while curr is not None:
            count+=1
            curr=curr.next
        curr=head
        for i in range(0,count//2):
            curr=curr.next
        return curr   
        