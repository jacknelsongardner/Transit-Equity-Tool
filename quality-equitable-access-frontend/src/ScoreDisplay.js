import React, { useState, useEffect } from 'react';

const outerWidth = 0.1;

const ScoreDisplay = ({ targetPercentage, text, number, diameter }) => {
  const [percentage, setPercentage] = useState(0);

  const outerDiameter = diameter + (outerWidth * diameter);

  const outerStyle = {
    position: 'absolute',
    top: '50%',
    left: '50%',
    width: `${diameter}px`,
    height: `${diameter}px`,
    borderRadius: '50%',
    backgroundColor: 'rgb(50, 79, 183)',
    transform: 'translate(-50%, -50%)', // Centers the outer circle within the container
  };

  const innerStyle = {
    position: 'absolute',
    top: '50%',
    left: '50%',
    width: `${outerDiameter}px`,
    height: `${outerDiameter}px`,
    borderRadius: '50%',
    background: 'conic-gradient(red 0%, yellow 50%, green 100%)',
    mask: `conic-gradient(#000 ${percentage}%, transparent 0 100%)`,
    WebkitMask: `conic-gradient(#000 ${percentage}%, transparent 0 100%)`,
    transform: 'translate(-50%, -50%) rotate(-90deg)', // Centers the inner circle and rotates
    transformOrigin: 'center',
    transition: 'mask 0.5s ease, -webkit-mask 0.5s ease',
  };

  const containerStyle = {
    position: 'relative',
    width: `${outerDiameter}px`,
    height: `${outerDiameter}px`,
    marginLeft: '30px',
    marginRight: '30px',
    marginBottom: '30px',
  };

  const textStyle = {
    position: 'absolute',
    top: '30%',
    left: '50%',
    transform: 'translate(-50%, -50%)',
    
    color: '#ffffff',
    fontSize: '40px',
  };

  const numberStyle = {
    position: 'absolute',
    top: '60%',
    left: '50%',
    transform: 'translate(-50%, -50%)',
    
    color: '#ffffff',
    fontWeight: 'bold',
    fontSize: '100px',
  };

  useEffect(() => {
    const animation = requestAnimationFrame(() => {
      setPercentage(targetPercentage);
    });

    return () => cancelAnimationFrame(animation);
  }, [targetPercentage]);

  return (
    <div style={containerStyle}>

      <div style={innerStyle}></div>
      <div style={outerStyle}></div>
      <div style={textStyle}>{`${text}`}</div>
      <div style={numberStyle}>{`${number}`}</div>
    </div>
  );
};

export default ScoreDisplay;
