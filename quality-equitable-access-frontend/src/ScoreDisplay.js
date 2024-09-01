import React, { useState, useEffect } from 'react';
import './ScoreDisplay.css'; // Assuming your CSS is in Circle.css

const ScoreDisplay = ({ targetPercentage, text }) => {
  const [percentage, setPercentage] = useState(0);

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
        style={{ '--percentage': percentage }}
      ></div>
      <div className="middle-circle"></div>
      <div className="circle-text">{`${text}`}</div>
    </div>
  );
};

export default ScoreDisplay;
