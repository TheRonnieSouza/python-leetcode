#https://leetcode.com/problems/reverse-linked-list/
#https://neetcode.io/solutions/reverse-linked-list
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class SolutionReverseLinkedList:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None          # ponteiro para o nó anterior (começa vazio: a cauda da lista invertida apontará para None)
        curr = head          # ponteiro para o nó atual que estamos processando (começa na cabeça original)

        while curr:          # percorre enquanto houver nó atual
            nxt = curr.next  # guarda o próximo nó (porque vamos mudar curr.next)
            curr.next = prev # inverte a seta do nó atual: ao invés de apontar para nxt, passa a apontar para prev
            prev = curr      # avança prev: agora prev vira o nó atual (parte já invertida cresce)
            curr = nxt       # avança curr para o próximo nó original (que tínhamos salvo em nxt)

        return prev          # quando curr é None, prev está na nova cabeça (lista totalmente invertida)