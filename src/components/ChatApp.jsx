import React, { useState, useEffect } from 'react';
import MessageList from './MessageList';
import AudioPlayer from './AudioPlayer';
import AudioRecorder from './AudioRecorder';
import axios from 'axios';

function ChatApp() {
  const [loading, setLoading] = useState(false);
  const [audioBlob, setAudioBlob] = useState(null);
  const [audioSrc, setAudioSrc] = useState('');
 