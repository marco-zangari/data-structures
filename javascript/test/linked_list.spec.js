'use strict'

let linkedList = require('../linked_list')
let chai = require('chai')
let expect = chai.expect
let assert = chai.assert

describe('linked_list.js tests', function(){
  it('test for linked list node', function(){
    let ll = new linkedList.LinkedList()
    expect(ll.head).to.equal(null)
  })
  it('test for linked list node empty', function(){
    let ll = new linkedList.LinkedList()
    expect(ll.head).is.null
  })
  it('test linked list push method', function(){
    let ll = new linkedList.LinkedList()
    ll.push(1)
    expect(ll.head.data).to.equal(1)
  })
  it('test linked list pop method', function(){
    let ll = new linkedList.LinkedList()
    ll.push(1)
    ll.pop()
    expect(ll.head).is.null
  })
  it('test linked list size', function(){
    let ll = new linkedList.LinkedList()
    ll.push(1)
    expect(ll.size()).to.equal(1)
  })
  it('test linked list search number in list', function(){
    let ll = new linkedList.LinkedList()
    for(let i = 0; i < 25; i++){
      ll.push(i)
    }
    let output = ll.search(5)
    expect(output.data).to.equal(5)
  })
  it('test linked list search for number not in list', function(){
    let ll = new linkedList.LinkedList()
    for(let i = 0; i < 25; i++){
      ll.push(i)
    }
    let output = ll.search(50)
    expect(output.data).to.not.equal(50)
  })
  it('test linked list display', function(){
    let ll = new linkedList.LinkedList()
    for(let i = 0; i < 5; i++){
      ll.push(i)
    }
    let output = ll.display()
    expect(output.data).to.equal('(4, 3, 2, 1, 0)')
  })
})
