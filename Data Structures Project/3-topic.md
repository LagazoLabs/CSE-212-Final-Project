# Binary Search Trees

## Introduction
Binary Search Trees are a complex structure of data. A Binary Search Tree, much like the name implies, structures data into a *tree* like format. Binary Search Trees sort data based off their value. An easy way to have a better understanding of it is if you compare it to family trees.

![family-tree-example](images/topic3-1.png)

As you can see, the **Child** is linked to two **Parents**, and where as the **Parents** will be linked to **Grandparents**. In terms of Binary Search Trees, **nodes** of data are connected to other parts of data. The **Parent Node**, which is the primary node that will be used to sort the data and connect to what are known as **Sub-Trees** or for a better understanding, **Child-Trees**. Data that is smaller than the **Parent Tree** is sorted to the left **Child Tree**, while data larger than the **Parent Tree** will be sorted to the right **Child Tree**. 

![bst-example](images/topic3-2.jpeg)

## Why Trees Are Used
As discussed in our section about [Queues](1-topic.md) and [Linked Lists](2-topic.md), one reason could be efficiency and performance. However, in terms of efficiency, Binary Search Trees are rather unique in this case.

They are faster than arrays, as arrays when inserting, deleting, or accessing have a big-O-notation of o(n), which is where performance is affected by the size of data. However, Binary Search Trees when they are inserting, deleting, or accessing have a big-O-notation of o(log(n)), which is also affected by the size of data, yet faster. Shockingly, these are not as fast as [Queues](1-topic.md) or [Linked List](2-topic.md), as when they are deleting or inserting, they have a big-O-notation of o(1), which is where the size of the data does not even matter. 

![big_o_notation](images/big_o_notation_graph.png)

[Source](https://www.bigocheatsheet.com)

So what gives? If it is not the most efficient method of storing data, why bother? Well, it is trust it is important to consider efficiency, you also have to keep in the mind the situation, mostly in scenarios where you may need to search for a specific value in a large quantity of data. As explained in **Introduction**, a Binary Search Tree with have a **Parent Node**, which will sort values smaller to the **Child Note** node and larger value to the right **Child Node**. Effectively, the work load will thus be cut in half, as the program will only need to search one side, not the other, as opposed to arrays which has to search from start to end.

## Creating a Tree
Trees are implemented used a class. 

```Python
class BinarySearchTree:
       
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
```

## Adding Items to a Tree

```Python
    def add_node(self, data):
        if data == self.data:
            return 

        if data < self.data:
            if self.left_child:
                self.left_child.add_node(data)
            else:
                self.left_child = BinarySearchTree(data)
             
        else:
            if self.right_child:
                self.right_child.add_node(data)
            else:
                self.right_child = BinarySearchTree(data)
```

## Finding Items in a Tree

As stated before, searching for items in a Binary Search Tree are much more efficient than regular old arrays as it cuts the workload in half by only checking one side. 

```Python
    def find_node(self, value):
          
        # First it will check if the parent node is the value we are looking for.
        if self.data == value:
            # If it is, it will return True.
            return True
        
        # If not, it will see if the value is smaller than the parent,
        # and if it is, it will only check the left side.
        if value < self.data:
            if self.left_child:
                return self.left_child.find_node(value)
            else:
                return False
        # If not, it will see if the value is larger than the parent,
        # and if it is, it will only check the right side.
        if value > self.data:
            if self.right_child:
                return self.right_child.find_node(value)
            else:
                return False
```

## Practice
