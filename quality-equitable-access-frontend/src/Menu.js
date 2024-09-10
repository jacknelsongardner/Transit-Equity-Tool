import React, { useState } from 'react';

// Recursive Menu Component
const Menu = ({ data }) => {
  
  
  return (
    
    
    <ul style={{listStyleType: 'none', 
                textAlign: 'center', 
                maxWidth: `500px`, 
                alignContent: 'center', 
                margin: '0 auto',
                padding: 0
                }}>
        <MenuItem key='View a breakdown' 
        name={'View a breakdown'} 
        content={data} 
        layer={0}
        />
    </ul>
  );
};


// Individual Menu Item
const MenuItem = ({ name, content, layer }) => {
    const [isOpen, setIsOpen] = useState(false);
    const [children, setChildren] = useState([]);
  

    // Check if content is an object (nested structure) or a simple value
    const isNested = typeof content === 'object' && !Array.isArray(content) && content !== null;
  
    const openClose = () => {
        if (isNested)
        {
            setIsOpen(!isOpen);
        }
    };

    return (
      <li>
        <div onClick={openClose} style={{ cursor: isNested ? 'pointer' : 'default' }}>
          {name}: {isNested ? <span>{isOpen ? '▼' : '►'}</span> : <span>{content}</span>}
        </div>
        {isNested && isOpen && (
          <ul style={{listStyleType: 'none', textAlign: 'left', marginLeft: `${layer*10}px`}}>
            {Object.keys(content).map((subKey) => (
              <MenuItem key={subKey} 
                        name={subKey} 
                        content={content[subKey]} 
                        layer={layer + 1}
                        />
            ))}
          </ul>
        )}
      </li>
    );
  };
  

export default Menu;
