import React from 'react'
import {Link} from 'react-router-dom'

const AuthorItem = ({author}) => {
return (
        <tr>
            <td><Link to={`/users/${author.id}`}>{author.id}</Link></td>
            <td>{author.first_name}</td>
            <td>{author.last_name}</td>
            <td>{author.birthday_year}</td>
        </tr>
    )
}
const AuthorList = ({items}) => {
    return (
        <table>
            <th>
                Id
            </th>
            <th>
                First name
            </th>
            <th>
                Last Name
            </th>
            <th>
                Birthday year
            </th>
            {items.map((author) => <AuthorItem author={author} />)}
        </table>)
}


export default AuthorList