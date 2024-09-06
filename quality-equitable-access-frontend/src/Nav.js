// HeaderNav.js
import React from 'react';

const HeaderNav = () => {
  const headerStyle = {
    backgroundColor: 'rgb(28, 79, 155)', // Dark blue color
    color: 'white',
    padding: '10px 20px',
    textAlign: 'center',
    position: 'fixed',
    width: '100%',
    top: '0',
    left: '0',
    zIndex: '1000',
    marginBottom: '200px',

  };

  const navStyle = {
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    listStyleType: 'none',
    padding: '0',
    margin: '0'
  };

  const navItemStyle = {
    margin: '0 15px',
    textDecoration: 'none',
    color: 'white'
  };

  return (
    <header style={headerStyle}>
      <nav>
        <ul style={navStyle}>
          <li><a href="#myscore" style={navItemStyle}>My Transit Equity Score</a></li>
          
        </ul>
      </nav>
    </header>
  );
};

//<li><a href="#calculator" style={navItemStyle}>Calculator</a></li>
//<li><a href="#map" style={navItemStyle}>Map</a></li>
//<li><a href="#contact" style={navItemStyle}>Contact</a></li>

export default HeaderNav;
