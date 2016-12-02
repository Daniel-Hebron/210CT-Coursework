class BinTreeNode(object):
 
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None
 
def tree_insert( tree, item):
    if tree==None:
        tree=BinTreeNode(item)
    else:
        if(item < tree.value):
            if(tree.left==None):
                tree.left=BinTreeNode(item)
            else:
                tree_insert(tree.left,item)
        else:
            if(tree.right==None):
                tree.right=BinTreeNode(item)
            else:
                tree_insert(tree.right,item)
    return tree
 
def postorder(tree):
    if(tree.left!=None):
        postorder(tree.left)
    if(tree.right!=None):
        postorder(tree.right)
    print (tree.value)
 
 
def in_order(tree):
    stack = [tree]
    visited = []

    while (stack!=[]):
        if tree.left != None and tree.left not in visited: #Checks if there is smaller element that hasnt been in visited
            stack.append(tree.left)
            tree = tree.left
        else:
            visited.append(tree)
            if tree.right != None and tree.right not in visited: #Checks if theres element on the right that is not in visited
                stack.append(tree.right)
                del stack[len(stack)-2] #deletes the element in stack 1 before last because it is unneeded
            else:
                del stack[len(stack)-1]

            try:
                tree = stack[len(stack)-1]
            except:
                pass

    for i in range(0,len(visited)): #printing list
        print(visited[i].value) #have to have .value otherwise it will print locations

                
     
if __name__ == '__main__':
   
  t=tree_insert(None,6);
  tree_insert(t,10)
  tree_insert(t,5)
  tree_insert(t,2)
  tree_insert(t,3)
  tree_insert(t,4)
  tree_insert(t,11)
  in_order(t)
