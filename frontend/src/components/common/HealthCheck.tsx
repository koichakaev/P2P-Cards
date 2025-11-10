import React from 'react';

export const HealthCheck: React.FC = () => {
  return (
    <div style={{ 
      padding: '40px', 
      textAlign: 'center',
      fontFamily: 'Arial, sans-serif'
    }}>
      <h1 style={{ color: '#2563eb' }}>P2P Cards 🚀</h1>
      <p style={{ fontSize: '18px', marginTop: '10px' }}>
        Frontend is running successfully!
      </p>
      <div style={{ marginTop: '20px' }}>
        <button 
          style={{
            padding: '10px 20px',
            backgroundColor: '#2563eb',
            color: 'white',
            border: 'none',
            borderRadius: '5px',
            cursor: 'pointer'
          }}
        >
          Get Started
        </button>
      </div>
    </div>
  );
};