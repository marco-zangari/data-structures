'use strict'

let Stack = require('../stack')
let chai = require('chai')
let expect = chai.expect

describe('stack.js tests', function() {
  it('stack exists', function(){
    let stack = new Stack()
    expect(stack.size()).to.equal(0)
  })
  it('test push and pop', function(){
    let stack = new Stack()
    stack.push('one')
    stack.push('two')
    expect(stack.pop()).is.equal('two')
  })
  it('test size method', function(){
    let stack = new Stack()
    stack.push('one')
    stack.push('two')
    expect(stack.size()).is.equal(2)
  })
  it('test error message for popping an empty stack', function(){
    let stack = new Stack()
    expect(stack.pop()).is.equal('Cannot pop from an empty list.')
  })
  it('test push multiple values, pops stack top', function(){
    let stack = new Stack
    for(let i = 0; i < 100; i++){
    stack.push(i)
    }
    let output = stack.pop()
    expect(output).is.equal(99)
  })
  it('test push multiple values, size after pop', function(){
    let stack = new Stack
    for(let i = 0; i < 100; i++){
    stack.push(i)
    }
    let output = stack.pop()
    expect(stack.size()).is.equal(99)
  })
})
