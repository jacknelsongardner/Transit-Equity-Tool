import './App.css';

import React, { useState } from 'react';
import Nav from './Nav.js';
import ScoreDisplay from './ScoreDisplay.js';

const loadingLogo = '/bus-logo.png';
const logo = '/equity.png';

const red = '#FF0000';   // Hex code for red
const yellow = '#FFFF00';  // Hex code for yellow
const orange = '#FFA500';  // Hex code for orange

const green = '#00FF00'; // Hex code for green
const white = '#FFFFFF'; // Hex code for white

const defaultAddress = '21426 E Lost Lake Road, Snohomish, WA 98296';


const transitNeedMessages = {
  high: 'your address has high need of public transit access',
  mid: 'your address has moderate need of public transit access',
  low: 'your address has low need of public transit access'
};

const transitAccessMessages = {
  high: 'your address has high acccess to public transit',
  mid: 'your address has moderate access to public transit',
  low: 'your address has low access to public transit'
};

const transitEquityMessages = {
  high: 'public transit exceeds the requirements for your address',
  mid: 'public transit meets the requirements for your address',
  low: 'public transit does not meet the requirements for your address'

}


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

  const rateText = (dictionary, rating) => {
    if (rating <= 33) {
      return dictionary.low; // Bad (0-25)
    } else if (rating <= 66) {
      return dictionary.mid; // Medium-good (51-75)
    } else {
      return dictionary.high; // Good (76-100)
    }
  }

  const handleScoreClick = (event) => {
    event.preventDefault(); // Prevent default form submission behavior

    var output;

    // in case an address was not inputted
    if (inputtedAddress == '')
    {
      setInputValue(defaultAddress); 
    }

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
      



      
      <header className="App-header">
        

        <div>


        {showScores &&(
          <div>
            
            <h2>Transit Equity Evaluation for </h2>
            <h1>{inputtedAddress}</h1>
            

            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', paddingTop: '20px'}}>
              <ScoreDisplay targetPercentage={needValue+1} diameter={20} text={`need`} color={rateColor(-1 * needValue)} number={needValue} />

              <ScoreDisplay targetPercentage={cumulativeValue+1} diameter={30} text={`equity`} color={rateColor(cumulativeValue)} number={cumulativeValue} />

              <ScoreDisplay targetPercentage={accessValue+1} diameter={20} text={`access`} color={rateColor(accessValue)} number={accessValue} />

            </div>

            <div style={{paddingTop:'20px'}}>
              <p>An <b>access</b> score of {accessValue} indicates that {rateText(transitAccessMessages, accessValue)} </p>
              <p>An <b>need</b> score of {needValue} indicates that {rateText(transitNeedMessages, needValue)} </p>
              <p>An <b>equity</b> score of {cumulativeValue} indicates that {rateText(transitEquityMessages, cumulativeValue)} </p>

              <button onClick={handleAddressClick}>Try again</button>

            </div>
          
          </div>
      
        )}
                
        {loading && (
          <div>
            <img src={loadingLogo} className="App-logo" alt="logo" />
            <h2>
              Loading...
            </h2>
          </div>

        )}

        {!showScores && !loading && (
          
          <div>

            <h1>Transit Equity</h1>
            <h2>Snohomish County</h2>
            <p>Evaluating Transit Service in Snohomish County by comparing Transit Access to Community Needs</p>

            <img src={loadingLogo} className="App-logo" alt="logo" />

            <h2>Enter your address below</h2>
            
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
