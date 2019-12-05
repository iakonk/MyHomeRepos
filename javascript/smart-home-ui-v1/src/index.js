import React from 'react';
import {render} from 'react-dom';
import Layout from './components/Layout/Layout';
import Dashboard from './pages/Dashboard';

render(<Layout><Dashboard/></Layout>,
       document.getElementById('main-wrapper')
)