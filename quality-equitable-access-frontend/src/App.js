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
        <button >
            Find your Score
        </button>
      </div>

      <div>
          <p>{outputValue}</p>
        </div>

      
        


      </header>
    </div>
  );
}

export default App;
