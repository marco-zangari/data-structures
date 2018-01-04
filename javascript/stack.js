'use strict'

const LinkedList = require ('./linked_list')

class Stack {
    constructor(iterable=null){
        this.func = new linkedlist.LinkedList()
        if(Array.isArray(iterable)){
            iterable.map(x => this.push(x));
        }
    }

push(val){
    return this.func.push(val)
}

pop(){
    return this.func.pop()
}

size(){
    return this.func.size()
}

}

module.exports = Stack