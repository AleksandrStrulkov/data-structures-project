"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import Node, Stack


class TestStack(unittest.TestCase):

    def test_Node(self):
        node1 = Node('data1', None)
        node2 = Node('data2', node1)
        self.assertEquals(node1.data, 'data1')
        self.assertEquals(node1.next_node, None)
        self.assertEquals(node2.data, 'data2')
        self.assertEquals(node2.next_node, node1)

    def test_Stack_push(self):
        stack = Stack()
        stack.push('data1')
        self.assertEquals(stack.top.data, 'data1')
        stack.push('data2')
        self.assertEquals(stack.top.data, 'data2')
        stack.push('data3')
        self.assertEquals(stack.top.data, 'data3')

    def test_stack_pop(self):
        stack = Stack()
        stack.push('data1')
        stack.pop()
        self.assertEquals(stack.top, None)
        stack.push('data1')
        stack.push('data2')
        self.assertEquals(stack.top.data, 'data2')
        self.assertEquals(stack.top.next_node.data, 'data1')
        stack.pop()
        self.assertEquals(stack.top.data, 'data1')
        self.assertEquals(stack.top.next_node, None)

    def test_str(self):
        test_assert = Stack()
        self.assertEquals(str(test_assert.top), "None")
        test_assert.push("1")
        self.assertEquals(str(test_assert.top.data), "1")
        test_assert.push("1")
        self.assertEquals(str(test_assert.top.next_node.data), "1")

if __name__ == "__main__":
    unittest.main()