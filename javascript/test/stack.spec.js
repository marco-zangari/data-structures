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
})
