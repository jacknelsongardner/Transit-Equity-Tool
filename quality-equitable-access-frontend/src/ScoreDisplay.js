import React, { useState, useEffect } from 'react';
import './ScoreDisplay.css'; // Assuming your CSS is in Circle.css

const outerWidth = .1;

const ScoreDisplay = ({ targetPercentage, text, diameter }) => {
  const [percentage, setPercentage] = useState(0);
  

  const outerStyle = {
    width: diameter,
    height: diameter,
    '--percentage': percentage
  };

  const innerStyle = {
    width: diameter + (outerWidth*diameter),
    height: diameter + (outerWidth*diameter)
  }

  useEffect(() => {
    const animation = requestAnimationFrame(() => {
      setPercentage(targetPercentage);
    });

    return () => cancelAnimationFrame(animation);
  }, [targetPercentage]);

  return (
    <div className="circle-container">
      <div
        className="circle"
        style={ innerStyle }
      ></div>
      <div className="middle-circle" style={outerStyle}></div>
      <div className="circle-text">{`${text}`}</div>
    </div>
  );
};

export default ScoreDisplay;
