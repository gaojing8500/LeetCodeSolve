from Python.DataStructureAlgorithom.base_node_type_data_structure import ListNode


class AddNumberSum(object):
    def add_number_sum(self, l1, l2):
        pre = ListNode(0)
        cur = pre
        carry = 0
        while l1 != None or l2 != None:
            x = l1.val if l1 != None else 0
            y = l2.val if l2 != None else 0
            tmp_sum = x + y + carry

            carry = tmp_sum / 10
            tmp_sum = tmp_sum % 10
            cur.next = ListNode(tmp_sum)

            cur = cur.next
            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next

        if carry == 1:
            cur.next = ListNode(carry)

        return pre.next
