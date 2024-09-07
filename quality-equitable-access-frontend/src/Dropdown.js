import React, { useState } from 'react';

function DropdownMenu(stats) {
  const [selectedValue, setSelectedValue] = useState("");


  const [stats, setStats] = useState({});

  const getStatsAsColRow = (stats) => {
    
  }

  const handleChange = (event) => {
    setSelectedValue(event.target.value);
  };

  return (
    <div>
      <h1>Dropdown with Text in Columns and Rows</h1>
      <select value={selectedOption} onChange={handleChange}>
        <option value="" disabled>Select an option</option>
        <option value="option1">Option 1</option>
        <option value="option2">Option 2</option>
        <option value="option3">Option 3</option>
      </select>

      {selectedOption && (
        <div>
          <h2>{`Selected: ${selectedOption}`}</h2>
          <table border="1">
            <tbody>
              {data[selectedOption].map((row, rowIndex) => (
                <tr key={rowIndex}>
                  {row.map((col, colIndex) => (
                    <td key={colIndex}>{col}</td>
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}