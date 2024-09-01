import './App.css';

import React, { useState } from 'react';
import Nav from './Nav.js';
import ScoreDisplay from './ScoreDisplay.js';


function App() {
  
  
  
  const [inputValue, setInputValue] = useState('');

  const [qualityValue, setQuality] = useState('');
  const [equityValue, setEquity] = useState('');
  const [accessValue, setAccess] = useState('');

  const [outputValue, setOutputValue] = useState('Your scores will appear here');
  const [error, setError] = useState('no Errors yet');

  const handleChange = (event) => {
    setInputValue(event.target.value);
  };

  const handleClick = (event) => {
    event.preventDefault(); // Prevent default form submission behavior

    fetch('http://127.0.0.1:5000/transitscore', { // Replace with your server URL
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ data: {address: inputValue} }), // Send the input data
    })
      .then(response => {return response.json();; })
      .then(data => {console.log(data); setOutputValue(data); })

      
  };
  
  return (
    
    <div className="App">
      <Nav />



      
      <header className="App-header">
        
        <div>
          <ScoreDisplay percentage={qualityValue} text={`quality: ${qualityValue}`}/>
          <ScoreDisplay percentage={equityValue} text={`equity: ${qualityValue}`}/>
          <ScoreDisplay percentage={accessValue} text={`access: ${qualityValue}`}/>

        </div>
        
        
        
        <p>
          Quality
        </p>

        <p>
          Equitable
        </p>

        <p>
          Access
        </p>


        <input 
        type="text" 
        value={inputValue} 
        onChange={handleChange} 
        
        placeholder="Enter your address here " 


      />

      <div style={{paddingTop:'20px'}}>
        <button onClick={handleClick}>
          
            Find your Score
        </button>
      </div>

      <div>
        <p>{JSON.stringify(outputValue)}</p>
      </div>

      
        


      </header>
    </div>
  );
}









export default App;
