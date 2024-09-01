import './App.css';

import React, { useState } from 'react';
import Nav from './Nav.js';
import ScoreDisplay from './ScoreDisplay.js';


function App() {
  
  
  
  const [inputValue, setInputValue] = useState('');

  const [qualityValue, setQuality] = useState(23);
  const [equityValue, setEquity] = useState(54);
  const [accessValue, setAccess] = useState(92);

  const [cumulativeValue, setCumulative] = useState(57);

  const [outputValue, setOutputValue] = useState('Your scores will appear here');
  const [error, setError] = useState('no Errors yet');

  const handleChange = (event) => {
    setInputValue(event.target.value);
  };

  const handleClick = (event) => {
    event.preventDefault(); // Prevent default form submission behavior

    var output;

    fetch('http://127.0.0.1:5000/transitscore', { // Replace with your server URL
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ data: {address: inputValue} }), // Send the input data
    })
      .then(response => {return response.json(); })
      .then(data => { 
        
        setOutputValue(data); 

        setQuality(data['quality']['result']);
        setEquity(data['equity']['result']);
        setAccess(data['access']['result']);


      })

    
      
  };
  


  return (
    
    <div className="App">
      <Nav />



      
      <header className="App-header">
        


        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          <ScoreDisplay targetPercentage={cumulativeValue} text={`cumulative: ${cumulativeValue}`}/>
          
        </div>

        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          <ScoreDisplay targetPercentage={qualityValue} text={`quality: ${qualityValue}`} />
          <ScoreDisplay targetPercentage={equityValue} text={`equity: ${equityValue}`} />
          <ScoreDisplay targetPercentage={accessValue} text={`access: ${accessValue}`} />
        </div>
                
        
        


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


      
        


      </header>
    </div>
  );
}









export default App;
