// src/components/AnalyticsChart.tsx

import { Line } from "react-chartjs-2";
import { Chart as ChartJS, LineElement, CategoryScale, LinearScale, PointElement } from "chart.js";

ChartJS.register(LineElement, CategoryScale, LinearScale, PointElement);

export default function AnalyticsChart({ data }: { data: any[] }) {
  const chartData = {
    labels: data.map((d: any) => new Date(d.created_at).toLocaleDateString()),
    datasets: [
      {
        label: "Engagement",
        data: data.map((d: any) => 1), // each action counts as 1
        borderColor: "#ff4081",
        backgroundColor: "rgba(255,64,129,0.2)",
      },
    ],
  };

  return <Line data={chartData} />;
}