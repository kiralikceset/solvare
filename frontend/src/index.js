/* index.js - React uygulamas\u0131n\u0131n giri\u015f noktasi
Bu dosya `App` bile\u015fenini DOM'a render eder.
Calistirmak icin `npm start` komutunu kullanin.
*/
import React from 'react';
import { createRoot } from 'react-dom/client';
import App from './App';

const container = document.getElementById('root');
const root = createRoot(container);
root.render(<App />);
