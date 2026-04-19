import React from 'react';
import AnalyticsChart from './components/AnalyticsChart';
import AnalyticsTable from './components/AnalyticsTable';
import StoryBar from './components/StoryBar';

const App = () => {
  return (
    <div className="App">
      <header className="App-header">
        <h1>ShowU Dashboard</h1>
      </header>
      <main>
        <StoryBar />
        <AnalyticsChart data={[]} />
        <AnalyticsTable data={[]} />
      </main>
    </div>
  );
};

export default App;