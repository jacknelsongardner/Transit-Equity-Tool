import React from 'react';
import './ScoreDisplay.css'; // Assuming the CSS is saved in Circle.css

const ScoreDisplay = ({ percentage, text }) => {
  return (
    <div className="circle-container">
      <div
        className="circle"
        style={{ '--percentage': percentage }}
      />
      <div className="circle-text">
        {text}
      </div>
    </div>
  );
};

export default ScoreDisplay;
