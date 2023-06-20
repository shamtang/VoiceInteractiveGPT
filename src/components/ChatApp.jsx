import React, { useState, useEffect } from 'react';
import MessageList from './MessageList';
import AudioPlayer from './AudioPlayer';
import AudioRecorder from './AudioRecorder';
import axios from 'axios';

function ChatApp() {
  const [loading, setLoading] = useState(false);
  const [audioBlob, setAudioBlob] = useState(null);
  const [audioSrc, setAudioSrc] = useState('');
  const [messages, setMessages] = useState([
    { id: 1, user: false, content: "Hello, I'm ChatGPT" },
    { id: 2, user: true, content: "Hi, I'm the User" },
    { id: 3, user: