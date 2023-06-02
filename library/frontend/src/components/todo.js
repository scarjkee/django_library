import React from 'react'
import { useParams } from 'react-router-dom'

const TodoItem = ({item}) => {
    return (
        <tr>
            <td>
                {item.project_name_todo}
            </td>
            <td>
                {item.create_user}
            </td>
            <td>
                {item.time_update}
            </td>
            <td>
                {item.status_notes}
            </td>
        </tr>
    )
}

const TodoList = ({items}) => {
    let { id } = useParams();
    let filtered_items = items.filter((item) => item.author.id == id)
    return (
        <table>
            <th>
                Project
            </th>
            <th>
                Create User
            </th>
            <th>
                Update
            </th>
            <th>
                Status
            </th>
            {filtered_items.map((item) => <TodoItem item={item} />)}
        </table>
    )
}
export default TodoList