// Example React component making an Axios request

import React, { useEffect, useState } from 'react';
import axios from 'axios';

const App = () => {
    const [messages, setMessages] = useState([]);

    useEffect(() => {
        axios.get('/api/messages')
            .then(response => setMessages(response.data))
            .catch(error => console.error('Error fetching messages:', error));
    }, []);

    return (
        <div>
            <ul>
                {messages.map((msg, index) => (
                    <li key={index}>{msg}</li>
                ))}
            </ul>
        </div>
    );
};

export default App;
