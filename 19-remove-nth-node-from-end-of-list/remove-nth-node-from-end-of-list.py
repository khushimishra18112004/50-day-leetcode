class Solution(object):
    def removeNthFromEnd(self, head, n):
        length=0
        temp=head
        while temp is not None:
            length+=1
            temp=temp.next
        if length==n:
            new_node=head.next
            del head
            return new_node
        position=length-n
        temp=head
        count=1
        while count<position:
                temp=temp.next
                count+=1
        temp.next=temp.next.next
        return head           