'use strict'

const dLL = require('../doubly_linked_list')

class Queue {
  constructor(iterable=null){
    this.func = new dLL.DoublyLinkedList()
    if(Array.isArray(iterable)){
      iterable.map(x=> this.enqueue(x))
    }
  }
  enqueue(val){
    return this.func.push(val)
  }
  dequeue(val){
    return this.func.shift()
  }
  peek(){
    if(this.func.tail){
      return this.func.tail.data
    }
    else {
      return null
    }
  }
  size(){
    return this.func._len
  }
}
