import React, { useState, useEffect } from 'react';

const outerWidth = 0.1;

const ScoreDisplay = ({ targetPercentage, text, number, diameter, color }) => {
  const [percentage, setPercentage] = useState(0);

  const outerDiameter = diameter + (outerWidth * diameter);

  const inner = {
    position: 'absolute',
    top: '50%',
    left: '50%',
    width: `${diameter}vw`,
    height: `${diameter}vw`,
    maxWidth: '280px',
    maxHeight: '280px',
    borderRadius: '50%',
    backgroundColor: 'rgb(50, 79, 183)',
    transform: 'translate(-50%, -50%)', // Centers the outer circle within the container
  };

  const outer = {
    position: 'absolute',
    top: '50%',
    left: '50%',
    width: `${outerDiameter}vw`,
    height: `${outerDiameter}vw`,
    maxWidth: '300px',
    maxHeight: '300px',
    borderRadius: '50%',
    background: `${color}`,
    mask: `conic-gradient(#000 ${percentage}%, transparent 0 100%)`,
    WebkitMask: `conic-gradient(#000 ${percentage}%, transparent 0 100%)`,
    transform: 'translate(-50%, -50%) rotate(-90deg)', // Centers the inner circle and rotates
    transformOrigin: 'center',
    transition: 'mask 0.5s ease, -webkit-mask 0.5s ease',
    
  };

  const containerStyle = {
    position: 'relative',
    width: `${outerDiameter}vw`,
    height: `${outerDiameter}vh`,
    marginLeft: '3vw',
    marginTop: '20px',
    marginRight: '3vw',
    marginBottom: '10px',
  };

  const textStyle = {
    position: 'relative',
    top: '25%',
    left: '50%',
    transform: 'translate(-50%, -50%)',
    
    color: '#ffffff',
    fontSize: `clamp(12px, ${diameter / 6}vw, 50px)`, // Minimum size 12px, preferred size based on diameter, max size 24px
  };
  
  const numberStyle = {
    position: 'relative',
    top: `40%`,
    left: `50%`,
    transform: 'translate(-50%, -50%)',
    
    color: '#ffffff',
    fontWeight: 'bold',
    fontSize: `clamp(24px, ${diameter / 2}vw, 100px)`, // Minimum size 24px, preferred size based on diameter, max size 48px

    marginBottom: '20px'
  };

  useEffect(() => {
    const animation = requestAnimationFrame(() => {
      setPercentage(targetPercentage);
    });

    return () => cancelAnimationFrame(animation);
  }, [targetPercentage]);

  return (
    <div style={containerStyle}>

      <div style={outer}></div>
      <div style={inner}>

        <div style={textStyle}>{`${text}`}</div>
        <div style={numberStyle}>{`${number}`}</div>

      </div>
    </div>
  );
};

export default ScoreDisplay;
