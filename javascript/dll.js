'use strict'

class Node {
  constructor(data=null, next=null, prev=null){
    this.data = data
    this.next = next
    this.prev = prev
  }
}

class DoublyLinkedList {
  contructor(){
    this.head = null
    this.tail = null
    this._size = 0
  }
  push(val){
    let new_node = new Node(val)
    if(this._size === 0){
      this.head = new_node
      this.tail = new_node
      this._size ++
    }
    else{
      new_node.next = this.head
      this.head.prev = new_node
      this.head = new_node
      this._size ++
    }
  }
  append(val){
    let new_node = new Node(val)
    if(this._size === 0){
      this.head = new_node
      this.tail = new_node
      this._size ++
    }
    else{
      new_node.prev = this.tail
      this.tail.next = new_node
      this.tail = new_node
      this._size ++
    }
  }
  pop(){
    let curr = this.head
    if(this.head === null){
      return 'Cannot pop from empty list'
    }
    else if(this._size > 1){
      this.head = curr.next
      this.head.prev = null
      this._size --
    }
    else if(this._size === 1){
      this.head = null
      this.tail = null
      this._size --
    }
    return curr.data
  }
  shift(val){
    let curr = this.tail
    if(this.tail === null){
      return 'Cannot shift from an empty list'
    }
    else if(this._size === 1){
      this.tail = null
      this.head = null
      this._size --
    }
    else if(this._size > 1){
      this.tail = curr.prev
      this.tail.next = null
      this._size --
    }
  }
}
module.exports = {DoublyLinkedList, Node}
