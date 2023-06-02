import './App.css';
import React from 'react';
import {BrowserRouter, Link, Route, Switch} from "react-router-dom";
import axios from 'axios';
import AuthorList from "./components/Author.js";
import TodoList from "./components/todo.js";



class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'authors': [],
            'todos':[]
            // 'project':[]
        }
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/authors/')
            .then(response => {
                const authors = response.data
                this.setState(
                    {
                        'authors': authors
                    }
                )
            }).catch(error => console.log(error))
        axios.get('http://127.0.0.1:8000/api/Todo/')
            .then(response => {
                const todo = response.data
                this.setState(
                    {
                        'todos': todo
                    }
                )
            }).catch(error => console.log(error))
    }



    render() {
        return (
            <div className='App'>
                <BrowserRouter>
                    <nav>
                        <ul>
                            <li>
                                <Link to='/users'>Authors</Link>
                            </li>
                            <li>
                                <Link to='/Todo'>Books</Link>
                            </li>
                        </ul>
                    </nav>
                    <Switch>
                        <Route exact path='/todo' component={() => <TodoList items={this.state.todos} />} />
                        <Route exact path='/users' component={() => <AuthorList authors={this.state.authors} />} />
                    </Switch>
            </BrowserRouter>
            </div>

        )
    }
    }
    export default App;