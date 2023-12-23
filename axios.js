const axios = require('axios');

// Example: Sending data to make predictions
axios.post('http://your-python-backend/predict', { data: yourData })
    .then(response => {
        console.log('Prediction:', response.data.result);
        // Update UI based on prediction results
    })
    .catch(error => {
        console.error('Error:', error);
    });
