import { useState, useEffect } from "react"
import axios from 'axios'

export default function App() {

 const [todos, setTodos] = useState([])

const getTodos = () => {
    axios
      .get('http://localhost:8000/api/')
      .then((res) => {
        setTodos(res.data)
      })
      .catch((error) => {
        console.error(error)
      })
  }
  useEffect(() => {
    getTodos()
  }, [])


  return (
    <div>
      <ul>
      {todos.map((todo) => (
        <li key={todo.id}>
          <h1>{todo.title}</h1>
          <p>{todo.body}</p>
        </li>
))}
      </ul>
      
    </div>
  )
}