/*
App.js - React aray\u00fcz\u00fc

Nas\u0131l \u00e7al\u0131\u015ft\u0131r\u0131l\u0131r?
1. `cd frontend`
2. Ba\u011fl\u0131l\u0131klar\u0131 kurun: `npm install`
3. Geli\u015ftirme sunucusunu ba\u015flat\u0131n: `npm start`

Bu bile\u015fen kullan\u0131c\u0131n\u0131n mood, zaman ve aktivitelerini toplayarak
Flask backend'e g\u00f6nderir ve olu\u015fan plan\u0131 g\u00f6sterir.
*/

import React, { useState } from 'react';

function App() {
  const [mood, setMood] = useState('');
  const [timeAvailable, setTimeAvailable] = useState('');
  const [activities, setActivities] = useState('');
  const [plan, setPlan] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const res = await fetch('/api/plan', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        mood,
        time_available: timeAvailable,
        activities: activities.split(',').map(a => a.trim()),
        location: 'Istanbul'
      })
    });
    const data = await res.json();
    setPlan(data);
  };

  return (
    <div>
      <h1>AI Kaos D\u00fczenleyici</h1>
      <form onSubmit={handleSubmit}>
        <input placeholder="Ruh hali" value={mood} onChange={(e) => setMood(e.target.value)} />
        <input placeholder="Bo\u015f zaman" value={timeAvailable} onChange={(e) => setTimeAvailable(e.target.value)} />
        <input placeholder="Aktiviteler, virg\u00fclle" value={activities} onChange={(e) => setActivities(e.target.value)} />
        <button type="submit">Plan Olu\u015ftur</button>
      </form>
      {plan && (
        <div>
          <p>{plan.plan}</p>
          <img src={plan.image_url} alt="plan g\u00f6rseli" width={300} />
          {plan.playlist && <p><a href={plan.playlist} target="_blank" rel="noreferrer">Spotify Listesi</a></p>}
        </div>
      )}
    </div>
  );
}

export default App;

