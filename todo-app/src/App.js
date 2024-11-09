import React, { Component } from "react"
import TodoItem from "./TodoItem"
import todosData from "./todosData"

class App extends Component {
  constructor() {
    super()
    this.state = {
      todos: todosData
    }
    this.handleChange = this.handleChange.bind(this)
  }

  handleChange(id) {
    this.setState(prevState => {
      const updatedTodos = prevState.todos.map(todo => {
        if (todo.id === id) {
          return {
            ...todo,
            completed: !todo.completed
          }
        }
        return todo
      })
      return {
        todos: updatedTodos
      }
    })
  }

  render() {
    const todoItems = this.state.todos.map(item => <TodoItem key={item.id} item={item} handleChange={this.handleChange}/>)
    
    return (
      <div className="todo-list d-flex flex-column align-items-center justify-content-center vh-100">
        <div className="todo-item list-group">
          {todoItems}
        </div>
      </div>
    )
  }
  
}

export default App
