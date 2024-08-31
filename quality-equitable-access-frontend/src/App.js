import './App.css';

import React, { useState } from 'react';




function App() {
  
  
  
  const [inputValue, setInputValue] = useState('');
  const [outputValue, setOutputValue] = useState('Your scores will appear here');


  const handleChange = (event) => {
    setInputValue(event.target.value);
  };
  
  return (
    <div className="App">
      <header className="App-header">
        <div>
          <p>{outputValue}</p>
        </div>
        
        
        <p>
          Enter your address below to get your QEA score
        </p>


        <input 
        type="text" 
        value={inputValue} 
        onChange={handleChange} 
        placeholder="Enter text here" 


      />
      <div style={{paddingTop:'20px'}}>
        <button >
            Find your Score
        </button>
      </div>

      
        


      </header>
    </div>
  );
}

export default App;
