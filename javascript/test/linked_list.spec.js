'use strict'

let linkedList = require('../linked_list')
let chai = require('chai')
let expect = chai.expect
let assert = chai.assert

describe(linked_list.js tests, function(){
  it('test for linked list node', function(){
    ll = linkedList.LinkedList()
    expect(ll.head).to.be.null
  })

})
