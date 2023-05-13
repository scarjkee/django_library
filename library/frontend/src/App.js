import React from 'react';
import logo from './logo.svg';
import './App.css';
import AuthorList from './components/Author.js';
import axios from 'axios';

class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'authors': []
        }
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/authors')
            .then(response => {
                const authors = response.data
                this.setState(
                    {
                        'authors': authors
                    }
                )
            }).catch(error => console.log(error))
    }

    render() {
        return (
            <>
                <div className="wrapper">
                <header className="header">
                    <div className="navbar-wrapp">
                        <nav className="navbar">
                            <div className="container">
                                <a href="https://nodejsdev.ru/" className="main-navbar">NodeJs</a>
                                <ul className="navbar-menu">
                                    <li><a href="#">Главная</a></li>
                                    <li><a href="#">User</a></li>
                                    <li><a href="#">#</a></li>
                                </ul>
                            </div>
                        </nav>
                    </div>
                </header>
                <main className="main">
                    <div className="main-text">
                        <AuthorList authors={this.state.authors} />
                    </div>
                </main>
                <footer className="main-foot">
                    <div className="footer">
                        <div className="container">
                            <div className="footer_top">
                                <h3 className="taxt mainh3">Django REACT Frame-work</h3>
                                <p className="text text_footer"></p>
                                <div className="botton_footer">
                                    <a href="#" className="top_botton_footer"></a>
                                </div>
                            </div>
                            <div className="reserved">
                                    <p className="text reserved__text">2023 All rights reserved.</p>
                            </div>
                        </div>
                    </div>
                </footer>
            </div>
            </>
        )
    }
    }
    export default App;