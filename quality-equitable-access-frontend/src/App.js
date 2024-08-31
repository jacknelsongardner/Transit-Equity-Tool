import './App.css';

import React, { useState } from 'react';




function App() {
  
  
  
  const [inputValue, setInputValue] = useState('');

  const handleChange = (event) => {
    setInputValue(event.target.value);
  };
  
  return (
    <div className="App">
      <header className="App-header">
        <img src={'busLogo.png'} className="App-logo" alt="logo" />
        
        
        
        <p>
          Enter your address below to get your QEA score
        </p>


        <input 
        type="text" 
        value={inputValue} 
        onChange={handleChange} 
        placeholder="Enter text here" 


      />
        <p>You typed: {inputValue}</p>



      </header>
    </div>
  );
}

export default App;
