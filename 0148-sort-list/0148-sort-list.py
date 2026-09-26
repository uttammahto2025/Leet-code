class Solution:
    def sortList(self, head):
        if not head or not head.next: 
            return head
        a=[]; p=head
        while p: a.append(p.val); p=p.next
        a.sort(); p=head
        for x in a: p.val=x; p=p.next
        return head