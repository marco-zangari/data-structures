'use strict'

let Q = require('../que')
let chai = require('chai')
let expect = chai.expect

describe('que.js tests', function(){
  it('test for empty que with null value', function(){
    let q = new Q()
    expect(q.peek()).to.equal(null)
  })
})
