import './App.css';

import React, { useState } from 'react';
import Nav from './Nav.js';
import ScoreDisplay from './ScoreDisplay.js';

const logo = '/bus-logo.png';

const red = '#FF0000';   // Hex code for red
const yellow = '#FFFF00';  // Hex code for yellow
const orange = '#FFA500';  // Hex code for orange

const green = '#00FF00'; // Hex code for green
const white = '#FFFFFF'; // Hex code for white

const defaultAddress = '21426 E Lost Lake Road, Snohomish, WA 98296';


function App() {
  
  const [showScores, setShowScores] = useState(false);
  
  const [inputtedAddress, setInputValue] = useState('');
  

  const [qualityValue, setQuality] = useState(23);
  const [needValue, setEquity] = useState(54);
  const [accessValue, setAccess] = useState(92);

  const [cumulativeValue, setCumulative] = useState(57);

  const [loading, setLoading] = useState(false);
  

  const [outputValue, setOutputValue] = useState('Your scores will appear here');
  const [error, setError] = useState('no Errors yet');

  const handleChange = (event) => {
    setInputValue(event.target.value);
  };


  const rateColor = (rating) => {
    if (rating <= 25) {
      return red; // Bad (0-25)
    } else if (rating <= 50) {
      return orange; // Medium-bad (26-50)
    } else if (rating <= 75) {
      return yellow; // Medium-good (51-75)
    } else {
      return green; // Good (76-100)
    }
  }

  const handleScoreClick = (event) => {
    event.preventDefault(); // Prevent default form submission behavior

    var output;


    fetch('http://50.46.51.158:4000/transitscore', { // Replace with your server URL
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ data: {
        address: inputtedAddress === '' ? defaultAddress : inputtedAddress
      } }), // Send the input data
     
    })
      .then(response => {return response.json(); })
      .then(data => { 
        
        console.log(data);

        setOutputValue(data); 

        setEquity(data['equity']['result']);
        setAccess(data['access']['result']);
        setCumulative(data['cumulative'])
        setShowScores(true);
        setLoading(false);
      })

      setLoading(true);

    
      
  };

  const handleAddressClick = (event) => {
    event.preventDefault(); // Prevent default form submission behavior
    // Reboot the whole page
    window.location.reload();
  }
  


  return (
    
    <div className="App">
      <Nav />



      
      <header className="App-header">
        

        <div>


        {showScores &&(
          <div>
            
            <p>Transit Equity Scores for </p>

            <p>{inputtedAddress}</p>

            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', paddingTop: '20px'}}>
              <ScoreDisplay targetPercentage={needValue+1} diameter={200} text={`need`} color={rateColor(-1 * needValue)} number={needValue} />

              <ScoreDisplay targetPercentage={cumulativeValue+1} diameter={250} text={`cumulative`} color={rateColor(cumulativeValue)} number={cumulativeValue} />

              <ScoreDisplay targetPercentage={accessValue+1} diameter={200} text={`access`} color={rateColor(accessValue)} number={accessValue} />

            </div>
            <div style={{paddingTop:'20px'}}>
              <button onClick={handleAddressClick}>Try again</button>

            </div>
          
          </div>
      
        )}
                
        {loading && (
          <div>
            <img src={logo} className="App-logo" alt="logo" />
            <p>
              Loading...
            </p>
          </div>

        )}

        {!showScores && !loading && (
          
          <div>
            <h1>Enter your address below</h1>
            
            <input 
            type="text" 
            value={inputtedAddress} 
            onChange={handleChange} 
            
            placeholder='21426 E Lost Lake Road, Snohomish, WA 98296'


            />

            <div style={{paddingTop:'20px'}}>
              <button onClick={handleScoreClick}>
                
                  Find your Score
              </button>
            </div>
          </div>

        )}
        


          

        </div>
        

      
        


      </header>
    </div>
  );
}









export default App;
