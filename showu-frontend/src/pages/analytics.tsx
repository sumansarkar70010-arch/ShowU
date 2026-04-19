// src/pages/analytics.tsx

import { useEffect, useState } from "react";
import AnalyticsChart from "../components/AnalyticsChart";
import AnalyticsTable from "../components/AnalyticsTable";

export default function AnalyticsPage() {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/api/v1/analytics/post/1") // example: post ID 1
      .then(res => res.json())
      .then(setData);
  }, []);

  return (
    <div className="dashboard">
      <h2>Creator Dashboard</h2>
      <AnalyticsChart data={data} />
      <AnalyticsTable data={data} />
    </div>
  );
}