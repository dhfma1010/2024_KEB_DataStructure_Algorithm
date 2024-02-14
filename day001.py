class Node :
    def __init__(self) :
        self.data = None
        self.link = None


def printNodes(start) :

        current = start

    if current is None :
        return
        print(current.data, end = ' ')

        current = current.link # 다음 다음 으로 이동
        print(current.data, end=' ')
    print()

def insertNode(findData, insertData) :
	global memory, head, current, pre

	if head.data == findData :      # 첫 번째 노드 삽입
		node = Node()
		node.data = insertData
		node.link = head
		head = node
		return

	current = head
	while current.link != None :    # 중간 노드 삽입
		pre = current
		current = current.link
		if current.data == findData :
			node = Node()
			node.data = insertData
			node.link = current
			pre.link = node
			return

	node = Node()                   # 마지막 노드 삽입
	node.data = insertData
	current.link = node


head, current, pre = None, None, None
dataArray = ["다현", "정연", "쯔위", "사나", "지효"]

## 메인 코드 부분 ##
if __name__ == "__main__" :

node = Node()
node.data = dataArray[0]
head = node


for data in dataArray[1:]:
pre = node
node = Node()
node.data = data
pre.link = node


printNodes(head)
