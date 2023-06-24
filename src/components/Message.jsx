import React from 'react';

// A component that renders a single message
function Message(props) {
  const chat_color = props.message.user ? 'black' : 'purple';
  return (
    <div className