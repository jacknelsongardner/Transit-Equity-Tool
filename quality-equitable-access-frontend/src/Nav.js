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
    zIndex: '1000'
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
          <li><a href="#home" style={navItemStyle}>Home</a></li>
          <li><a href="#about" style={navItemStyle}>About</a></li>
          <li><a href="#services" style={navItemStyle}>Services</a></li>
          <li><a href="#contact" style={navItemStyle}>Contact</a></li>
        </ul>
      </nav>
    </header>
  );
};

export default HeaderNav;
