import requests
import json
import pprint
import subprocess


class Node():
    """
    Node on the list
    """
    def __init__(self, data=None, nxt=None):
        self.data = data
        self.nxt= nxt
    def __repr__(self):
        return repr(self.data)

class LinkedList():
    """
    Implemented of the linked list
    """
    def __init__(self):
        self.head = None

    def __repr__(self):
        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.nxt
        return '[' + ','.join(nodes) +']'

    def append(self,data):
        """
        Adding a new node on the end of the linked list
        """
        if not self.head:
            self.head = Node(data=data)

        curr = self.head
        while curr.nxt:
            curr = curr.nxt
        curr.nxt = Node(data=data)
    def traverse(self):
        pass
r = requests.post('http://localhost:8000/rest_auth/login/',data={'username':'kirega','password':'allar'})

r = r.content.decode('utf-8')
r = json.loads(r)
print(r['key'])

q = requests.get('http://localhost:8000/adverts/list', headers={'Authorization':'Token ' + r['key']})
q = q.content.decode('utf-8')
q = json.loads(q)

l=[]

# Instance of linkedList
playlist = LinkedList()

for each in q :
    # print(each['upload'])
    l.append(each['upload'])
    playlist.append(each['upload'])
    m = each['upload']
