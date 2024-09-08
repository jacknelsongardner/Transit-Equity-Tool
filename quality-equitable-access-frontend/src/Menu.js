import React, { useState } from 'react';

// Recursive Menu Component
const Menu = ({ data }) => {
  return (
    
    
    <ul>
        <MenuItem key='View a breakdown' name={'View a breakdown'} 
        content={data} 
        />
    </ul>
  );
};


// Individual Menu Item
const MenuItem = ({ name, content }) => {
    const [isOpen, setIsOpen] = useState(false);
  
    // Check if content is an object (nested structure) or a simple value
    const isNested = typeof content === 'object' && content !== null;
  
    return (
      <li>
        <div onClick={() => isNested && setIsOpen(!isOpen)} style={{ cursor: isNested ? 'pointer' : 'default' }}>
          {name}: {isNested ? <span>{isOpen ? '▼' : '►'}</span> : <span>{content}</span>}
        </div>
        {isNested && isOpen && (
          <ul style={{ marginLeft: '20px' }}>
            {Object.keys(content).map((subKey) => (
              <MenuItem key={subKey} name={subKey} content={content[subKey]} />
            ))}
          </ul>
        )}
      </li>
    );
  };
  

export default Menu;
