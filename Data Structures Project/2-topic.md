# Linked List

## Introduction
A link list is a data structure that is utilized to organize data. Unlike arrays, values in a linked list are not guranted to be next to eachother. There are pointers that will direct the code to the location of the next value. In this case, a location of a value is refered to as a node.

## Why Linked List Are Used
Some may be asking why we don't just use a regular array, wouldn't it be more simplier that way? Why yes, it may be the more simple solution, but it will not always be the most efficient. Linked list have a big-O-notation of o(1) when it comes to insertions and deletions (meaning the size of the linked list will not matter towards performance), while arrays will have a big-O-notation of o(n) (which *will* be dependent on the array size).
![big_o_notation](images/big_o_notation_graph.png)
[Source](https://www.bigocheatsheet.com)

## Creating Linked List
As stated before, each element, or each **node** will be *linked* together using **pointers.** These pointers will connect and point a program from one node to the next. The first node is often refered to as the head, while the end is the tail.

## Adding Items to a Linked List
There are various ways to add items to a linked list, and all it depends is if you are removing from the head/tail, or the middle.

**NOTE: THE IMAGES ARE ONLY PLACEHOLDERS (UNLESS WE ARE ALLOWED TO USE THEM)**

![inserting_into_head](https://byui-cse.github.io/cse212-course/lesson07/linked_list_insert_head.jpeg) 
In order insert into the head, we will need to set the current head as the second next value.

![insert_into_middle](https://byui-cse.github.io/cse212-course/lesson07/linked_list_insert_middle.jpeg)
In order to insert into the middle, the nodes will need to be rearranged. Such as inserting 5 into 1,2,3,4,6,8,10, inserting 5 after 4 will require "5" to be programmed as the new previous of 6, and 4 the new previous of 4, and 5 the new next of 4. 

## Removing Items from a Linked List
There are various ways to remove items to a linked list, and all it depends is if you are removing from the head/tail, or the middle.

**NOTE: THE IMAGES ARE ONLY PLACEHOLDERS (UNLESS WE ARE ALLOWED TO USE THEM)**
![removing_from_head](https://byui-cse.github.io/cse212-course/lesson07/linked_list_remove_head.jpeg)
In order insert into the head, we will need to set the current head as none, while the second node becomes the new node.

![removing_from_middle](https://byui-cse.github.io/cse212-course/lesson07/linked_list_remove_middle.jpeg)

## Practice